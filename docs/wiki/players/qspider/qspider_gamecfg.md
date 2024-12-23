---
sidebar_position: 2
sidebar_label: Конфигурационный файл
---
[Назад: qSpider - основная информация](index)

# Конфигурационный файл

Конфигурационный файл "`game.cfg`" определяет поведение плеера во время запуска той или иной игры.

Данный файл нужно размещать рядом с файлом "`.qsp`" запускаемой игры.

* Если игра упакована в архив "`.zip`" или "`.aqsp`", конфигурационный файл должен быть упакован в тот же самый архив рядом с файлом "`.qsp`" самого верхнего уровня.

Для web-версии плеера можно написать один конфигурационный файл для всех игр и разместить его в папке "`game`", при этом конфигурационные файлы, которые находятся рядом с файлами игр, будут иметь приоритет над общим.

**Внимание!** Запускаться в web-версии плеера будет только первая игра, описанная в конфигурационном файле. Поэтому если вы хотите дать игрокам возможность запускать несколько игр, размещённых у вас на сайте, первую запускаемую игру сделайте в виде каталога или launcher'а. В качестве примера смотрите [Хранилище QSP-игр](https://aleksversus.github.io/QSP-storage/).

## Структура конфигурационного файла

Конфигурационный файл (конфиг, конфиг-файл) состоит из секций, каждая из которых описывает одну игру. Таким образом в конфиге должна быть хотя бы одна секция, описывающая игру.

* Для десктопной версии плеера в конфиге указывается только одна секция игры.
* Для стандалон-сборки имеет смысл указывать только одну секцию игры.
* Несколько игр в конфиге нужно указывать, если игры распространяются пакетом (в виде сборника).

### Описание игры

Секция, описывающая игру, начинается с заголовка `[[game]]` и заканчивается там, где начинается следующая секция, описывающая игру, либо заканчивается с концом файла.

Заголовок секции пишется отдельной строкой.

Структура конфиг-файла для трёх игр может выглядеть примерно так:

```toml
[[game]]
id = "7466df3b-4236-4668-b0df-2a70477da67b"
title = "Сказочка на ночь"
description = """описание первой игры"""
file = "skazka/skazka.qsp"

[[game]]
id = "30c8aebe-1690-4e6d-8b42-47c4be381748"
title = "Куртуазная Баллада"
description = """описание второй игры"""
file = "ballad/ballad.zip"

[[game]]
id = "c2cb4b5b-6a1c-482e-bb47-9ef207fb0dcd"
mode = "aero"
title = "Город туманов"
description = """описание третьей игры"""
file = "cityofmists.aqsp"
```

Как видно из приведённого примера, следом за заголовком секции идёт ряд параметров. Сначала записывается название параметра (ключ), затем ставится знак равенства, а после в кавычках (или без них, если это число) указывается значение параметра. Если значение пишется в несколько строк, оно помещается в тройные кавычки.

Для описания игры используются следующие параметры, ключи:

