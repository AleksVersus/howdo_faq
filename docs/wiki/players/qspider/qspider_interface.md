---
sidebar_position: 4
sidebar_label: Взаимодействие с интерфейсом (расширенные возможности qSpider)
---
# Взаимодействие с интерфейсом (расширенные возможности qSpider)

**qSpider** в отличие от классического плеера позволяет авторам более широко работать с выводимой на экран HTML-разметкой.

Управление интерфейсом и HTML-разметкой из кода игры осуществляется с помощью [встроенной в плеер библиотеки](qspider_inclib) "`qspider`". Чтобы воспользоваться этой библиотекой, необходимо подключить её в начале игры, как обычный модуль QSP:

```qsp
inclib 'qspider'
```

В **qSpider** вы можете:

* Создавать собственные [темы оформления](qspider_themes) и управлять ими.
* Взаимодействовать с HTML через [специальные теги](qspider_spectags).
* [Связывать элементы форм HTML](#Привязка элементов HTML-форм к QSP-переменными) со значениями переменных QSP.
* [Вызывать код QSP по событию](#Вызов QSP-кода по событию в плеере) в браузере (плеере).
* [Вызывать встроенную команду плеера](#Вызов команд плеера) при клике по HTML-элементу.

## Привязка элементов HTML-форм к QSP-переменными

В **qSpider** Элементы HTML-форм (`input`, `select`, `textarea` и др.) можно связать с QSP-переменной. Для этого нужно использовать специальный атрибут `qsp-bind`.

Связь двунаправленая — изменение переменной обновит элемент и изменение элемента (ввод текста или выбор опции) записываются в переменную.

Примеры использования атрибута `qsp-bind`:

```html
<input type="text" qsp-bind="$username"> <input type="password" qsp-bind="$form_password"> <input type="color" value="#e66465" qsp-bind="$color"> <input type="checkbox" value="1" qsp-bind="enable"> <select qsp-bind="$car">
    <option value="mercedes">Mercedes</option>
    <option value="audi">Audi</option>
</select>
```

Это позволяет быстрее и проще создавать собственные диалоговые окна для взаимодействия с игроком.

## Вызов QSP-кода по событию в плеере

Вы можете вызывать код QSP при определённых событиях в плеере с помощью новых атрибутов, начинающихся с префикса `qsp-on:`.

Поддерживаются следующие атрибуты:

* `qsp-on:click` — одинарный клик
* `qsp-on:dblclick` — двойной клик
* `qsp-on:contextmenu` — клик правой кнопкой
* `qsp-on:mouseenter` — наведение курсора
* `qsp-on:mouseleave` — выход курсора за пределы элемента

Содержимым атрибутов должен быть валидный код QSP. Примеры использования атрибутов:

```html
<div qsp-on:click="exec: msg 'click'" qsp-on:dblclick="exec: msg 'dblclick'">Click me</div>
<div qsp-on:contextmenu="exec: menu '$context_menu'">Right Click me</div>
<div qsp-on:mouseenter="exec: pl 'enter'" qsp-on:mouseleave="exec: pl 'leave'">Hover me</div>
```

## Вызов команд плеера

Вы можете вызывать множество команд плеера по клику на HTML-элемент, используя специальный атрибут `qsp-command`.

Пример использования атрибута:

```html
<button qsp-command="resume">Resume</button>
```

Поддерживаются следующие команды плеера:

* `quit` — выход из игры на полку игр
* `restart` — перезапуск игры
* `resume` — продолжить игру (закрытие меню паузы)
* `mute` — выключить звук
* `unmute` — включить звук
* `quicksave` — быстрое сохранение
* `quickload` — быстрая загрузка
* `pause:saves` — открыть меню сохранения
* `pause:preferences` — открыть настройки
* `scroll:main:bottom` и `scroll:main:top` — прокрутка окна основного описания
* `scroll:stats:bottom` и `scroll:stats:top` — прокуртка окна доп описания

Эти команды можно вызывать и непосредственно из кода QSP, если подключить [встроенную библиотеку](qspider_inclib) `qspider`.

Пример вызова команд из кода QSP:

```qsp
inclib 'qspider'
@qspider_quit()
@qspider_open_pause_screen('saves')
```

## Другие статьи по qSpider

* [qSpider — общая информация](index)
* [Конфигурационный файл](qspider_gamecfg)
* [Особенности запуска и работы игр AeroQSP на qSpider](qspider_aeroqsp)
* [Темы оформления](qspider_themes)
* [Специальные теги](qspider_spectags)
* [Встроенная библиотека](qspider_inclib)
* [Стандалон-сборка игры на qSpider](qspider_standalone)
