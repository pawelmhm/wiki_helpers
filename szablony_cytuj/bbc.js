title = $$("h1")[0].textContent
isbn = $$("#details-standardno td")[0]
if (isbn) {
isbn = isbn.textContent.split(" ")[0]
}
author = $$("#details-allauthors td a")[0]
publisher = 'bbc.com'

unix_timestamp= $$(".mini-info-list__item .date")[0].attributes["data-seconds"].value

function padToFour(number) {
  if (number<=9999) { number = ("0"+number).slice(-2); }
  return number;
}

function timestamp_to_date(timestamp) {
    var date = new Date(timestamp );
    // Hours part from the timestamp
    var days = date.getDate();
    // Minutes part from the timestamp
    var months = date.getMonth() + 1;
    // Seconds part from the timestamp
    var years = date.getFullYear();

     // Will display time in 10:30:23 format
    var datex = years + "-" + padToFour(months) + "-" + padToFour(days) 
    return datex
}

str= "{{Cytuj stronę | tytuł=" + title 
if (author) {
    str += " | nazwisko=" + author.textContent
}
else {
    str += " | nazwisko=bbc"
}
str += " | opublikowany=" + publisher
str += " | data=" + timestamp_to_date(unix_timestamp * 1000)
str += " | data dostępu=" + timestamp_to_date(Date.now())
str += " | język=en"
str += " | url=" + window.location.href
str += " | odn=tak" 
str += " | rok=" + new Date(unix_timestamp * 1000).getFullYear()
str += "}}"
console.log(str)
