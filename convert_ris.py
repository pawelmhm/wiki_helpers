from RISparser import readris
import click
import pystache
import html


@click.command()
@click.argument('filename')
def main(filename):
    with open('cytuj.mustache') as template_file:
        template = template_file.read()

    with open(filename) as bib_file:
        entries = readris(bib_file)
        for e in entries:
            print(e)
            for i, a in enumerate(e['authors']):
                surname, name = a.split(",", 1)
            e['name'] = name
            e['surname'] = surname
            e['znaczenie'] = e['custom1']
            e['pismo'] = e['secondary_title']
            e['title'] = html.unescape(e['title'])

            print("{{" + pystache.render(template, e) + "}}")

main()

