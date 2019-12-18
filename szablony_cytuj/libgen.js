title = $$("h1")[0].textContent
$$("#info p").forEach(function (elem) {
    value = elem.textContent //.split(":");
    if (value.match("Author")) {
        author = value.split(":", 2)[1].trim();
    }
    if (value.match('Publisher')) {
        wydawca = value.split(",")[0].split(":")[1]
        date = value.split(",")[1].split(":")[1]
    }
    if (value.match("ISBN")) {
        isbn = value.split(":", 2)[1]
    }
    console.log(author.split(" " ))
})

imie = author.split(" ")[0]
nazwisko = author.split(" ").slice(1)
console.log("{{Cytuj książkę | tytuł=" 
+ title + " | isbn=" + isbn + " | imię=" + 
imie + "| nazwisko=" + nazwisko + " | rok=" + 
date + "| odn=tak}}")
