from __future__ import print_function
import json
import os
import pandas as pd

from units import fmtscaled
from phedex import _cleanDictionary, _summariseSubscription

test_file = os.path.join(os.path.dirname(__file__), 'full_qry.txt')
with open(test_file) as f:
    result = json.loads(f.read())

datasets = result['phedex']['dataset']
print('Found', len(datasets), 'datasets')


retain = ['files', 'name', 'bytes', 'subscription', 'block']

for i, dataset in enumerate(datasets):
    if i > 9:
        break
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
# print(df)
df.to_csv('split.csv', sep=' ')
# return df
