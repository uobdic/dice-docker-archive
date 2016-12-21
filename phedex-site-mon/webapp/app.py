from __future__ import unicode_literals
import os
import json

from flask import Flask, render_template
from flask.ext.cache import Cache
from phedex import getSubscriptions

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.charts import Bar


app = Flask('PhEDEx site mon')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    site = os.environ.get('SITE', 'T2_UK_SGrid_Bristol')
    datasets = getSubscriptions(site, test=False)
    template = '{:<50} {:<10} {:<10}'
    lines = [template.format('Name', 'group', 'request')]
    for dataset in datasets:
        name = dataset['name']
        group = dataset['group']
        request = dataset['requested_by_name']
        line = template.format(name, group, request)
        lines.append(line)

    body = '<br>'.join(lines)

    return body


@app.route('/test')
#@cache.cached(timeout=60)
def test():
    provider = str(os.environ.get('PROVIDER', 'world'))
    site = os.environ.get('SITE', 'T2_UK_SGrid_Bristol')
    datasets = getSubscriptions(site, test=True)
    template = '{:<50} {:<10} {:<10}'
    lines = [template.format('Name', 'group', 'request')]

    grouped_by_user = datasets.groupby(['requested_by_name'])['bytes_raw'].sum()
    #print datasets.groupby('requested_by_name').groups
    #print grouped.sum()

    for g in grouped_by_user:
        print 'Total', g
    import pandas as pd
    #test = pd.DataFrame({'usage': datasets.groupby(['requested_by_name'])['bytes_raw'].sum()}).reset_index()
    #print test

    test = pd.DataFrame(
        {
            'usage': datasets.groupby(['requested_by_name'])['bytes_raw'].sum()
        }).reset_index()
    #test['group'] = datasets[test['requested_by_name']]
    from units import fmtscaled
    from functools import partial
    scaleUnits = partial(fmtscaled, unit="B")
    #test['usage'] = test['usage'].apply(scaleUnits)
    #print test

#    for dataset in datasets:
#        print dataset.values, dataset
#        name = dataset['name']
#        group = dataset['group']
#        request = dataset['requested_by_name']
#        line = template.format(name, group, request)
#        lines.append(line)
#        break

    body = '<br>'.join(lines)
    #body += '<br> RAW: <br>' + test.to_html()

    return plot(body, test)


def plot(content, data=[]):
    x = list(range(0, 100 + 1))
    fig = figure(title="Polynomial")
    print(dir(fig))
    #fig.line(x, [i ** 2 for i in x], line_width=2)
    #fig.hbar(data['requested_by_name'], data['usage'])
    p=Bar(data, 'requested_by_name', values='usage')

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(p)
    html = render_template(
        'overview.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        content=content,
    )
    return encode_utf8(html)

def _display_by_group(df):
    pass

def _display_by_user(df):
    pass

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
