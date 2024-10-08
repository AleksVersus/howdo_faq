---
sidebar_position: 7
sidebar_label: Строки
---
[Назад: Массивы](../arrays)

# Строки

В **QSP** есть три типа данных: числовой, строковый и кортежи. В данном разделе мы рассмотрим строковый тип данных и способы работы с ним.

Если мы присваиваем строковое значение переменной, перед именем такой переменной обязательно нужно ставить символ `$`. То же самое, если мы *извлекаем* строковое значение из переменной.

```qsp
$text = "Зелёное яблоко" &! помещаем строковое значение в переменную
*pl $text &! выводим на экран значение строковой переменной
```

Также рекомендуется к названиям всех функций, возвращающих строковые значения, приписывать символ `$` для улучшения читаемости кода.

```qsp
$max('Петя','Вася','Лёша','Дима')
$text = $str(453+111)
$name = $input('Введите имя:')
```

## Константы

Под константой следует понимать одно конкретное значение. Например, число `1441` — это числовая константа, а строка `"Зелёные яблоки"` — это строковая константа.

Если с числовыми константами в **QSP** всё просто (записываем число, используя набор цифр; например, `4953`), то со строковыми есть несколько нюансов:

*  Строковая константа берётся с двух сторон в кавычки (обрамляется кавычками).
    *  Кавычки могут быть двух видов: апострофы `' '` и прямые кавычки `" "`.
    *  Если нужно в константу включить кавычки того же вида, нужно написать их два раза подряд (*экранировать через дублирование*):
        ```qsp
        *PL 'Byte Soft''s "QSP"'
        *PL "Byte Soft's ""QSP"""
        !Byte Soft's "QSP"
        ```
*  В строковых константах сохраняются переносы строк и отступы:
    ```qsp
    'Данный текст
    будет расположен на
    нескольких строках'

    $a='И этот
      текст    
    также'

    a=2 & act 'Многострочное
    название':gt 'next'
    ```
*  Если ошибка допущена внутри строковой константы, то вся многострочная константа будет считаться одной строкой при выводе ошибки.
    ```qsp
    ! ошибка указывается во второй строке
    *pl "Хотя на самом
    деле ошибка
    в четвёртой <<"строке">>"
    ```
*  Текстовые константы и значения переменных можно объединять двумя способами:
    *  С помощью оператора конкатенации `&`. Выражение нужно брать в скобки, т.к. существует ещё разделитель команд `&`:
        ```qsp
        ! В переменную $res запишется 'x=5 y=6':
        $res = ('x=' & x & ' y=' & y)

        ! В переменную $res запишется  'x=',
        ! а '5' выведется в основное окно описания:
        $res = 'x=' & x
        ```
    *  С помощью оператора сложения `+`: 
        ```qsp
        ! Результат 'x=5 y=6':
        $res = 'x=' + x + ' y=' + y
        ```
        *  Следует соблюдать осторожность, если одно из слагаемых числового типа: 
            ```qsp
            x = 1
            $res = '1' + x
            !Результат '2' вместо '11'
            ```

### Экранирование

Чуть выше были приведены два случая экранирования кавычек в строке. Экранирование становится особенно важным, когда мы имеем дело с более сложным вложением кавычек. Например, при работе с HTML-разметкой.

Для более полного понимания того, как можно экранировать кавычки в **QSP**, рассмотрим гиперссылку, в которую встроен переход на локацию. Вот как эта ссылка будет выглядеть на экране при отключенном режиме распознавания HTML:

```html
<a href="EXEC: goto 'Верстак' " class="plain">Верстак</a>
```

Если мы заключим нашу ссылку в одинарные кавычки, нам придётся экранировать одинарные кавычки внутри атрибута **href**:

```qsp
*p '<a href="EXEC: goto ''Верстак'' " class="plain">Верстак</a>'
```

Если мы заключим нашу ссылку в двойные кавычки, то нам придётся экранировать непосредственно границы атрибутов от кода **QSP**:

