/*eslint-env browser*/
(function () {
    "use strict"; // ну и ебала с этим use strict
    function close_content(event) {
        // в функцию передаём событие event у события есть цель, эта цель получается с помощью свойства .target
        // таким образом из события мы можем восстановить элемент к которому это событие применяется
        var sdr = document.getElementById('soderzhanije_outer'); // здесь мы получаем элемент, на который хотим воздействовать
        // далее сравниваем айдишники элементов, к которым применяется событие с нужными нам. И если событие применяется не
        // к тому элементу, игнорируем этот элемент. Если же событие применяется к нужному нам элементу, скрываем содержание
        if ((event.target.id === "soderzhanije_outer") || (event.target.id === "section_content_close")) {
            sdr.style.cssText = "display:none;";
        }
    }
    function open_content() {
        var sdr = document.getElementById('soderzhanije_outer');
        sdr.style.cssText = "display:flex;";
    }
    var btn_open = document.getElementById('section_content_open');
    btn_open.onclick = open_content;
    var btn_close = document.getElementById('section_content_close');
    btn_close.onclick = close_content;
    var sdr = document.getElementById('soderzhanije_outer');
    sdr.onclick = close_content;
}());