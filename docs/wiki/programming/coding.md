---
sidebar_position: 4
---
[Назад: Выражения](../expressions.md)

# Программный код

Выполнение кода в плеере **QSP** происходит последовательно, команда за командой, сверху вниз и слева направо:

``` qsp
*pl "Первая команда"
*pl "Вторая команда"
*pl "Третья команда"

*pl "Четвёртая команда" & *pl "Пятая команда" & *pl "Шестая команда"
```

## Структура команд

Все команды в **QSP** составляются по общим принципам:

``` qsp
  {оператор} [значение 1], [значение 2], ..., [значение 18]
```

Здесь вместо `{оператор}` может и должен стоять любой оператор **QSP** из тех, что перечислены в разделе ["Ключевые слова. Операторы"](../../hide/keywords_operator.md). Если в команде нет `{оператор}`, значит на самом деле на этом месте подразумевается **неявный оператор**.

``` qsp
! здесь используются явные операторы:
*pl "Ехал Грека Через Реку"
addobj "Рак"
! а здесь имеет место неявный оператор:
137+294
func('pow',3,3)
```

В качестве значений `[значение 1]`, `[значение 2]`, \... ,`[значение 18]` могут выступать строковые или числовые константы, переменные, значения функций, или целые выражения, а число таких значений зависит от назначения оператора. Например, для оператора `*PL` может быть указано лишь одно значение, а для оператора `ADDOBJ` от одного до трёх таких значений. Сами значения перечисляются через запятую.

``` qsp
*pl "Три в кубе это "+func('pow',3,3)+". Да, серьёзно. А ты не верил?"
```

Если необходимо, то для удобства чтения кода значения для операторов можно (но не обязательно) помещать в круглые скобки:

``` qsp
pl("Строка текста")
addobj("Отвёртка","img/screwdriver.png",3)
```

**Внимание!** В одной команде не может быть более одного оператора! Равно так же не может быть команды совсем без оператора. Если в вашей команде нет оператора, то вы имеете дело с `неявным оператором`.

Операция присваивания предполагает, что перед именем переменной стоит оператор `SET`, хотя обычно этот оператор опускают, то есть его тоже можно назвать "неявным":

``` qsp
[имя_переменной] = [значение]
```

Здесь `=` — это операция присваивания. Не путайте с операцией сравнения **равно**.

## Порядок записи команд

Вот несколько правил и рекомендаций для корректного написания кода:

* Каждую отдельную команду нужно записывать в отдельной строке.
* Отступы (пробелы и символы табуляции) перед командой и после неё игнорируются плеером, поэтому вы можете ставить их в нужном количестве для удобства чтения кода:
    ``` qsp
  *p "<table width=240>"
        *p "<tr>"
          *p "<td>Имя:</td>"
          *p "<td>"
            *p $name
          *p "</td>"
        *p "</tr>"
        *p "<tr>"
          *p "<td>возраст:</td>"
          *p "<td>"
            *p age
          *p "</td>"
        *p "</tr>"
      *p "</table>"
    
```

* Пустые строки так же игнорируются плеером, поэтому для лучшей читаемости кода вы можете размещать их между командами:
    ``` qsp
  яблоко = 1
      груша = 1

      *pl 'Яблок' + яблоко
      *pl 'Груш' + груша
    
```

* При необходимости можно написать несколько команд в одну строку. При этом в качестве разделителя команд служит символ "**&**" (не путайте с операцией объединения строк):
    ``` qsp
  яблоко+=1 & *pl "У меня есть <<яблоко>> яблок." & яблоко_взял=1
    
```
 Без необходимости так делать не рекомендуется, поскольку это ухудшает читаемость кода, а так же повышает вероятность допустить [баг](../../hide/bag.md). Подобное перечисление команд уместно в гиперссылках:
    ``` qsp
  *pl '<a href="EXEC: яблоко += 1 & GT $CURLOC">яблоко</a>'
    
```
 В данном случае при нажатии на ссылку выполнится код:
    ``` qsp
  яблоко += 1
      GT $CURLOC
    
```

*  Внутреннюю часть многострочных операторов рекомендуется сдвигать вправо 2-4 пробелами (или одним символом табуляции). Это никак не влияет на выполнение, но делает код более читаемым:
    ``` qsp
  IF яблоки=0 :
        ADDOBJ 'Яблоко'
        яблоки = 1
      END
    
```

