/*eslint-env browser*/

/* Исправляем год в штампе */
const date = new Date();
document.querySelectorAll('.subscribe-year').forEach((span) => {
	span.innerHTML = date.getFullYear();
});

// /* Исправляем заголовок */
// var title = document.title;
// var head = document.body.getElementsByTagName('h2')[0];
// document.title = title + " - "+head.innerHTML;