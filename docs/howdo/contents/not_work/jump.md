---
sidebar_position: 8
---

# 13.8. Не работает оператор `JUMP` — не может найти метку
<!-- [:faq_13_08] -->

**В:** Не работает оператор `JUMP` — не может найти метку.

У меня есть действие
```qsp
act "Прыгнуть":
    jump 'loop'
end
```
и метка "loop", расположенная в той же локации, что и действие, но плеер пишет, что указанная метка не найдена.

**О:**

Дело в том, что оператор `jump` может "прыгать" только по меткам, которые находятся в его области видимости. В данном случае область видимости оператора `jump` будет ограничена кодом действия, а значит "прыгнуть" он сможет только на метку, расположенную внутри действия.

Данный вариант работать не будет:
```qsp
:loop

!... какой-то код...

act "Прыгнуть":
    jump 'loop'
end
```
А вот этот сработает:
```qsp
act "Прыгнуть":
    :loop

    !... какой-то код...

    jump 'loop'
end
```
Сработает и этот вариант, поскольку код действия является частью кода локации, а значит входит в область видимости оператора `jump` (но действие при этом на экране не появится):
```qsp
jump 'loop'
act "Прыгнуть":
    :loop
    !... какой-то код...
end
```
Аналогичным образом нельзя "выпрыгнуть" из кода гиперссылки и из кода, переданного оператору `dynamic` или фyнкции `dyneval`.
