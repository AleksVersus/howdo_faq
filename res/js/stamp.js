/*eslint-env browser*/
/* функция исправляющая год в штампе */
var ds = new Date();
var stamp_faq = document.getElementById("date_stamp_faq");
var stamp_gamrus = document.getElementById("date_stamp_gamrus");
stamp_faq.innerHTML = ds.getFullYear();
stamp_gamrus.innerHTML = ds.getFullYear();
