---
sidebar_position: 3
---

# 8.3. Какой командой можно вывести текст в окно дополнительного описания?
<!-- [:faq_08_03] -->

**В:** Какой командой можно вывести текст в окно дополнительного описания?

**О:**

Для вывода текста в окно дополнительного описания воспользуйтесь одним из трёх операторов:

* `p` — просто выводит текст на экран в окне дополнительного описания
* `pl` — выводит текст на экран в окне дополнительного описания, а после переводит каретку на новую строку. Т.е. любой другой добавленный в окно дополнительного описания текст обязательно будет выведен с новой строки.
* `nl` — сначала переводит каретку на новую строку, затем выводит текст в окне дополнительного описания.

Примеры:

```qsp
p "Кусочек текста"
pl "Строка текста, а затем переход на новую строку"
nl "Сначала переход на новую строку, а затем строка текста"
```