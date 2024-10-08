---
sidebar_position: 8
---

# 9.8. Как сделать вывод рандомного изображения?
<!-- [:faq_09_08] -->
**В:** Как сделать вывод рандомного изображения?

**О:**

Если у вас есть несколько изображений, имена которых различаются лишь порядковыми номерами, то вывод одного из них случайным образом довольно прост.

Например, изображения с названиями от "pic_1.jpg" до "pic_10.jpg" лежат в папке с игрой. Вывести на экран случайное можно так:

```qsp
*pl "<img src='pic_<<rand(1,10)>>.jpg'>"
```

Плеер встретит данную команду, и в первую очередь раскроет подвыражение. В подвыражении стоит функция `rand(1,10)`, которая вернёт случайное число от `1` до `10`. Это число будет подставленно вместо подвыражения, и таким образом в атрибуте `src` получится полное название файла изображения. Плееру останется только вывести его на экран.

Если же у вас есть изображения с названиями, которые различаются не только порядковыми номерами, или лежат в разных папках, вывести на экран одно случайное будет ненамного сложнее. Главное предварительно внести все пути изображений в массив:

```qsp
$pic_mass[0] = "фон/солнечный_день.jpg"
$pic_mass[1] = "фон/пасмурный_вечер.png"
$pic_mass[2] = "image/opendoor.jpg"
$pic_mass[3] = "personage/чукча.gif"
$pic_mass[4] = "personage/жена чукчи.gif"
$pic_mass[5] = "arrow.png"
```

Затем уже выбранный случайный элемент массива подставляется в атрибут `src`:

```qsp
*pl "<img src='<<$pic_mass[rand(0,5)]>>'>"
```

Точно так же. Плеер попытается раскрыть подвыражение, в котором находится выражение `$pic_mass[rand(0,5)]` — то есть плееру нужно получить значение некой ячейки массива `$pic_mass`. Номер ячейки определяет функция `rand(0,5)` — то есть случайное число от 0 до 5 (таков номер последней заполненной ячейки массива). Плеер получит значение этой ячейки (а туда записан путь к изображению) и подставит вместо подвыражения. Таким образом в атрибуте `src` будет полный путь к изображению, плееру останется только вывести изображение на экран.
