---
sidebar_position: 5
---

# 18.5. В папке с игрой стали появляться файлы с расширением `.tmp`. Что это за файлы, нужны они, и как избавиться от их появления?
<!-- [:faq_18_05] -->
**В:** В папке с игрой стали появляться файлы с расширением `.tmp`. Что это за файлы, нужны они, и как избавиться от их появления?

**О:**
Данные файлы появляются, если в папке с игрой присутствует файл "`qspgui.cfg`", на котором установлен атрибут "только чтение". Это файлы, которые создаются под временные нужды. Чтобы избежать размножения этих файлов, нужно снять атрибут "только чтение" с файла "`qspgui.cfg`".

Так же, есть мнение, что можно избежать появления этих файлов, если установить данный атрибут на всю папку с плеером.
