---
sidebar_position: 2
---

# 20.2. Как проверить число на чётность?
<!-- [:faq_20_02] -->
**В:** Как проверить число на чётность?

**О:**

Задача довольно простая. В QSP есть функция, которая позволяет получить остаток от деления любого числа на любое.

Чётные числа делятся на 2 нацело, это значит, что остаток от деления таких чисел на 2 равен 0. Поэтому код проверки чётности можно записать так:
```qsp
if n mod 2 = 0:
! если число делится на 2 без остатка, оно чётное
    "Чётное число"
else
! если число не делится на 2 без остатка, оно нечётное
    "Нечётное число"
end
```
Можно и покороче:
```qsp
$iif((n mod 2) = 0, "Чётное число", "Нечётное число")
```
Таким образом можно проверять делимость любого числа на любое. Например, проверить, делится ли число на 3:
```qsp
$iif((m mod 3) = 0, "Делимое на 3", "Неделимое на 3")
```
