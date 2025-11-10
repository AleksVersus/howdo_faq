---
sidebar_position: 3
sidebar_label: Quest Navigator
---
# Quest Navigator

Плеер **Quest Navigator** создавался как следующий шаг развития платформы **QSP**, на смену устаревшим **классическому плееру** и **AeroQSP**. Однако уже много лет **Quest Navigator** не обновляется и не развивается.

В настоящий момент мы не рекомендуем пользоваться этим плеером, так как существует более современный, развивающийся плеер [qSpider](qspider/index.md).

## Принципиальные отличия

*  Содержимое отрисовывается средствами браузера, благодаря этому есть полная поддержка HTML, CSS и Javascript (к сожалению, HTML-движок **Quest Navigator**а морально устарел и не соответствует современным стандартам).
*  Оформление отделено от кода игры.
*  Облегчено портирование плеера благодаря перемещению платформонезависимой части логики в общий Javascript-фреймворк.
*  Поддержка мобильных платформ (Android, iOS).

## Доступен на платформах

*  Android
*  iOS

## Будущие платформы

*  Windows Phone 8 (разработка не начата)
*  Десктопные версии Windows (в разработке). Тема на форуме: [Quest Navigator для Windows](https://qsp.org/index.php?option=com_agora&task=topic&id=633)

## Исходный код

*  Универсальный плеер для Windows на движке Awesomium [GitHub](http://github.com/Nex-Otaku/quest-navigator-awesomium)
*  Ветка библиотеки QSP, модифицированная для **Quest Navigator** [GitHub](https://github.com/Nex-Otaku/qsplib-experimental)
*  JS framework (ядро) [GitHub](https://github.com/Nex-Otaku/quest-navigator-core)
*  Библиотечный проект для standalone-приложений Android [GitHub](https://github.com/Nex-Otaku/quest-navigator-library-android)

## Статьи по теме

*  [Файлы игры на Quest Navigator](navigator/navigator_game_files)
*  [Параметры запуска Quest Navigator](navigator/navigator_command_line)
*  [Шаблон игры на Quest Navigator](navigator/navigator_game_template)
*  [Создание игр для плеера Quest Navigator](navigator/sozdanie_igr_na_quest_navigator)
*  [Использование шрифтов в Quest Navigator](navigator/ispolzovanie_shriftov_v_quest_navigator)
*  [Файл настроек игры в Quest Navigator](navigator/fajl_nastroek_igry_v_quest_navigator)
*  [Независимая сборка игры для Quest Navigator](navigator/navigator_standalone)

## Ответы по Quest Navigator в F.A.Q.

* [Пишу несколько игр в Quest Navigator. Как сделать, чтобы у каждой игры было собственное оформление?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/layout_templates)
* [Как подключить свой шрифт к игре?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/add_user_font)
* [Пишу bcolor=rgb(255,200,200), но это не меняет цвет фона игры. Как изменить цвет фона из кода QSP?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/change_background_color)
* [Хочу прописать игре собственный вид курсора, как это сделать?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/change_cursor)
* [Скопировал шаблон оформления в папку со своей игрой, но что с ним теперь делать?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/template_settings)
* [Как узнать, на каком плеере запущена игра: на классическом QSP, или на Quest Navigator?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/proverka_pleera)
* [Как вставить видео в игру на Навигаторе?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/video)
* [Как делать standalone-сборку на Навигаторе?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/standalone)
* [Где в Quest Navigator править размер окна с игрой?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/windows_size)
* [Как выполнить JavaScript прямо из кода QSP?](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/exec_js)
* [Инструкция от Nex\'а, позволяющая сменить оформление из кода игры](https://aleksversus.github.io/howdo_faq/docs/informarch/navigator/change_interface)
