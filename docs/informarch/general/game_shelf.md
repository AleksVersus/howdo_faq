---
sidebar_position: 4
---

# Полка игр
<!-- [:informarch_gameshelf] -->

## Что должно быть реализовано в полке игр
<!-- [:informarch_gameshelf_todo] -->

:::warning[Эта статья устарела]
Новый плеер c полкой игр - [qSpider](https://github.com/QSPFoundation/qspider/releases)
:::

Обсуждали недавно с elmortem, каким бы хотелось видеть Classic-плеер в плане работы с играми. Вот к чему пришли.

В HTMLTads есть "полка игр" - страница, которая появляется при запуске плеера(т.е. не при открытии конкретной игры, а при самостоятельном запуске), на которой содержатся ссылки на игры, открытые когда-либо игроком. Просто и удобно, открыл плеер, тыкнул на название игры, игра запустилась. Не надо даже в меню лезть.

Вот такую "полку игр" хотелось бы видеть в Classic QSP, но этого - мало.

Времена медленного интернета прошли, приложения все теснее интегрируются с Web, поэтому:

Хотелось бы также видеть на "стартовой страничке" также список игр с сайта - Новые, Популярные, и т.д., в т.ч. список обновлений для уже установленных в системе игр, и ссылку на обновление версии плеера, если оно требуется. Возможно, это следует реализовать не отдельными списками, а одним с переключаемыми сортировками.

Возможно, к этому добавится что-то еще - например, ссылки на новости сайта, комментарии к играм или сообщения на форуме.

При такой интерактивной странице "Набор игрока"(напомню, он был введен временно) уже не будет нужен - будет просто инсталлятор плеера, в котором будет "стартовая страница", с которой можно будет загрузить и обновить любую игру одним кликом мышки.

"Набор игрока" будет упразднен, в будущем он заменится "Коллекциями игр", т.е. списками, составленными по какому-то критерию. Например, серия "Боевики", "Фэнтези", "РПГ", "Ужасы". Возможно, это будет реализовано через теги для игр, которые все еще в планах.

Разумеется, весь онлайн-контент нужно будет сделать с возможностью отключения в настройках. Одной галочки, пожалуй, будет достаточно. Само собой, при обновлении страницы он не должен блокировать доступ к списку локально загруженных игр.

### Плюсы:
<!-- [:informarch_gameshelf_pluses] -->

* Игрок всегда в курсе выхода новых игр и обновлений плеера.
* Любую игру, в которую он играл, можно сразу запустить одним кликом.
* Публикация информации с сайта в плеере(новости, сообщения на форуме, комментарии к играм) привлечет дополнительное внимание игрока к сайту.
* Процесс скачивания-запуска игры максимально упростится.
* Обновить игру до последней версии станет очень просто, и не нужно будет следить за обновлениями - плеер сам будет предлагать обновить игру.
* Можно будет примерно оценивать активную аудиторию игроков по статистике запросов со "стартовых страниц".

## Требования к играм для попадания в полку игр на Android-плеере
<!-- [:informarch_gameshelf_needs] -->

Требования, которым должна соответствовать игра, чтобы у игрока была возможность нормально играть в нее через "полку игр".

* Игра должна быть упакована в архив zip.
* Главный(запускаемый) .qsp-файл должен находиться в корне архива, а не во вложенных папках.
* На одном уровне с главным .qsp-файлом не должно находиться других .qsp-файлов
* В архиве не должно быть папок и файлов с русскими буквами в имени.


Автор: **Nex**
26.Сен.10 11:29:12
