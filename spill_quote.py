#!/usr/bin/env python
import datetime
import json

import click
import extruct
import requests


@click.command()
@click.argument('url')
def main(url):
    res = requests.get(url)
    print(res)
    data = extruct.extract(res.text, res.url)
    jl_jd = data['json-ld'][0]
    root = '<ref>{{Cytuj stronę |'
    root += f'url={jl_jd["url"]}'
    root += f'| tytuł={jl_jd["headline"]} | data={jl_jd["datePublished"][:10    ]}'
    author = jl_jd["author"][0]["name"]
    name, surname = author.split(" ", 2)
    root += f' | imię={name} | nazwisko={surname}'
    root += f'| język={jl_jd["inLanguage"]}'
    root += f'| opublikowany={jl_jd["isPartOf"]["name"]}'
    dzisiaj = datetime.datetime.now().isoformat()[:10]
    root += f' | data dostępu={dzisiaj}'
    root += '}}</ref>'
    print(root)

if __name__ == "__main__":
    main()