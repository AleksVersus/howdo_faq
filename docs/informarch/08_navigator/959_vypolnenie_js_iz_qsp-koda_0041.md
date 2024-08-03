# 22.10. Как выполнить JavaScript прямо из кода QSP?
<!-- [:faq_22_10] -->

:::danger[**Эта статья устарела!**]
Эта статья устарела. Новый плеер с поддержкой HTML - [qSpider](../../04_qspider_0004).
:::

В: Как выполнить JavaScript прямо из кода QSP?

О:
Для этого в QSP предусмотрен специальный оператор `EXEC`. Например, с помощью JavaScript поменяем цвет фона на бирюзовый:

```qsp
EXEC('JS:document.body.style.backgroundColor="#000041";')
```
В качестве аргумента данному оператору передаётся строка текста. Левая часть — до двоеточия — показывает на тип выполняемой инструкции JS — JavaScript. Правая часть — после двоеточия — непосредственно инструкция на JavaScript, которая присваивает элементу `document.body` соответствующий цвет фона.

Подобным образом можно выполнять и другие инструкции JavaScript прямо из кода QSP, однако следует помнить, что JavaScript выполняется только на уровне оформления и никак не влияет на код и состояния самой игры.