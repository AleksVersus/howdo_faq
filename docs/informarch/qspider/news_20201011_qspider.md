---
sidebar_position: 20201011
---

# qSpider - плеер для запуска QSP игр в браузере

[Клуб любителей текстовых игр на QSP·11 окт 2020](https://m.vk.com/@qsplayer-qspider-pleer-dlya-zapuska-qsp-igr-v-brauzere)

Этот проект начался просто как проверка возможности запуска C кода в броузере с помощью WebAssembly.  
Потом было понимание, что в связи со «смертью» Flash, скоро перестанет работать AeroQSP плеер, и было бы неплохо сделать возможность запуска игр сделаных под AeroQSP.  
И вот пришло время его альфа-релиза.

### Страница с релизами

[https://github.com/qspfoundation/qspider/releases](https://m.vk.com/away.php?to=https%3A%2F%2Fgithub.com%2Fqspfoundation%2Fqspider%2Freleases)

Новые релизы будут появляться на ней по мере выхода.

### Демо-игра

[Сказочка на ночь](https://m.vk.com/away.php?to=https%3A%2F%2Fqspfoundation.github.io%2Fqspider%2F)

Поддерживаются только новые версии браузеров (поддержки Internet Explorer нет и не будет).

В плеере используется самая последня версия qsplib библиотеки, которую сейчас активно разрабатывает Байт.

Ее основные отличия от 5.7.0

- операторы работы с модулями переименваны -ADDQST в INCLIB и KILLQST в FREELIB
- в ряде функций (напрмер ARRPOS и ARRCOMP) необязательный параметр перенесен с первого места на третье
- добавлены локальные переменные
- добавлены циклы
- изменена логика работы массивов — если раньше в одном элементе массива могли одновременно находиться и числовое, и строковое значение, то сейчас будет храниться всего лишь одно с признаком типа.

### Отличия qSpider от Классического плеера:

- пути к ресурсам (картинкам/аудио файлам) регистрозависимы — то есть если файл называется 'image.jpg' а в файле игры записано 'Image.jpg' или 'image.JPG' то плеер не сможет показать такую картинку
- для проигрования аудио используются встроенные средства браузера, поэтому рекомендованый формат для плеера — mp3 как самый поддерживаемый (хорошая альтернатива — webm, у него меньше размер при том же качестве, но чуть хуже с поддержкой браузеров)
- есть возможность пропуска wait (кликом по странице)
- сохранения хранятся в браузере

Внешний вид пока не финализирован — критика и предложения по улучшению очень приветствуются.

### Планы на ближайшее будущее:

- загрузка игры из архива и по внешней ссылке
- экспорт/импорт сохранений — для переносов между браузерами
- возможность запуска Aero игр

Запуск плеера на компьютере

Из-за ограничений безопасности плеер нельзя запустить просто открыв index.html файл в браузере.  
Поэтому для запуска необходим локально запущенный сервер — можно использовать один из [списка](https://m.vk.com/away.php?to=https%3A%2F%2Fgist.github.com%2Fwillurd%2F5720255) или же расширение хрома [Web Server for Chrome](https://m.vk.com/away.php?to=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fweb-server-for-chrome%2Fofhbbkphhbklhfoeikjpcbhemlocgigb "https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb").

В дальнейших инструкциях я буду использовать расширение:

- устанавливаем [Web Server for Chrome](https://m.vk.com/away.php?to=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fweb-server-for-chrome%2Fofhbbkphhbklhfoeikjpcbhemlocgigb "https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb")
- скачиваем и распаковываем qspider-player.zip с страницы [релизов](https://m.vk.com/away.php?to=https%3A%2F%2Fgithub.com%2Fqspfoundation%2Fqspider%2Freleases)
- открываем в хроме chrome://apps/ и выбираем в списке Web Server
- в открывшемся попапе выбираем папку, в которую распаковали плеер и запускаем сревер
- там же в попапе будет ссылка

По умолчанию вместе с плеером упакована игра «Сказочка на ночь».

Для запуска другой игры:

- копируем игру в подпапку `game`
- редактируем в той же папке файл `game.cfg`  
    id — уникальный идентификатор игры (используется для сохранений)title — название игры (будет показано в заголовке плеера)folder — путь к папке с игрой относительно папки gamefile — название файла с игрой

**Автор статьи:** Werewolf  
**Оригинал статьи:** [https://ifhub.club/2020/10/11/qspider-pleer-dlya-zapuska-qsp-igr-v-brauzere.html](https://m.vk.com/away.php?to=https%3A%2F%2Fifhub.club%2F2020%2F10%2F11%2Fqspider-pleer-dlya-zapuska-qsp-igr-v-brauzere.html "https://ifhub.club/2020/10/11/qspider-pleer-dlya-zapuska-qsp-igr-v-brauzere.html")
**Обсуждение на форуме:** [http://qsp.su/...topik1291#p2807](https://m.vk.com/away.php?to=http%3A%2F%2Fqsp.su%2Findex.php%3Foption%3Dcom_agora%26task%3Dtopic%26id%3D1291%26Itemid%3D57%23p28071 "http://qsp.su/index.php?option=com_agora&task=topic&id=1291&Itemid=57#p28071")
**Обсуждение в дискорде:** [https://discord.gg/K6JyYVk](https://m.vk.com/away.php?to=https%3A%2F%2Fdiscord.gg%2FK6JyYVk)
