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
            e['znaczenie'] = e.get('custom1')
            e['pismo'] = e.get('secondary_name', e.get('journal_name'))
            title = e.get('title', e.get('primary_title'))
            e['title'] = title

            print("{{" + pystache.render(template, e) + "}}")

main()

