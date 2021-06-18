/*eslint-env browser*/
/* функция исправляющая год в штампе */
var ds = new Date();
var stamp_year = document.getElementById("date_stamp");
stamp_year.innerHTML = ds.getFullYear();
