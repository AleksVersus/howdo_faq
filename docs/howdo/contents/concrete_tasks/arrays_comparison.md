---
sidebar_position: 8
---

# 20.8. Как в QSP сравнить два массива?
<!-- [:faq_20_08] -->
**В:** Как в QSP сравнить два массива?

**О:**
На первый взгляд вопрос кажется довольно простым, однако сравнение сравнению рознь. И если мы зададим вопрос: как именно мы хотим сравнить два массива? — возникают совершенно разные решения для различных вариантов сравнения.

Мы можем сравнить массивы по числу элементов:

```qsp
if arrsize('mass_1') = arrsize('mass_2'):
    *pl 'Число элементов в массивах одинаковое.'
else
    *pl 'Число элементов в массивах разное.'
end
```

Довольно простая задача.

Возьмём задачу посложнее: проверить массивы на идентичность. То есть значение каждого элемента одного массива должно совпадать со значением элемента другого массива под тем же индексом:

```qsp
loop local i, size = 0, arrsize('mass_1') while i < size and $text = '' step i += 1:
    if mass_1[i] <> mass_2[i]:
        $text = 'Массивы не идентичны'
    end
end
if $text = '': $text = 'Массивы идентичны'
```

Само собой проверять на идентичность массивы разного размера нет смысла.

Третья задача ещё сложнее. Нужно проверить, присутствуют ли в массивах одни и те же значения, но при этом не важно, совпадают ли индексы элементов с этими значениями.

Кажется, что она решается относительно просто:

```qsp
loop local i,size = 0,arrsize('mass_1') while i < size and $text = '' step i += 1:
    if arrpos('mass_2', mass_1[i]) = -1:
        $text = 'Массивы разнятся по содержимому'
    end
end
if $text = '': $text = 'Массивы состоят из одинаковых элементов'
```

Это решение может сработать, если в массивах, например, вот такое содержимое:

```qsp
mass_1[0] = 1 & mass_2[0] = 4
mass_1[1] = 2 & mass_2[1] = 3
mass_1[2] = 3 & mass_2[2] = 2
mass_1[3] = 4 & mass_2[3] = 1
```

Но как быть, если в массивах вот такое содержимое

```qsp
mass_1[0] = 1 & mass_2[0] = 4
mass_1[1] = 1 & mass_2[1] = 4
mass_1[2] = 1 & mass_2[2] = 1
mass_1[3] = 4 & mass_2[3] = 1
```

Да, в них содержатся одинаковые значения, но встречаются они разное количество раз. А если при сравнении нам нужно учесть и количество?

Задача становится чуть более сложной. И теперь её решение будет включать в себя несколько этапов:

1. Сравнение массивов по размеру. Если размеры разные, то массивы в любом случае не равны.
2. Копирование массивов во временные.
3. Сортировка значений во временных массивах
4. Сравнение временных массивов на идентичность

Сортировка значений в массивах — это отдельный вопрос, и он представлен в смежном разделе [**Сортировка данных**](data_sorting.md).

Готовое решение для сравнения массивов на идентичность, на подобие (значения одинаковы но расположены в разном порядке), на совпадение хотя бы одного элемента есть в библиотеке [easy.math.3](https://github.com/AleksVersus/easy.math.3), см. функцию [em.arr.simpl](https://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_simpl).
