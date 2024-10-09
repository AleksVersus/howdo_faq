---
sidebar_position: 7
---
# Встроенная библиотека `qspider`

В плеер **qSpider** втроена специальная библиотека `qspider`, которая содержит набор функций для управления интерфейсом вашей игры.

Чтобы воспользоваться функциями библиотеки, её нужно подключить, как [обычный модуль QSP](../../advanced/modules), написав, например в самой первой локации в игре команду:

```qsp
inclib 'qspider'
```

Все функции библиотеки вызываются из кода QSP.

## Команды плеера

Данные функции позволяют управлять поведением плеера прямо из кода QSP.

* `qspider_quit` — выход из игры на полку игр. 
    ```qsp
    @qspider_quit()
    ```

* `qspider_restart` — перезапуск текущей игры. 
    ```qsp
    @qspider_restart()
    ```

* `qspider_resume` — продолжить игру (закрыть меню паузы). 
    ```qsp
    @qspider_resume()
    ```

* `qspider_mute` — Выключить звук. 
    ```qsp
    @qspider_mute()
    ```

* `qspider_unmute` — Включить звук. 
    ```qsp
    @qspider_unmute()
    ```

* `qspider_toggle_mute` — Переключить звук. 
    ```qsp
    @qspider_toggle_mute()
    ```

* `qspider_quicksave` — Переключить звук. 
    ```qsp
    @qspider_quicksave()
    ```

* `qspider_quickload` — Переключить звук. 
    ```qsp
    @qspider_quickload()
    ```

* `qspider_open_pause_screen` — открыть меню паузы. Аргументы `$args[0]`:
    * `saves` — меню сохранений. 
        ```qsp
        @qspider_open_pause_screen('saves')
        ```
    * `preferences` — меню настроек. 
        ```qsp
        @qspider_open_pause_screen('preferences')
        ```
    * без аргументов — основной раздел меню паузы. 
        ```qsp
        @qspider_open_pause_screen()
        ```

* `qspider_scroll` — прокрутить окно (вверх или вниз). Аргументы:
    * `$args[0]` — указать окно:
        * `main` — окно основного описания. 
            ```qsp
            @qspider_scroll('main', 'bottom')
            ```
        * `stats` — окно дополнительного описания. 
            ```qsp
            @qspider_scroll('stats', 'bottom')
            ```
    * `$args[1]` — указать направление:
        * `top` — прокрутить до верха. 
            ```qsp
            @qspider_scroll('main', 'top')
            ```
        * `bottom` — прокрутить до низа. 
            ```qsp
            @qspider_scroll('main', 'bottom')
            ```

## Управление темами

Вы можете переключать созданные заранее [темы оформления](qspider_themes), используя встроенную функцию библиотеки:

* `qspider_change_theme` — включить указанную тему оформления.
    ```qsp
    @qspider_change_theme('dark-theme')
    ```
    Аргументом указывается название темы.

## Управление слоями

Эти функции позволяют управлять поведением слоёв, созданных с помощью [специальных тегов](qspider_spectags) **qsp-layer**. По умолчанию все слои скрыты.

Пример слоя:

```html
<qsp-layer name="layer1" index="10">Some UI</qsp-layer>
```

* `qspider_show_layer` — показать слой на экране.
    ```qsp
    @qspider_show_layer('layer1')
    ```
    В качестве аргумента передаётся название слоя, соответствующее значению атрибута `name`.

* `qspider_hide_layer` — скрыть слой с экрана.
    ```qsp
    @qspider_hide_layer('layer1')
    ```
    В качестве аргумента передаётся название слоя.

* `qspider_show_only_layer` — показать указанный слой, а остальные скрыть.
    ```qsp
    @qspider_show_only_layer('layer1')
    ```
    В качестве аргумента передаётся название слоя.

## Управление регионами

Данные функции позволяют управлять поведением регионов, созданных с помощью [специального тега](qspider_spectags) **qsp-region**.

Пример региона:

```html
<qsp-region name="region1"></qsp-region>
```

* `qspider_update_region` — полностью перезаписать содержимое региона.
    ```qsp
    @qspider_update_region('region1', '<b>Текст</b>')
    ```
    Аргументы:
        * `$args[0]` — название региона.
        * `$args[1]` — новое содержимое региона.

* `qspider_prepend_region` — вставить содержимое в начало региона.
    ```qsp
    @qspider_prepend_region('region1', 'Текст<br>')
    ```
    Аргументы:
        * `$args[0]` — название региона.
        * `$args[1]` — добавляемое содержимое региона.

* `qspider_append_region` — вставить содержимое в начало региона.
    ```qsp
    @qspider_append_region('region1', '<br>Конец')
    ```
    Аргументы:
        * `$args[0]` — название региона.
        * `$args[1]` — добавляемое содержимое региона.

* `qspider_scroll_region` — прокрутить регион. Аргументы:
    * `$args[0]` — название региона.
    * `$args[1]` — направление прокрутки:
        * `top` — прокрутить до верха. 
            ```qsp
            @qspider_scroll_region('region1', 'top')
            ```
        * `bottom` — прокрутить до низа. 
            ```qsp
            @qspider_scroll_region('region1', 'bottom')
            ```

* `qspider_clear_region` — очистить содержимое региона.
    ```qsp
    @qspider_clear_region('region1')
    ```
    В качестве аргумента передаётся название региона.

## Вызов событий на объекте `window`

При необходимости вы можете вызвать на объекте `window` браузера/плеера событие с указанным именем. Это позволит, например, в нужный момент запустить JavaScript.

Команда для вызова события из кода QSP:

* `qspider_event` — вызывает событие с указанным именем. Аргументы:
    * `$args[0]` — имя события, которое нужно вызвать.
    * `args[1] ... args[18]` — числовые и текстовые аргументы, которые нужно передать в событие.

Примеры вызова событий:

```qsp
@qspider_event('test_event') & ! вызов события без аргументов
@qspider_event('event_with_args', 1, "test") & ! с аргументами
```

Также, см. статью: [qSpider v.0.10.0](https://ifhub.club/2021/05/23/qspider-0100.html)

## Другие статьи по qSpider

* [qSpider — общая информация](index)
* [Конфигурационный файл](qspider_gamecfg)
* [Особенности запуска и работы игр AeroQSP на qSpider](qspider_aeroqsp)
* [Взаимодействие с интерфейсом](qspider_interface)
* [Темы оформления](qspider_themes)
* [Специальные теги](qspider_spectags)
* [Стандалон-сборка игры на qSpider](qspider_standalone)

