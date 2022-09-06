/*eslint-env browser*/

/* Исправляем год в штампе */
var ds = new Date();
var stamp_faq = document.getElementById("date_stamp_faq");
var stamp_gamrus = document.getElementById("date_stamp_gamrus");
stamp_faq.innerHTML = ds.getFullYear();
stamp_gamrus.innerHTML = ds.getFullYear();

/* Исправляем заголовок */
var title = document.title;
var head = document.body.getElementsByTagName('h2')[0];
document.title = title + " - "+head;