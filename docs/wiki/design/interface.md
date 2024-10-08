---
sidebar_position: 4
sidebar_label: Настройки интерфейса
---
[Назад: Графика](graphics)

# Настройки интерфейса

Возможности работы с интерфейсом отличаются для различных версий плееров. В данном разделе будет рассказано об основных возможностях, реализованных в классическом плеере и **qSpider**.

## Функция кодирования цвета

Прежде всего следует ознакомиться с функцией кодирования цвета `RGB`, поскольку именно она используется при работе с переменными, задающими основные цвета интерфейса.

* `RGB` — возвращает числовой код цвета на основе четырёх числовых аргументов, каждый из которых соответствует составляющей требуемого цвета и составляющей прозрачности. Общая запись:
    ```qsp
    RGB([#красный],[#зелёный],[#синий],[#альфа])
    ```
    , где `[#красный]`,`[#зелёный]` и `[#синий]` — числовое выражение трёх составляющих цвета соответственно красной, зелёной и синей; `[#альфа]` — составляющая прозрачности; должны принимать значения от 0 до 255.\
    Данная функция обычно используется совместно с системными переменными `BCOLOR`, `FCOLOR`, `LCOLOR`. Пример:
    ```qsp
    ! гиперссылки светло-жёлтого цвета
    lcolor = rgb(255,255,100)
    ! фон тёмно-серого цвета
    bcolor = rgb(25,25,25)
    ! текст светло-зелёного цвета
    fcolor = rgb(100,255,100)
    ```
    Пример полупрозрачного цвета ссылок:
    ```qsp
    lcolor = rgb(0,255,255,128)
    ```
    Прозрачность (альфа-канал) может не работать в классическом плеере.

## Общие настройки отображения текста

Для того, чтобы задавать общие настройки отображения текста в QSP используется ряд системных переменных.

### Переменные, задающие цвета

* `BCOLOR` — содержит цвет текущего фона. Если равна 0, то используется цвет, заданный в настройках программы. Примеры:
    ```qsp
    ! чёрный цвет фона
    bcolor=-16777216
    ! красный цвет фона
    bcolor=-16776961
    ! белый цвет фона
    bcolor=-1
    ```
    Поскольку цвет фона кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `RGB`, которой в качестве аргументов передаются три составляющие цвета:
    ```qsp
    ! задаём цвет фона через функцию rgb(red,green,blue)
    ! фон синего цвета
    bcolor=rgb(0,0,255)
    ! фон жёлтого цвета
    bcolor=rgb(255,255,0)
    ! фон оранжевого цвета
    bcolor=rgb(255,130,0)
    ! фон голубого цвета
    bcolor=rgb(0,255,255)
    ! фон малинового цвета
    bcolor=rgb(255,0,255)
    ```

* `FCOLOR` —  содержит цвет используемого в данный момент шрифта. Если равна 0, то используется цвет, заданный в настройках программы. Изменение значения переменной меняет цвет всего текста игры, кроме гиперссылок и текста, цвет которого переназначен через HTML. Пример:
    ```qsp
    ! чёрный цвет текста
    fcolor=-16777216
    ! красный цвет текста
    fcolor=-16776961
    ! белый цвет текста
    fcolor=-1
    ```
    Поскольку цвет шрифта кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `RGB`, которой в качестве аргументов передаются три составляющие цвета:
    ```qsp
    ! задаём цвет текста через функцию rgb(red,green,blue)
    ! текст чёрного цвета
    fcolor=rgb(0,0,0)
    ! текст белого цвета
    fcolor=rgb(255,255,255)
    ! текст красного цвета
    fcolor=rgb(255,0,0)
    ! текст зелёного цвета
    fcolor=rgb(0,255,0)
    ```

