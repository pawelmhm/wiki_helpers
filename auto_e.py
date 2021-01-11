import sys
import json

def main(f):
    with open(f) as fi:
        data = json.load(fi)[0]

    name, surname = data['author'].split(" ", 1)
    a = f'url={data["url"]} | imię={name} | nazwisko={surname} | tytuł={data["headline"]} | język={data["inLanguage"]} | data={data["datePublished"]}'.format(data)
    print('<ref>{{Cytuj stronę | ' + a + '}}</ref>')


if __name__ == "__main__":
    main(sys.argv[1])
