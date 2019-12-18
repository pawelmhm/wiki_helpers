from jinja2 import Template

def main():
    infobox = Template("""Biogram infobox
|imię i nazwisko      = {{name}}
|imię i nazwisko org  =
|grafika              = {{grafika}}
|opis grafiki         =
|data urodzenia       = {{birth}}
|miejsce urodzenia    = {{where}}
|data śmierci         = {{dead}}
|miejsce śmierci      =
|zawód                =
|odznaczenia          =
|commons              =
|www                  =
""")
    name = input("name ")
    grafika = input("grafika ")
    dead = input("dead ")
    birth = input("birth ")
    where = input('where ')
    output = infobox.render(name=name, grafika=grafika, dead=dead, birth=birth, where=where)
    output = "{{" + output + "}}"
    print(output)
    rest = Template("""
'''{{name}}''' (ur. {{urodz}} w {{where}}, zm. {{dead}}) - {{opis}}
== Przypisy ==""")
    opis = input('opis ')

    rest = rest.render(name=name, urodz=birth, opis=opis, dead=dead, where=where)
    output += rest
    output += "\n{{Przypisy}}"
    print(output)

    biblio = """
== Bibliografia =="""
    book = input('book ')
    biblio += "\n" + "{{" + book + "}}"
    output += biblio
    output += "\n{{Kontrola autorytatywna}}"
    print(output)

main()
