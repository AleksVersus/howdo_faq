---
sidebar_position: 1
---

# 14.1. Как добавить предмет в окно предметов?
<!-- [:faq_14_01] -->

**В:** Как добавить предмет в окно предметов?

**О:**
Всё очень просто. Для этого используется оператор `addobj`. В качестве аргумента оператору передаётся название предмета:

```qsp
addobj "Отвёртка"
```

Если нужно добавить предмет с картинкой, то вторым аргументом указывается путь к файлу картинки.

Например, файл картинки нашего предмета называется "`screw.png`" и лежит в папке "`img`", вложенной в папку с игрой, тогда предмет с картинкой можно добавить так:

```qsp
addobj "Отвёртка","img/screw.png"
```

Ещё картинку можно вставлять прямо в название предмета, используя html. Для этого включаем поддержку html в плеере, прописав, например на самой первой локации в игре, команду:

```qsp
usehtml=1
```

Далее добавляем предмет с картинкой, используя тег `<img>`. В атрибуте `src` этого тега указываем путь к файлу картинки:

```qsp
addobj "<img scr='img/screw.png'> Отвёртка"
```

Обратите внимание. Хотя при этом на экране мы будем видеть картинку и слово "Отвёртка", названием предмета будет вся строка "`<img scr='img/screw.png'> Отвёртка`".
