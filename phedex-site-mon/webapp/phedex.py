
import requests
import json
import os
import six
from units import fmtscaled
import cache
import copy

PHEDEX_API_URL = 'https://cmsweb.cern.ch/phedex/datasvc/json'
PHEDEX_INSTANCE = 'prod'
PHEDEX_REQUEST_TEMPLATE = 'https://cmsweb.cern.ch/phedex/{instance}/Request::View?request={request_id}'
SITE = None

REQUEST_CACHE = cache.SubscriptionCache.get()


def _getTransferRequest(request_id):
    global REQUEST_CACHE
    request_id = str(request_id)
    if REQUEST_CACHE.has_key(request_id):
        return copy.deepcopy(REQUEST_CACHE[request_id])
    global SITE
    params = [
        ('request', request_id),
        ('node', SITE),
    ]
    query = _constructQuery('transferrequests', params)
    r = requests.get(query, verify=False, params=params)
    result = r.json()['phedex']['request'][0]

    result['requested_by'] = _cleanDictionary(
        result['requested_by'], ['name', 'dn', 'email'])
    result = _cleanDictionary(result, ['time_create', 'requested_by'])
    # flatten result
    for k,v in six.iteritems(result['requested_by']):
        result['requested_by_' + k] = v
    del result['requested_by']
    REQUEST_CACHE[request_id] = result
    return REQUEST_CACHE[request_id]


def _cleanDictionary(dictionary, keys_to_retain):
    unwanted = set(dictionary) - set(keys_to_retain)
    for unwanted_key in unwanted:
        del dictionary[unwanted_key]
    return dictionary


def _summariseSubscription(subscription):
    retain = ['percent_files', 'time_create', 'group', 'request']
    subscription = _cleanDictionary(subscription, retain)

    request_id = subscription['request']
    request = _getTransferRequest(request_id)
    subscription.update(request)
    subscription['request_id'] = request_id
    #subscription['request_url'] = PHEDEX_REQUEST_TEMPLATE.format(
    #    instance = PHEDEX_INSTANCE,
    #    request_id = request_id
    #)
    del subscription['request']

    return subscription


def _extractDatasetInfo(result):
    datasets = result['phedex']['dataset']
    retain = ['files', 'name', 'bytes', 'subscription']
    for dataset in datasets:
        subscription = None
        if dataset.has_key('block'):
            # block types have 1 or more blocks, each with a subscription
            subscription = dataset['block'][0]['subscription'][0]
        else:
            subscription = dataset['subscription'][0]
        dataset = _cleanDictionary(dataset, retain)
        dataset.update(_summariseSubscription(subscription))
        if dataset.has_key('subscription'):
            del dataset['subscription']
        dataset['bytes_raw'] = dataset['bytes']
        dataset['bytes'] = fmtscaled(dataset['bytes'], unit='B')
    import pandas as pd
    df = pd.DataFrame(datasets)
    df.to_csv('df.csv', sep=' ')
    global REQUEST_CACHE
    cache.SubscriptionCache.set(REQUEST_CACHE)
    return df


def _transformParams(params):
    '''
        Take a list of tuples and convert into query string
    '''
    tmp = ['{0}={1}'.format(k, v) for (k, v) in params]


def _constructQuery(what, params):
    query = '{base}/{instance}/{what}'.format(
        base=PHEDEX_API_URL,
        instance=PHEDEX_INSTANCE,
        what=what,
        #params='&'.join(['{0}={1}'.format(k, v) for (k, v) in params])
    )

    return query


def getSubscriptions(site, since=1481500800, test=False):
    #url = '{base}&node={site}'.format(base = PHEDEX_BASE_URL, site = site)
    #url = PHEDEX_BASE_URL + '&node=' + site
    global SITE
    SITE = site
    result = None
    if test:
        result = copy.deepcopy(cache.PhedexCache.get())
        #test_file = os.path.join(os.path.dirname(__file__), 'full_qry.txt')
        #with open(test_file) as f:
        #    result = json.loads(f.read())
    else:
        params = [
            ('create_since', since),
            ('node', site),
        ]
        query = _constructQuery('subscriptions', params)
        r = requests.get(query, verify=False)
        result = r.json()
    return _extractDatasetInfo(result)