* `LCOLOR` — содержит текущий цвет шрифта гиперссылок. Если равна 0, то используется цвет, заданный в настройках программы. Изменение значения переменной меняет цвет текста всех гиперссылок, кроме тех, цвет которых переназначен через HTML. Пример:
    ```qsp
    ! чёрный цвет гиперссылок
    lcolor=-16777216
    ! красный цвет гиперссылок
    lcolor=-16776961
    ! белый цвет гиперссылок
    lcolor=-1
    ```
    Поскольку цвет в QSP кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `RGB`, которой в качестве аргументов передаются три составляющие цвета:
    ```qsp
    ! задаём цвет  гиперссылок через функцию rgb(red,green,blue)
    !  гиперссылки синего цвета
    lcolor=rgb(0,0,255)
    ! гиперссылки жёлтого цвета
    lcolor=rgb(255,255,0)
    ! гиперссылки оранжевого цвета
    lcolor=rgb(255,130,0)
    ! гиперссылки голубого цвета
    lcolor=rgb(0,255,255)
    ! гиперссылки малинового цвета
    lcolor=rgb(255,0,255)
    ```

### Переменные, задающие шрифт

* `FSIZE` —  содержит размер используемого в данный момент шрифта. Если равна **0**, то используется размер, заданный в настройках программы. Относительно данного значения в HTML-режиме вычисляются размеры шрифтов тега `<font>`. Пример:
    ```qsp
    fsize=18
    ```
    Размер шрифта устанавливается для всего текста в игре, кроме текста, размер которого переназначен через HTML.

* `$FNAME` — содержит название используемого в данный момент шрифта во всей игре. Если равна `""` (пустая строка), то используется шрифт, заданный в настройках программы. Пример:
    ```qsp
    ! устанавливаем для всей игры шрифт Courier New
    $fname = "Courier New"
    ```

## Настройки отображения окон

* `SHOWSTAT [#выражение]` - если значение выражения отлично от 0, то показывает **Окно дополнительного описания**, иначе скрывает его. Пример:
    ```qsp
    showstat 0 & ! скрываем окно дополнительного описания
    showstat 1 & ! окно дополнительного описания снова отображается
    ```
    Для удобства чтения кода можно заранее определить переменные `on` и `off` с соответствующими значениями:
    ```qsp
    on, off = 1, 0
    showstat on & ! включаем окно дополнительного описания
    showstat off & ! выключаем окно дополнительного описания
    ```

* `SHOWACTS [#выражение]` - если значение выражения отлично от 0, то показывает **Список действий**, иначе скрывает его.\
    Пример:
    ```qsp
    showacts 0 & ! скрываем Окно действий
    showacts 1 & ! выводим Окно действий на экран
    ```
    Для удобства чтения кода можно заранее определить переменные `on` и `off` с соответствующими значениями:
    ```qsp
    on, off = 1, 0
    showacts on & ! включаем окно дополнительного описания
    showacts off & ! выключаем окно дополнительного описания
    ```

* `SHOWOBJS [#выражение]` - если значение выражения отлично от 0, то показывает **Список предметов**, иначе скрывает его.\
    Пример:
    ```qsp
    showobjs 0 & ! скрываем Окно предметов
    showobjs 1 & ! выводим Окно предметов на экран
    ```
    Для удобства чтения кода можно заранее определить переменные `on` и `off` с соответствующими значениями:
    ```qsp
    on, off = 1, 0
    showobjs on & ! включаем окно дополнительного описания
    showobjs off & ! выключаем окно дополнительного описания
    ```

* `SHOWINPUT` — управляет отображением строки ввода на экране. Общая запись:
    ```qsp
    SHOWINPUT [#выражение]
    ```
    , где `[#выражение]` — это число. Обычно используются значения 0 и 1. Если значение выражения `[#выражение]` отлично от нуля, строка ввода отображается. Если значение выражения `[#выражение]` равно нулю, строка ввода скрыта. Примеры:
    ```qsp
    showinput 1 & ! показывает строку ввода
    showinput 0 & ! скрывает строку ввода
    ```
    Для удобства чтения кода можно заранее определить переменные `on` и `off` и использовать их:
    ```qsp
    on, off = 1, 0
    showinput on & ! показывает строку ввода
    showinput off & ! скрывает строку ввода
    ```

## Обновление настроек интерфейса

* `REFINT` — принудительное обновление интерфейса (в т.ч. смена цветов, шрифтов, назначенных с помощью системных переменных). По умолчанию обновление интерфейса происходит 2 раза в секунду (каждые 500 мс). Также см. оператор [SETTIMER](../programming/service_locations).

[Вперёд: HTML](html)
