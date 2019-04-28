title = $$("h1")[0].textContent


author = $$("a[rel=author] span")[0]
if (author) {
    author = author.textContent

}
else {
    author = "Charlemagne"
}
publisher = 'The Economist'

unix_timestamp = $$("time.blog-post__datetime")
unix_timestamp = unix_timestamp[0].attributes['datetime'].value.slice(0, 10)
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
str += " | nazwisko=" + author
str += " | opublikowany=" + publisher
str += " | data=" + unix_timestamp

str += " | data dostępu=" + timestamp_to_date(Date.now())
str += " | język=en"
str += " | url=" + window.location.href
str += " | odn=tak" 
str += " | rok=" + unix_timestamp.slice(0, 4)
str += "}}"
console.log(str)
