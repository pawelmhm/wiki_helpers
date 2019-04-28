title = $$("h1")[0].textContent
isbn = $$("#details-standardno td")[0]
if (isbn) {
isbn = isbn.textContent.split(" ")[0]
}
author = $$("#details-allauthors td a")[0]
if (author) {
author = author.textContent    
} else {
    author =''
}
publisher = $$("#bib-publisher-cell")[0].textContent
place = publisher.split(":")[0]
date = publisher.match(/\d\d\d\d/)[0];
imie = author.split(" ")[0]
nazwisko = author.split(" ")[1]
console.log("{{Cytuj książkę | tytuł=" 
+ title + " | isbn=" + isbn + " | imię=" + 
imie + "| nazwisko=" + nazwisko + " | miejsce=" + place + " | rok=" + 
date + "| odn=tak}}")