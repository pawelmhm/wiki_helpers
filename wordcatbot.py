import requests
import parsel
import sys
import json
import pystache

def main(url):
    res = requests.get(url)
    sel = parsel.Selector(text=res.text, type='html')
    data = sel.css("#__NEXT_DATA__::text").get()
    dds = json.loads(data)["props"]["pageProps"]["record"]
    with open('cytuj_ksiazke.mustache') as template_file:
        template = template_file.read()

    data = {
        "author": dds["creator"],
        "title": dds["title"],
        "oclc": dds["oclcNumber"],
        "year": dds['publicationDate'],
        "place": dds['publicationPlace'],
        "isbn": dds["isbn13"],
        "publisher": dds["publisher"]
    }

    msg = "{{" + pystache.render(template, data) + "}}"
    print(msg)


main(sys.argv[1])
