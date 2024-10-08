---
sidebar_position: 2
sidebar_label: Отладчик
---
[Назад: Quest Generator](qgen)

# Отладчик

Здесь вы можете скачать готовый отладчик от **WEREWOLF**, который позволит в любое время выполнить произвольный кусок кода или просмотреть значения переменных из указанного списка:

[Отладчик от **Werewolf**а](https://qsp.org/index.php?option=com_content&id=71&Itemid=56)

Простейший отладчик можно сделать самому. Для этого в самой первой локации игры пишем следующие команды:

```qsp
! включаем отображение строки ввода:
showinput 1
! задаём локацию-обработчик строки ввода:
$usercom = "userCom"
```

Название локации, которую используем в качестве [локации-обработчика строки ввода](../programming/service_locations), может быть любым, но его необходимо обязательно присвоить переменной `$USERCOM`, чтобы игра поняла, какую именно локацию использовать в качестве локации-обработчика строки ввода.

Создаём локацию с именем "`userCom`" (либо с тем именем, что вы указали в `$USERCOM`), где пишем следующее:

```qsp
dynamic $user_text
```

Вот и всё. Теперь любая команда, введённая в строку ввода, будет выполнена, как обычный код.

Например, если вам потребуется получить значение переменной, вы просто вводите название этой переменной в строку ввода и нажимаете "`Enter`".

Если необходимо срочно попасть на другую локацию во время теста игры, просто вводите в строку ввода `goto "название_локации_на_которую_хотите_попасть"` и нажимаете "`Enter`".

[Вперёд: Пишем игры в текстовом редакторе. TXT2GAM](txt2gam)
