---
sidebar_position: 2
---

# Локализация классического плеера QSP версии 5.7.0
<!-- [:informarch_localization] -->

> Пишу на QSP полуигровой дипломный проект. Всё круто. Но научрука смущают пункты меню плеера вроде "квест", "игра". Понимаю, что можно поменять названия пунктов в файле языка "`*.mo`", но не понимаю как. По сему вопрос - Существуют ли способы создания своих файлов языка для интерфейса плеера? И если это как-то очевидно и я просмотрел, то заранее извиняюсь smile

Этот вопрос на сайте нигде пока что не освещен, думаю, пора сделать спец. страничку, посвященную исходному коду и локализациям windows-плеера QSP, а также самой `qsp.dll`.

Ответ на вопрос, как модифицировать файлы локализации:

1. Качаем [poedit](https://sourceforge.net/projects/poedit/), устанавливаем.
2. Берем файл с русской локализацией, папка `QSP-плеера/langs/ru/qspgui.mo`
3. Копируем в папку папка `poedit/bin`
4. Заходим в эту папку и запускаем командную строку, в ней пишем
    ```
    msgunfmt qspgui.mo > qspgui.po
    ```
5. Редактируем `qspgui.po` в `poedit`
6. Сохраняем. При сохранении файл `qspgui.mo` сгенерируется автоматически(в настройках "по умолчанию" есть соответствующая галочка)
7. Берем полученный `qspgui.mo` и записываем его в папка `QSP-плеера/langs/ru/qspgui.mo`

Автор заметки: **Nex**.

Тема на форуме: ["Локализация QSP"](https://qsp.org/index.php?option=com_agora&task=topic&id=164&Itemid=57)
