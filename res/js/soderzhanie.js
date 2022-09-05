/*eslint-env browser*/
(function () {
    "use strict"; // ну и ебала с этим use strict
    function close_content(event) {
        // в функцию передаём событие event у события есть цель, эта цель получается с помощью свойства .target
        // таким образом из события мы можем восстановить элемент к которому это событие применяется
        // далее сравниваем айдишники элементов, к которым применяется событие с нужными нам. И если событие применяется не
        // к тому элементу, игнорируем этот элемент. Если же событие применяется к нужному нам элементу, скрываем содержание
        if ((event.target.id === "soderzhanije_outer") || (event.target.id === "section_content_close")) {
            document.getElementById('soderzhanije_outer').style.cssText = "display:none;";
        }
    }
    function open_content() {
        document.getElementById('soderzhanije_outer').style.cssText = "display:flex;";
    }
    // вешаем слушателей событий на элементы
    document.getElementById('section_content_open').addEventListener('click', open_content);
    // document.getElementById('section_content_close').addEventListener('click', close_content);
    document.getElementById('soderzhanije_outer').addEventListener('click', close_content);
}());