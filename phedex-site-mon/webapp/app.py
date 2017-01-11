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

from units import fmtscaled
import pandas as pd


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
    pd.set_option('display.max_colwidth', -1)
    provider = str(os.environ.get('PROVIDER', 'world'))
    site = os.environ.get('SITE', 'T2_UK_SGrid_Bristol')
    datasets = getSubscriptions(site, test=True)
    template = '{:<50} {:<10} {:<10}'
    lines = [template.format('Name', 'group', 'request')]

    datasets = datasets[datasets['group'] == 'local']

    grouped_by_user = datasets.groupby(['requested_by_name'])
    datasets_by_user = datasets[['requested_by_name', 'name', 'bytes']].groupby(datasets['requested_by_name'])

    test = pd.DataFrame(
        {
            'usage': grouped_by_user['bytes_raw'].sum(),
        }
        ).sort_values('usage', ascending=False).reset_index()

    users = datasets['requested_by_name'].unique()


    datasets_by_user_str = ''
    for user in users:
        data = datasets[datasets['requested_by_name']==user].sort_values('bytes_raw', ascending=False).reset_index()
        datasets_by_user_str += '<h1>{0}</h1><br >'.format(user)
        datasets_by_user_str += data[['name', 'bytes']].to_html()
        datasets_by_user_str += '<br />'

    from units import fmtscaled
    from functools import partial
    scaleUnits = partial(fmtscaled, unit="B")
    test['usage_scaled'] = test['usage'].apply(scaleUnits)

    body = '<br>'.join(lines)
    body += '<br> RAW: <br>' + test[['requested_by_name', 'usage_scaled']].to_html()
    body += datasets_by_user_str

    body += '<br \>' + plot_bar(test)

    return plot(body, test)


def plot(content, data=[]):
    x = list(range(0, 100 + 1))
    fig = figure(title="Polynomial")
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

def plot_bar(df):
    import plotly.plotly as py
    import plotly.graph_objs as go
    from plotly import offline

    df = df.sort_values(['usage'])

    data = [
        go.Bar(
            x=df['usage'], # assign x as the dataframe column 'x'
            y=df['requested_by_name'],
            orientation='h',
            marker=dict(
                #color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                )
            ),
        )
    ]

    maxName = df['requested_by_name'].apply(len).max()
    layout = go.Layout(
        title='Local CMS data usage',
        #bargap = 0.9,
        boxgap = 50,
        barmode='stack',
        margin=go.Margin(
            l=maxName*7,
            #r=50,
            #b=100,
            #t=200,
            pad=10
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            autotick=False,
            showticklabels=True,
        ),
        xaxis=dict(
            ticksuffix='B',
        )
    )
    return offline.plot({'data': data, 'layout':layout},
                        output_type='div')#, image_width=800)

def _display_by_group(df):
    pass

def _display_by_user(df):
    pass

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