```qsp
*p "<a href=""EXEC: goto 'Верстак' "" class=""plain"">Верстак</a>"
```

Есть способ записи, когда нам не приходится экарнировать кавычки вообще. Мы просто заключаем ссылку в фигурные скобки (не рекомендуется):

```qsp
*p {<a href="EXEC: goto 'Верстак' " class="plain">Верстак</a>}
```

Может так же пригодиться способ, позволяющий создавать глубокие уровни вложенности кавычек друг в друга и обходиться без экранирования:

```qsp
*p '<a href="EXEC:' + " goto 'Верстак' " + ' " class="plain">Верстак</a>'
```

## Сравнение строк

Точно так же, как и числовые значения, мы можем сравнивать строковые значения. При этом операции сравнения будут возвращать **1**, если равенство верно, и **0**, если равенство неверно.

```qsp
if 'abc'='abc': 'Условие выполнено'
*pl ('abc'='abc') & ! увидим на экране единицу
*pl ('abc'>'ab') & ! увидим на экране единицу
*pl ('abc'<'abc') & ! увидим на экране ноль
```

Строки сравниваются посимвольно, начиная с крайнего левого символа.

```qsp
! это не валидный код qsp
! а табличка сравнения строковых констант
'ac' = 'ac'
'bc' > 'ac'  &! 'b' > 'a'
'ac' > 'ab'  &! 'c' > 'b'
'b'  > 'ab'  &! 'b' > 'a'
'ab' > 'a'   &! 'b' > ''
```

## Подвыражения

**QSP** позволяет вставлять значения различных выражений в строковые константы, а так же в базовые описания локаций и названия базовых действий. Для этого используются специальные конструкции из двойных угловых скобок: `<<` и `>>`. Выражения, помещённые в такие двойные угловые скобки, называются **подвыражениями**, или **вложенными выражениями**.

Примеры:

```qsp
число_гоблинов=5
'Тебя окружили <<число_гоблинов>> гоблинов!'
! на экране будет строка:
! Тебя окружили 5 гоблинов!
```

```qsp
pl 'Вас зовут <<$playerName>>, вы находитесь в <<$curloc>>.'
```

Когда плеер встречает подобное подвыражение, он это подвыражение **раскрывает**. Это значит, что плеер вычисляет значение выражения в двойных угловых скобках, а затем подставляет полученное значение на место этого самого подвыражения.

Другие примеры:

```qsp
pl 'i='+$str(i)
!эквивалентно
pl 'i=<<i>>'
```

Подвыражения можно вкладывать друг в друга. Здесь очень важно соблюдать чередование кавычек, если вы это делаете:

```qsp
!Вложенные подвыражения:
pl val('<<val("<<i>>")>><<j>>')
pl val('<<$str(val("<<i>>"))>>')
! Здесь в подвыражения вкладываются другие
! строковые константы с подвыражениями
```

Если нужно последовательность `<<` вывести на экран, или поместить в переменную, можно воспользоваться одним из этих способов:

*  Разбить `<<` на `'<'+'<`\':
    ```qsp
    $text = '<'+'<var>>'
    'string <'+'<var>>'
    ```
* Использовать фигурные скобки:
    ```qsp
    $text={<<var>>}
    *pl {string <<var>>}
    ```

**Фигурные скобки** — это ещё один способ создавать строковые константы. При их использовании создаются точно такие же строковые константы, как и в случае с обычными кавычками, однако в таких константах не раскрываются подвыражения. К тому же текст, размещённый в фигурных скобках не подсвечивается непосредственно как текст различными редакторами (например, Quest Generator), а подсвечивается как обычный код. Поэтому фигурные скобки обычно используют для создания [динамического кода](../dynamical).

```qsp
*pl {
    Это текст в фигурных скобках,
    здесь не раскрываются <<подвыражения>>
}
dynamic {
    ! обычно в фигурных
    ! скобках размещают
    *pl "Код для оператора DYNAMIC"
}
```

## Функции

*  `LEN([$стр])` - возвращает длину строки `[$стр]`.
    ```qsp
    *pl len('Зелёные яблоки') &! на экране будет число 14
    ```

