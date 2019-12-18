title = $$("h1")[0].textContent
pismo = $$(".journalHeader a")[0].textContent;
doi = $$(".property_doi")[0].textContent;

author = '';
i = 1;
$$(".cardArticles a[itemprop=author]").forEach(function (e) {
    i+= 1;
    author += e.textContent + "";
})
console.log(author);
str = "{{Cytuj pismo| tytuł=" 
str += title.trim() + " |"
str += "czasopismo=" + pismo + "|"
str += "doi=" + doi.split(":")[1].trim() + "|";
str += "autor=" + author
str += "}}"

