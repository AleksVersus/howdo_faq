---
sidebar_position: 5
sidebar_label: Темы оформления
---
# Темы оформления

**qSpider** позволяет вам писать собственные темы оформления, которые затем можно переключать прямо из кода игры. Таким образом вы можете написать несколько тем для различных нужд, и включать их по мере необходимости.

Например, у вас могут быть различные темы для локаций-помещений и локаций-пустошей. У вас могут быть отдельные темы для локаций-страниц, где вы представляете информацию об игре. Можно оформить темы для визуализации чтения книг, взаимодействия с хранилищами и так далее.

Отделение интерфейса от кода игры — это полезная практика, позволяющая разнести оформление и логику. Так код становится более читаемым и понятным.

Тема в qSpider представляет собой HTML-код, где для каждого элемента плеера используется свой HTML-тег.

## Создание тем

Свою тему вы можете создать, модифицируя шаблон одной из встроенных тем:

  * [Классическая](https://github.com/QSPFoundation/qspider/blob/master/public/themes/classic.html)
  * [Aero](https://github.com/QSPFoundation/qspider/blob/master/public/themes/aero.html)

Если вы когда-нибудь стилизовали HTML-разметку с помощью CSS, отредактировать тему для вас не составит труда.

Обратите внимание на первые строки темы (ниже пример из встроенной классической темы):

```html
<qspider-theme name="qspider:classic">
<css-link src="qspider:themes/common.css"></css-link>
<css-link src="qspider:themes/classic.css"></css-link>
```

В теге `qspider-theme` в атрибуте `name` указывается название темы. Именно это название в дальнейшем будет использоваться для указания темы по умолчанию и при переключении тем.

Префикс `qspider:` в этом атрибуте указывает на то, что тема встроена в плеер, а значит **qSpider** будет искать эту тему в своих внутренних ресурсах. Названия созданных вами тем должны указываться без префикса `qspider:`.

Теги `css-link` содержат ссылки на CSS-файлы со стилями для темы. Точно так же: обратите внимание на атрибут `src`. Префикс `qspider:` указывает, что CSS будет браться из внутренних ресурсов плеера. Вам нужно указывать пути без префикса `qspider:` для реально существующих в игре файлов. Пути к CSS файлам указываются в темах **относительно конфигурационного файла игры** (`game.cfg`), в котором эти темы подключаются.

## Подключение тем

Для подключения своих тем к игре, пропишите в файле конфигурации параметры **themes** и **defaultTheme**:

```qsp
[[game]]
id = "test-asset-qspider"
title = "Суппер-пуппер-мега-игра"
file="game_start.qsps"
themes = ["themes/intro_page.html", "themes/game_main.html"]
defaultTheme = "intro-page"
```

В параметре **themes** размещается список путей к темам относительно файла конфигурации.

В параметре **defaultTheme** указывается название темы, которая будет использоваться по умолчанию (атрибут `name` тега `qspider-theme`).

## Переключение тем

Переключение темы можно производить непосредственно из кода игры, используя [встроенную библиотеку](qspider_inclib) "`qspider`":

```qsp
inclib 'qspider'
@qspider_change_theme('game-main')
```

## Другие статьи по qSpider

* [qSpider — общая информация](index)
* [Конфигурационный файл](qspider_gamecfg)
* [Особенности запуска и работы игр AeroQSP на qSpider](qspider_aeroqsp)
* [Взаимодействие с интерфейсом](qspider_interface)
* [Специальные теги](qspider_spectags)
* [Встроенная библиотека](qspider_inclib)
* [Стандалон-сборка игры на qSpider](qspider_standalone)
