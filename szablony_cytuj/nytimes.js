date = $$("header time[datetime]")[0].attributes['datetime'].value;
title = $$("h1")[0].textContent
date_now = new Date()
date_now_s = date_now.getFullYear() + "-" 
date_now_s += date_now.getMonth() + 1 
date_now_s += "-" + date_now.getDate() ;
autor = $$("*[itemprop*=author] *")[0].attributes['data-byline-name']
if (autor) {
    autor = autor.value
    
} else{
    autor = $$("*[itemprop*=author] span")[0].textContent;
}
console.log(autor)
imie = autor.split(" ")[0]
nazwisko = autor.split(" ")[1]

str = "{{Cytuj stronę | "
data = [
    "data=" + date,
    "tytuł=" + title,
    "opublikowany=New York Times",
    "data dostępu=" + date_now_s,
    "imię=" + imie,
    "nazwisko=" + nazwisko,
    "rok=" + date.slice(0, 4),
    "odn=tak",
    "url=" + window.location.href,
    "język=en"
]
str += data.join(" | ")
str += "}}"
console.log(str)