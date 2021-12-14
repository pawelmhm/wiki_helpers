#!/usr/bin/env python
import datetime
import json

import click
import html
import extruct
import pystache
import requests
from nameparser import HumanName


def parse_openg(data):
    og = dict(data['opengraph'][0]['properties'])
    dd = {}
    dd['url'] = og["og:url"]
    dd['pismo'] = og["og:site_name"]
    dd['title'] = og['og:title']
    dd['data'] = og["article:published_time"]
    return dd

def parse_ld(data):
    jl_jd = data['json-ld'][0]
    print(jl_jd)
    dd = {}
    dd['url'] = jl_jd.get("url", "")
    dd['title'] = html.unescape(jl_jd.get("headline", ""))

    dd['data'] = jl_jd["datePublished"][:10]
    author = jl_jd["author"]
    if not isinstance(author, list):
        author = [author]

    for i, au in enumerate(author, 1):
        if isinstance(au, dict):
            aut = au["name"]
        else:
            aut = au
        name = HumanName(aut)
        if i == 1:
            dd['name'] = name.first
            dd['surname'] = name.last
        else:
            dd['imię{}'.format(i)] = name.first
            dd['nazwisko{}'.format(i)] = name.last

    dd['lang'] = jl_jd.get("inLanguage", "")
    pismo = jl_jd.get("isPartOf", {}).get("name")
    if not pismo:
        pismo = jl_jd.get("publisher", {}).get("name", "")

    dd['pismo'] = pismo
    return dd

def parse_micro(data):
    micr = data['microdata']
    art = [a for a in micr if "Article" in a.get('type')]
    if not art:
        return
    art = art[0]['properties']
    dd = {}
    dd['title'] = art['headline']
    return dd


@click.command()
@click.argument('url')
def main(url):
    with open('cytuj_strone.mustache') as template_file:
        template = template_file.read()

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    data = extruct.extract(res.text, res.url)
    print(json.dumps(data))
    dd = {}

    if 'json-ld' in data and len(data.get('json-ld', [])) != 0:
        dd = parse_ld(data)
    elif 'microdata' in data and len(data.get('microdata', [])) != 0:
        raise
        dd = parse_micro(data)
    elif "opengraph" in data:
        dd = parse_openg(data)

    dzisiaj = datetime.datetime.now().isoformat()[:10]
    dd['data_d'] = dzisiaj
    if not dd.get('url'):
        dd['url'] = url
    msg = "{{" + pystache.render(template, dd) + "}}"
    print(msg)

if __name__ == "__main__":
    main()
