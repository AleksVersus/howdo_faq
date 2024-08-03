# 7.1. Как делать гиперссылки, по нажатию на которые выполняется код?
<!-- [:faq_07_01] -->
В:	Как делать гиперссылки, по нажатию на которые выполняется код?
	Как делать кликабельный текст?
	Как сделать, чтобы по нажатию на текст что-то происходило?

О:

Гиперссылки в QSP делаются точно так же, как и в HTML-документах, то есть с использованием тегов `<a>` и `</a>`.

Например так:
```qsp
*pl "На берёзе созрело несколько <a href=''>яблок</a>."
```
В атрибуте `href`, если говорить об html-документе, обычно пишется url — адресс страницы в интернете. Однако в QSP мы можем разместить внутри этого атрибута строку кода. Например такую:
```qsp
яблоко=яблоко+1 & addobj "Яблоко"
```
Чтобы плеер понял, что в атрибуте `href` находится не url, а какой-то код, мы должны указать перед этим кодом ключевое слово `EXEC`:
```qsp
*pl "На берёзе созрело несколько <a href='exec: '>яблок</a>."
```
Теперь нам нужно вставить после EXEC: нашу строку кода. Однако, мы уже использовали кавычки (`""`) для указания границ строки, и апострофы (`''`) для указания границ атрибута `href`. А в нашей строке кода тоже есть кавычки. Как быть?

Мы можем использовать три различных варианта:

Можно экранировать кавычки кода от QSP с помощью дублирования:
```qsp
*pl "На берёзе созрело несколько <a href='exec:яблоко=яблоко+1 & addobj ""Яблоко""'>яблок</a>."
```
Можно заменить кавычки кода на апострофы, и эти апострофы экранировать от HTML спомощью обратного слэша (данный способ не рекомендуется, так как может не работать в Quest Navigator, qSpider и других более новых версиях плеера):
```qsp
*pl "На берёзе созрело несколько <a href='exec:яблоко=яблоко+1 & addobj \'Яблоко\''>яблок</a>."
```
Либо мы можем заменить апострофы атрибута `href` на кавычки и экранировать эти кавычки от кода QSP:
```qsp
*pl "На берёзе созрело несколько <a href=""exec:яблоко=яблоко+1 & addobj 'Яблоко'"">яблок</a>."
```
Все три способа равнозначны. Используйте тот, что удобнее.