*  Крайне редко для повышения читаемости кода приходится разбивать строку на несколько. Такая строка хотя и будет в коде разбита на части, но будет восприниматься плеером, как единая (сообщения об ошибках будут выводится с учётом того, что это одна строка).

```{=html}
<!-- -->
```
    Чтобы следующая строка считалась частью текущей, нужно в конце текущей строки дописать ''** _**'' (пробел и символ подчёркивания):<code qsp>
    if a<5 and n-b>4+5+h/7*2 or t=4: p 'TTTTTTTTT' & cla & $f='Text Variable' & goto 'FFFF'

\</code\> равнозначно 
    ``` qsp
  if a<5 and _
      n-b>4+5+h/7*2 or _
      t=4: p 'TTTTTTTTT' _
    & cla & $f='Text Variable' _
    & goto 'FFFF'

```
 Вместо разбиения строки рекомендуется видоизменить код так, чтобы разбивать строку не требовалось.\
**Обратите внимание.** Сочетание символов `** _**` (пробел и символ подчёркивания) при склеивании строк заменяется на пробел, поэтому такой код:
    ``` qsp
  t _
  or _
  t

```
 будет эквивалентен такому коду:
    ``` qsp
  t or t

```
 Разбивать команду на две строки внутри строковой константы нельзя:
    ``` qsp
  ! на экране мы увидим две строки текста, а не одну:
  *pl "Это строка, которую я хочу разбить _
  на две строки кода, но при выводе видеть одну строку"

```


## Комментарии

Оператор комментария `!` служит для комментирования кода и позволяет оставлять "заметки на полях", которые помогут впоследствии ориентироваться в коде. Всё, что следует за оператором комментария, плеер игнорирует.

Поскольку `!` — это оператор (не путайте с операцией **не равно**), если вы пишете его на одной строке с другими командами, нужно обязательно ставить разделитель `&` (амперсанд) между последней командой и оператором комментария:

``` qsp
! это комментарий в отдельной строке
яблоки = 0 & ! а это комментарий в строке с командой
```

Так как весь текст после оператора комментария будет проигнорирован плеером, комментарий надо ставить всегда самым последним в строке из нескольких команд:

``` qsp
! комментарий. Следующие команды не работают: & *pl "Первая команда" & *pl "вторая команда"
*pl "Эта команда работает" & ! а остальные нет & *pl "вторая команда" & *pl "третья команда"
*pl "Эта команда работает" & *pl "и эта работает" & ! а последняя нет & *pl "третья команда"
*pl "Все три" & *pl " команды" & *pl "работают" & ! а это комментарий
```

Комментарии бывают двух видов: однострочные и многострочные.

* Однострочный комментарий начинается от оператора комментария и заканчивается с концом строки:
    ``` qsp
  ! Однострочный комментарий
      ! и это однострочный комментарий
      яблоки = 0 & ! и это однострочный комментарий
    
```

* Многострочный комментарий так же начинается от оператора комментария и заканчивается с концом строки, однако при использовании кавычек (`" "`), апострофов (`' '`) или фигурных скобок, он может захватывать так же и те строки, что размещены внутри кавычек, апсотрофов или фигурных скобок:
    ``` qsp
  !'Многострочный
      комментарий в апострофах'
      яблоки = 1
      сыр = 5 &  ! А здесь "комментарий начинается
      в той же строке, но" заканчивается 'сильно
      позже'. Во всём виноваты {кавычки и скобки
      }Кстати:
      яблоки=0
      !'Комментарии рекомендуется писать всё-таки
      в отдельных строках, а не как бутерброд с "сыром"'
    
```


## Запись констант

Константами в **QSP** можно назвать конкретные числовые или строковые значения. В следующем примере для операторов вывода текста указаны конкретные значения, это и есть константы:

``` qsp
! вывод на экран числа 137. Можно назвать это число константой.
*pl 137
! вывод на экран строки текста. Эту строку можно назвать константой
*pl "На окошке крошку-мошку ловко ловит лапой кошка"
```

Для записи числовых констант (чисел) используются символы цифр без дополнительных обозначений:

``` qsp
x = 145 & ! 145 здесь - константа
(137+299*2)/11-19 & ! целое выражение из числовых констант
```

Для записи строковых констант (строк) используются символы, отмечающие начало и конец такой строковой константы. Можно использовать кавычки (`" "`), апострофы (`' '`), или фигурные скобки (`{ }`):

