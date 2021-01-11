#!/usr/bin/env python
import datetime
import json

import click
import extruct
import pystache
import requests
from nameparser import HumanName


def parse_ld(data):
    jl_jd = data['json-ld'][0]
    print(jl_jd)
    dd = {}
    dd['url'] = jl_jd.get("url", "")
    dd['title'] = jl_jd["headline"]
    dd['data'] = jl_jd["datePublished"][:10]
    author = jl_jd["author"]
    if not isinstance(author, list):
        author = [author]

    for i, au in enumerate(author, 1):
        aut = au["name"]
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


@click.command()
@click.argument('url')
def main(url):
    with open('cytuj_strone.mustache') as template_file:
        template = template_file.read()

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    print(res)
    data = extruct.extract(res.text, res.url)
    # print(json.dumps(data))
    # return
    dd = {}

    if 'json-ld' in data and len(data.get('json-ld', [])) != 0:
        dd = parse_ld(data)

    dzisiaj = datetime.datetime.now().isoformat()[:10]
    dd['data_d'] = dzisiaj
    if not dd.get('url'):
        dd['url'] = url
    msg = "{{" + pystache.render(template, dd) + "}}"
    print(msg)

if __name__ == "__main__":
    main()