*  `$MID([$стр],[#начало],[#длина])` - вырезает из строки `[$стр]` строку, которая начинается с символа номер `[#начало]` и имеет длину `[#длина]`. Нумерация символов в строке ведётся с **1**.
    * Параметр `[#длина]` может отсутствовать, при этом вырезается вся строка, начиная с символа `[#начало]`.
    * Если `[#начало]` превышает длину строки, функция возвращает пустую строку.
    *  Примеры:
        ```qsp
        $MID('abcd', 1, 2) &! 'ab'
        $MID('abcd', 2, 3) &! 'bcd'
        $MID('abcd', 2)    &! 'bcd'
        $mid('abcd',5) &! '' (пустая строка)
        ```

*  `$UCASE([$стр])` - возвращает строку больших букв, полученную изменением регистра букв исходной строки `[$стр]`.
    ```qsp
    $UCASE('TexT#') &! 'TEXT#'
    ```

*  `$LCASE([$стр])` - возвращает строку маленьких букв, полученную изменением регистра букв исходной строки `[$стр]`.
    ```qsp
    $LCASE('TExT#') &! 'text#'
    ```

*  `$TRIM([$стр])` - удаляет прилегающие пробелы и символы табуляции из `[$стр]` и возвращает полученную строку. 
    ```qsp
    $TRIM(' TRIM TEST ') &! 'TRIM TEST'
    ```

*  `$REPLACE([$стр],[$поиск],[$замена])` - заменяет в строке `[$стр]` все вхождения строки `[$поиск]` строкой `[$замена]`.
    *  Параметр `[$замена]` может отсутствовать и принимается равным пустой строке.
    *  Примеры:
        ```qsp
        $REPLACE('test', '12', '4') &! 'test'
        $REPLACE('test', 'e', 's')  &! 'tsst'
        $REPLACE('test', 't', '34') &! '34es34'
        $REPLACE('test', 't')       &! 'es'
        ```

*  `INSTR([$строка],[$поиск],[#начало])` - возвращает номер позиции символа, с которого начинается вхождение строки `[$поиск]` в строку `[$строка]` (или **0**, если вхождения нет). Поиск начинается с символа номер `[#начало]`.
    *  Параметр `[#начало]` может отсутствовать, при этом он принимается равным **1**.
    *  Примеры:
    ```qsp
    INSTR('ABCDefgh','BC',1) &! 2
    INSTR('ABCDefgh','Be',1) &! 0
    INSTR('abcdef','abc')    &! 1
    ```

*  `ISNUM([$строка])` - функция проверяет, является ли строка `[$строка]` числом. Функция возвращает `0` (ложь) или `1` (истина). 
    ```qsp
    ISNUM(' 9999 ') &! 1
    ISNUM(' -888')  &! 1
    ISNUM('777a6')  &! 0
    ISNUM('')       &! 0, т.к. пустая строка не содержит числа
    ```

*  `VAL([$стр])` - переводит строку цифр `[$стр]` в соответствующее число. При ошибке возвращает `0`.
    ```qsp
    яблоки = VAL($яблоки)
    val('123') & ! увидим 123
    val('') & ! увидим 0
    val('sand') & ! увидим 0
    ```

*  `$STR([#число])` - переводит число (числовое выражение) в соответствующую строку. 
    ```qsp
    PL $STR(56)
    ```

## Операторы

* `SCANSTR [$имя_массива], [$текст_для_разбора], [$регэксп], [#номер_группы]` — оператор ищет в строке `[$текст_для_разбора]` непересекающиеся фрагменты, соответствующие регулярному выражению `[$регэксп]`, и помещает их в массив `[$имя_массива]`. Если параметр `[#номер_группы]` указан и отличается от нуля, в массив помещается не весь фрагмент целиком, а лишь та его часть, которая соответствует группе с указанным номером.
    * Подробное описание оператора и примеры использования в разделе "[массивы](../arrays)".

[Вперёд: Регулярные выражения](regexp)