* **id** — уникальный идентификатор игры (используется для сохранений, поэтому технически можно использовать любой набор символов, однако лучше сгенерировать собственный уникальный айди по образцу из примера, воспользовавшись онлайн-генератором [uuidgenerator.net](https://www.uuidgenerator.net);
* **title** — название игры (будет показано в заголовке плеера и на вкладке браузера);
* **description** — необязательное краткое описание игры, аннотация;
* **file** — путь к файлу с игрой относительно файла "game.cfg", или внешняя ссылка (например `file = "https://qspfoundation.github.io/qspider/game/skazka/skazka.qsp"`, для браузерной версии;
* **mode** — если ваша игра написана для AeroQSP, данному параметру назначается значение "aero".
* **themes** — в этом параметре перечисляются кастомные темы оформления. См. [Взаимодействие с интерфейсом](qspider_interface).
* **defaultTheme** — в этом параметре указывается тема, используемая по умолчанию. См. [Взаимодействие с интерфейсом](qspider_interface).
* **save_slots** — в этом параметре указывается доступное игроку для сохранений число слотов

Для десктопной версии плеера все параметры, кроме "id", не обязательны. Тем не менее рекомендуется их проставлять для удобства чтения конфигурационного файла. Для игр, написанных для AeroQSP, параметр "mode" обязателен.

Далее каждая секция игры может содержать подсекции, расширяющие возможности управления плеером и игрой.

### Назначение горячих клавиш `[game.hotkeys]`

Для каждой игры можно назначить собственные комбинации горячих клавиш. Для этого в секции игры прописываем подсекцию с заголовком `[game.hotkeys]`. После заголовка перечисляем клавиши или их сочетания в качестве ключей, а в качестве значений прописываем названия локаций, код которых будет выполнен при нажатии на горячие клавиши. Пример:

```plain
[game.hotkeys]
i = "Инвентарь"
"ctrl+shift+m" = "карта"
"up up down down left right left right b a" = "konami"
```

Для одиночного нажатия клавиш в качестве ключа указывается её обозначение:

```plain
i="Инвентарь"
```

Для того, чтобы указать одновременное нажатие нескольких клавиш, их обозначения перечисляются через "+" (плюс):

```plain
"ctrl+shift+m" = "карта"
```

Для того, чтобы задействовать последовательное нажатие клавиш, их обозначения перечисляются через пробел:

```plain
"up up down down left right left right b a" = "konami"
```

Можно использовать следующие обозначения:

#### Клавиши-модификаторы

* **shift**
* **ctrl**
* **alt**
* **meta** — для поддержки на macOs лучше использовать этот модификатор вместо ctrl

#### Специальные клавиши

* **backspace**
* **tab**
* **enter**
* **capslock**
* **esc**
* **space**
* **pageup**
* **pagedown**
* **end**
* **home**
* **left**
* **up**
* **right**
* **down**
* **ins**
* **del**
* **plus**
* **f1** - **f19**

Остальные клавиши можно определять просто по символу `a`, `$`, `*`, или `=`.

### Подключение дополнительных ресурсов `[game.resources]`

Есть возможность подключить к каждой отдельной игре дополнительные ресурсы. Например, собственные css-файлы, скрипты, шрифты и т.д. Для этого в секции игры нужно создать подсекцию с заголовком `[game.resources]`. Пример:

```plain
[game.resources]
styles = [
  "https://fonts.googleapis.com/css?family=Sofia",
  "styles.css"
]
scripts = [
  "script.js"
]
fonts = [
  ["Shelter", "fonts/shelter.woff2"]
]
icon = "icon.png"
```

#### CSS

Для подключения css-файлов используем ключ "`styles`", значением которого выступает список ссылок на необходимые нам файлы css. Это могут быть как внешние ссылки, так и пути относительно файла "`game.cfg`".

Список обязательно помещается в квадратные скобки! Его элементы разделяются запятыми. Отступы между элементами и скобками ни на что не влияют. За последним значением списка нельзя ставить запятую. Пример:

```plain
styles = ["skins/game.css","lewis.css"]
```

К основным элементам интерфейса добавлен атрибут `data-qsp` (например, `data-qsp="main"`, `data-qsp="actions"` и т.д.), который позволит вам стилизовать данные элементы, или взаимодействовать с ними через скрипты.

#### JavaScript

Для подключения JavaScript используется ключ "`scripts`". Его значением так же выступает список ссылок на нужные скрипты. Поскольку нет возможности автоматически удалить JS код из памяти (при переключении на другую игру, например) — это надо делать вручную. Подробнее об этом можно почитать в [статье Werewolf-а, посвящённой выходу qSpider 0.10.0](https://ifhub.club/2021/05/23/qspider-0100.html).

**Пример подключения скриптов:**

```plain
scripts=["skins/js/game.js","skins/js/QspLibBrowserTest.js"]
```

#### fonts

Ключ "`fonts`" предназначен для подключения шрифтов к игре. Его значением является список, элементами которого являются другие списки — каждый такой отвечает за подключение одного шрифта. Пример подключения:

```plain
fonts=[
  ["GoodVibesPro","skins/fonts/good-vibes-pro.woff2"],
  ["AstronBold","skins/fonts/astron-bold.woff2"]
]
```

Как видите, в данном примере подключаются два шрифта. Здесь "`GoodVibesPro`" и "`AstronBold`" — это имена шрифтов, которые вы можете использовать при стилизации текста в вашей игре. Вы можете сами назначать эти имена. Вторым элементом для каждого из шрифтов указывается путь к конкретному файлу шрифта. Рекомендуемый формат — `woff2`, он поддерживается всеми современными браузерами. В сети полно онлайн конверторов из `ttf` в `woff2`.

Если у шрифта есть **Bold**, *Italic* и ***BoldItalic*** варианты в отдельных файлах, то подключение может выглядеть так:

```plain
fonts = [
  ["Shelter", "fonts/shelter.woff2"],
  ["Shelter", "fonts/shelter-bold.woff2", "bold"],
  ["Shelter", "fonts/shelter-italic.woff2", "normal", "italic"],
  ["Shelter", "fonts/shelter-bold-italic.woff2", "bold", "italic"]
]
```

#### FavIcon

Параметр "`icon`" дает возможность заменить иконку во вкладке браузера, так называемый "favicon". По умолчанию там находится логотип QSP. Пример использования:

```plain
icon="skins/gfx/doctor.png"
```

### Поддержка игр AeroQSP \[game.aero\]

Для того, чтобы запускать AeroQSP-игру, нужно в секции игры выставить параметр "`mode`":

```plain
mode="aero"
```

Так же, если используется размер игры, отличающийся от дефолтного 800х600, необходимо добавить секцию `[game.aero]` с размерами:

```plain
[game.aero]
width = 504
height = 680
```

Смотрите так же раздел ["Особенности работы игр AeroQSP на qSpider"](qspider_aeroqsp)

### Настройка окна desktop-плеера \[game.window\]

Вы можете настраивать окно плеера в десктопной версии. Для этого в основной секции игры нужно объявить подсекцию с заголовком `[game.window]`, и проставить необходимые параметры:

```plain
[game.window]
width = 1280
height = 960
resizable = true
minWidth = 1024
minHeight = 768
```

* **width** и **height** задают размер окна при старте игры;
* **minWidth** и **minHeight** дают возможность задать минимально возможные размеры, если игрок попытается изменить размеры окна;
* **resizable** — позволяет запретить изменения размера в принципе (автоматически включается в aero-режиме).

## Пример файла "game.cfg" для отдельной игры

```plain
[[game]]
id = "50458ae2-c07d-ca43-4a81-7bf480eedcf6"
title = "Вереница миров, или Выводы из закона Мёрфи"
description = """В Лаборатории Мерфи опять неприятности. Похищен опытный образец бета-аннигилятора, и похититель скрылся в Веренице Миров - сложной системе межпространственных порталов. Кому предстоит расхлёбывать это дельце? Ну конечно же вам, майор!"""
file = "merphy_law.qn.qsp"

[game.hotkeys]
b = "back.varriors"
"ctrl+shift+m"="карта"
"up up down down left right left right" = "konami"

[game.resources]
styles = ["skins/qspidergame.css"]
fonts=[
  ["GoodVibesPro","skins/fonts/good-vibes-pro.woff2"],
  ["AstronBold","skins/fonts/astron-bold.woff2"]
]
icon="skins/gfx/doctor.png"

[game.window]
width = 1280
height = 720
resizable = true
minWidth = 848
minHeight = 480
```

## Другие статьи по qSpider

* [qSpider — общая информация](index)
* [Особенности запуска и работы игр AeroQSP на qSpider](qspider_aeroqsp)
* [Взаимодействие с интерфейсом](qspider_interface)
* [Темы оформления](qspider_themes)
* [Специальные теги](qspider_spectags)
* [Встроенная библиотека](qspider_inclib)
* [Стандалон-сборка игры на qSpider](qspider_standalone)
