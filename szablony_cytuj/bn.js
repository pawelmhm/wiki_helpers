txt_title = $$("#bibTitle")[0].textContent;
title_x = txt_title.split("/");
title = title_x[0].trim();
author = title_x[1].trim();

more_data = $$("#bibInfoDetails tr")
console.log(title)
isbn = ''
for (i=0 ;i < more_data.length; i++) {
    cell_name = more_data[i].cells[0].textContent;
    cell_cont = more_data[i].cells[1].textContent;
    if (cell_name.search("Adres") != -1) {
        place = cell_cont.split(":")[0].trim();
        date = cell_cont.match(/\d\d\d\d/)[0];
    }
    if (cell_name.search("ISBN") != -1) {
        isbn = cell_cont.trim()
    }
}


console.log("{{Cytuj książkę | tytuł=" + title + " | isbn=" + isbn + " | autor=" + author + " | miejsce=" + place + " | data=" + date + "}}")