``` qsp
*pl "Это строковая константа"
*pl 'И это строковая константа'
*pl {И даже это}
```

Более подробно о правилах записи строк в **QSP** можно почитать в разделе ["Строки"](../strings/index.md).

## Операторы и функции

**Оператор** - ключевое слово (команда) языка **QSP**, выполняющее какое-либо действие. Оператор может иметь параметры (аргументы), которые задаются выражениями. Операторы не возвращают результат выполнения.

Как правило, операторы меняют состояние игры.

Каждая команда **QSP** содержит один оператор и его аргументы (параметры). Если вы написали команду без оператора, то в ней обязательно присутствует **неявный оператор**.

``` qsp
!Примеры вызовов операторов:
ADDOBJ 'ключ','pics/key.png'
ADDOBJ ('ключ','pics/key.png')
PL ('текст')
CLEAR()
```

**Функция** - ключевое слово, которое используется для того, чтобы получить какое-либо значение. Например, сколько предметов игрок несёт в рюкзаке. Для этого, в коде мы указываем функцию, и необходимые для расчёта параметры (аргументы функции). Результат, "посчитанный" этой функцией, подставляется на её место в **выражении**. На языке программистов это звучит так:

    "мы вызвали функцию, и функция вернула нам значение".

Как правило, при вызове функции состояние игры не меняется. Примеры вызовов функций:

``` qsp
maximum = MAX(1, 2, 4)
случайное_число = RAND(4)
предметов_в_рюкзаке = COUNTOBJ 
PL $STR(43)
```

В одной команде может быть вызвано несколько функций:

``` qsp
*pl "Случайный предмет: "+$getobj(rand(1,countobj))
bcolor=rgb(func('hex_in_dec','ff'),func('hex_in_dec','34'),func('hex_in_dec','67'))
```

При использовании функций, возвращающих текстовое значение, настоятельно рекомендуется прописывать перед именем функции символ `$` для улучшения читаемости кода.

Максимальное число аргументов для операторов и функций в **QSP**: 20.

## Базовые функции

*  `$QSPVER` - возвращает версию библиотеки плеера в формате "X.Y.Z Player". Например, классический плеер версии 5.8.0. возвращает значение "5.8.0 (classic)", а qSpider просто "5.8.0". Пример использования:
    ``` qsp
  if $QSPVER<'5.8.0':
        *pl "Ваша версия плеера не подходит для данной игры. Установите плеер версии 5.8.0."
      end
    
```
Так же данная функция может возвращать платформу, на которой запущена игра, если указать аргументом значение "platform":
    ``` qsp
$QSPVER('platform')
```

*  `$CURLOC` - возвращает название текущей локации.

### Математические функции

*  `RAND([#выр1],[#выр2])` - возвращает случайное число между числами \[#выр\] и \[#выр2\]. Параметр \[#выр2\] может отсутствовать, при этом он принимается равным единице (**1**). Примеры:
    ``` qsp
  RAND(1,4) & ! вернёт случайное значение от 1 до 4
      RAND(4,1) & ! вернёт случайное значение от 1 до 4
      RAND(1000) & ! вернёт случайное значение от 1 до 1000
      RAND 1000 & ! вернёт случайное значение от 1 до 1000
    
```

*  `RND` - возвращает случайное значение от 1 до 1000.
*  `MAX([выр1],[выр2], …)` - возвращает максимальное из значений выражений-аргументов. Если передан один аргумент, то считается, что указано имя массива:
    ``` qsp
  MAX(1,2,5,2,0) &! вернёт 5
      MAX(a,b,c) &! вернёт максимальное из значений переменных a,b,c
      MAX('aa','ab','zz') &! вернёт 'zz'
      MAX('a') &! вернёт максимальное из числовых значений элементов массива "a"
      MAX('$b') &! вернёт максимальное из текстовых значений элементов массива "$b"
    
```

*  `MIN([выр1],[выр2], …)` - возвращает минимальное из значений выражений-аргументов. Если передан один аргумент, то считается, что указано имя массива:
    ``` qsp
  MIN(1,2,5,2,0) &! вернёт 0
      MIN(a,b,c) &! вернёт минимальное из значений переменных a,b,c
      MIN('aa','ab','zz') &! вернёт 'aa'
      MIN('a') &! вернёт минимальное из числовых значений элементов массива "a"
      MIN('$b') &! вернёт минимальное из текстовых значений элементов массива "$b"
    
```


[Вперёд: Циклы](../cycle.md)