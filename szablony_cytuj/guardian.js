title = $$("h1")[0].textContent


author = $$("a[rel=author] span")[0].textContent
publisher = 'The Guardian'

unix_timestamp = $$("time[itemprop=datePublished]")[0].attributes["data-timestamp"]
unix_timestamp = unix_timestamp.value

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
str += " | nazwisko=" + author.split(" ")[1] + " | imię=" + author.split(" ")[0]
str += " | opublikowany=" + publisher
str += " | data=" + timestamp_to_date(unix_timestamp / 1)
str += " | data dostępu=" + timestamp_to_date(Date.now())
str += " | język=en"
str += " | url=" + window.location.href
str += " | odn=tak" 
str += " | rok=" + new Date(unix_timestamp / 1).getFullYear()
str += "}}"
console.log(str)
copn
