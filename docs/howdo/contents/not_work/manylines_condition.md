---
sidebar_position: 9
---

# 13.9. Не работает многострочное условие. Как исправить?
<!-- [:faq_13_09] -->

**В:** Не работает многострочный код. Как исправить?
    
Пишу такой код:
```qsp
if mark_var=1: 'Первый текст.'
    'Второй текст.'
    'Третий текст.'
end
```
Но даже если `mark_var` равно нулю, второй и третий текст всё равно выводятся.

**О:**

Необходимо различать однострочную и многострочную формы записи конструкции условия.

Вот так выглядит однострочная форма:
```qsp
IF [#выражение]: [команды 1]
```
Как видите, за ключевым словом `IF` следует выражение `[#выражение]`, и если это выражение верно, тогда выполняется набор команд `[команды 1]`, который записан после двоеточия в той же строке, что и `IF`. При этом команды перечисляются через амперсанд (`&`).

Код из примера в однострочной форме должен будет выглядеть так:
```qsp
if mark_var=1: 'Первый текст.' & 'Второй текст.' & 'Третий текст.'
```
Однострочную форму записи не требуется закрывать ключевым словом `END`, так как окончанием этой формы считается конец строки с `IF`.

А вот так выглядит многострочная форма записи конструкции условия:
```qsp
IF [#выражение]:
    [команды 1]
END
```
Здесь после двоеточия в той же строке, где находится и ключевое слово `IF`, ничего не пишется. Именно так плеер понимает, что имеет дело с многострочной формой записи. И в этом случае, если выражение `[#выражение]` верно, плеер ищет соответствующие верному условию команды (`[команды 1]`) в следующей строке после двоеточия.

Многострочная форма записи всегда закрывается ключевым словом `END`. Только так плеер может понять, что последующие команды уже не относятся к конструкции условия.

Код из примера в многострочной форме записи должен выглядеть так:
```qsp
if mark_var=1:
    'Первый текст.'
    'Второй текст.'
    'Третий текст.'
end
```
Или так:
```qsp
if mark_var=1:
    'Первый текст.' & 'Второй текст.' & 'Третий текст.'
end
```
Оба варианта являются многострочной формой записи конструкции условия.

Теперь нетрудно догадаться, почему даже когда `mark_var` равно нулю в исходном примере второй и ттретий тексты всё равно выводились.

Плеер встречает конструкцию:
```qsp
if mark_var=1: 'Первый текст.'
```
и, поскольку за двоеточием в той же строке, где находится `IF`, идёт команда `'Первый текст.'`, плеер понимает, что это однострочная форма записи, а значит окончанием конструкции условия можно считать конец строки. Таким образом команды, расположенные в нижеследующих строках, для плеера попросту не относятся к конструкции условия, и он выполняет их в любом случае. `END` при этом игнорируется.
