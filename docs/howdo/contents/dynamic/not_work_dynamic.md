---
sidebar_position: 4
---

# 12.4. Почему не работает `dynamic`?
<!-- [:faq_12_04] -->
**В:**    Почему не работает `dynamic`?
    Пишу код в переменной, а потом `dynamic "$var_name"`, но вместо того, чтобы выполнить код, плеер выводит этот код на экран. Почему?

**О:**
Для примера поместим некий код в переменную:
```qsp
$var_name="var_count=25"
```
Теперь попробуем использовать `dynamic`, как в предложенном вопросе:
```qsp
dynamic "$var_name"
```
Что при этом произойдёт?

`dynamic` должен выполнить код, переданный ему в виде строки текста.

Какую строку текста мы ему передаём?
```qsp
"$var_name"
```
Какой код содержится в этой строке?
```qsp
$var_name
```
Что делает этот код?

Выводит на экран содержимое переменной `$var_name`. А какое у этой переменной содержимое?
```qsp
"var_count=25"
```
Эту строку мы и увидим на экране.

Чтобы `dynamic` выполнил код, записанный в переменную, нужно передать ему непосредственно значение переменной:
```qsp
dynamic $var_name
```