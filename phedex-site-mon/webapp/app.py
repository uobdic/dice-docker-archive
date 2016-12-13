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
@cache.cached(timeout=60)
def test():
    provider = str(os.environ.get('PROVIDER', 'world'))
    site = os.environ.get('SITE', 'T2_UK_SGrid_Bristol')
    datasets = getSubscriptions(site, test=True)
    template = '{:<50} {:<10} {:<10}'
    lines = [template.format('Name', 'group', 'request')]
    for dataset in datasets:
        print dataset
        name = dataset['name']
        group = dataset['group']
        request = dataset['requested_by_name']
        line = template.format(name, group, request)
        lines.append(line)
        break

    body = '<br>'.join(lines)
    dataset_raw = json.dumps(datasets[0], indent=4).replace('\n', '<br>')
    body += '<br> RAW: <br>' + dataset_raw

    return plot(body)


def plot(content, data=[]):
    x = list(range(0, 100 + 1))
    fig = figure(title="Polynomial")
    fig.line(x, [i ** 2 for i in x], line_width=2)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = render_template(
        'overview.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        content=content,
    )
    return encode_utf8(html)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
