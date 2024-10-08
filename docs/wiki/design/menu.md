---
sidebar_position: 1
sidebar_label: Всплывающее меню
---
[Назад: Динамический код](../programming/dynamical)

# Меню

**QSP** позволяет в любом месте игры вызывать всплывающее меню. Такое меню удобно для расширения функционала различных частей игры. Например, (и это самый распространённый случай), всплывающее меню позволяет "привязать" различные стандартные действия к предметам.

Меню можно вызвать в ЛЮБОМ МЕСТЕ игры. Т.е. нет никакого технического запрета, чтобы вызвать меню прямо из кода локации, или из действия, или из кода гиперссылки. Оператор используется один и тот же.

## Оператор MENU

`MENU [$имя_масива]` - вызов "всплывающего" меню из массива с именем `[$имя_массива]`.

Прежде, чем использовать данный оператор, необходимо заполнить массив, на основе содержимого которого будут формироваться пункты меню. Начиная с плеера версии 5.9.0 у нас есть два варианта, как заполнять этот массив.

### Первый вариант заполнения массива меню. Кортежи

Этот вариант можно использовать, начиная с плееров версии 5.9.0. В более старых версиях он не работает.

Здесь каждый пункт меню это кортеж из трёх значений:

```qsp
["название пункта меню", "название локации", "путь к файлу иконки"]
```

* Название пункта меню — это то, что мы увидим на экране, когда меню будет выведено;
* название локации — это название локации-обработчика пункта меню, код которой будет выполняться при щелчке на соответствующем пункте меню;
* путь к файлу иконки — это путь к файлу изображения, которое будет выведено рядом с названием пункта меню. Если путь к файлу иконки не указан или указанный файл недоступен, то пункт меню отобразится без иконки.

Таким образом мы должны заполнить массив кортежей для того, чтоб создать наши пункты меню:

```qsp
%stone[0] = ['Взять камень','takestone']
%stone[1] = ['Кинуть камень','throwstone']
%stone[2] = ['Осмотреть камень','lookstone']
```

Здесь название массива (`%stone`) - это название меню, а кортежи - действия, для которых указаны названия пунктов и названия локаций-обработчиков выбора пунктов меню. При выборе пункта "Взять камень" произойдёт вызов локации с названием "takestone". Аналогично будет происходить с другими пунктами.

Чтобы вывести меню на экран, нужно воспользоваться оператором `MENU`:

```qsp
menu '%stone'
```

Пример создания меню с иконками:

```qsp
! нет иконки
%usr_menu[0] = ['Взять предмет:take_item']
! иконка задана gif-файлом
%usr_menu[1] = ['Положить предмет:put_item:images/put_item.gif']
! иконка задана значением $icon_file
%usr_menu[2] = ['Уничтожить предмет','del_item', $icon_file]
! пункт меню задан 3-мя переменными
%usr_menu[3] = [$name, $location, $icon_file]

menu 'usr_menu' &! покажет меню из 4-х пунктов
```

Меню заканчивается на элементе массива со пустым кортежем, либо с кортежем, в котором отсутствует значение для названия пункта меню или локации-обработчика пункта меню. 

Примеры, когда два последних пункта меню не будут созданы:

```qsp
%usr_menu[0]=['Взять предмет','take_item'] & ! этот пункт мы увидим на экране
$usr_menu[1]=['Осмотреть предмет','look_item'] & ! и этот пункт мы увидим на экране
$usr_menu[2]=[] & ! пустой кортеж, плеер посчитает, что меню кончилось
$usr_menu[3]=['Положить предмет','put_item'] & ! этот пункт мы не увидим
```

```qsp
%usr_menu[0]=['Взять предмет','take_item'] & ! этот пункт мы увидим на экране
$usr_menu[1]=['Осмотреть предмет','look_item'] & ! и этот пункт мы увидим на экране
$usr_menu[2]=['уничтожить предмет', ''] & ! не указана локация-обработчик, пункт не увидим
$usr_menu[3]=['Положить предмет','put_item'] & ! и этот пункт мы не увидим
```

```qsp
%usr_menu[0]=['Взять предмет','take_item'] & ! этот пункт мы увидим на экране
$usr_menu[1]=['Осмотреть предмет','look_item'] & ! и этот пункт мы увидим на экране
$usr_menu[2]=['', 'del_item'] & ! не указано название, пункт не увидим
$usr_menu[3]=['Положить предмет','put_item'] & ! и этот пункт мы не увидим
```

Чтобы вставить разделитель в меню, используйте кортеж со значениями `-` и `-`. Т.е. если нужно поставить разделитель вместо 3-го элемента:

```qsp
%usr_menu[0]=['Взять предмет','take_item']
$usr_menu[1]=['Осмотреть предмет','look_item']
$usr_menu[2]=['-', '-'] & ! разделитель вместо пункта меню
$usr_menu[3]=['Положить предмет','put_item']
```

### Второй вариант заполнения массива меню. Строки

Этот вариант можно использовать, как в плеерах версии 5.9.0, так и в более ранних версиях.

Здесь пункты меню — это строковые значения массива с особым форматом записи:

```qsp
"название пункта меню:название локации:путь к файлу иконки"
```

* Название пункта меню — это то, что мы увидим на экране, когда меню будет выведено;
* название локации — это название локации-обработчика пункта меню, код которой будет выполняться при щелчке на соответствующем пункте меню;
* путь к файлу иконки — это путь к файлу изображения, которое будет выведено рядом с названием пункта меню. Если путь к файлу иконки не указан или указанный файл недоступен, то пункт меню отобразится без иконки.

Таким образом мы должны заполнить массив для того, чтоб создать наши пункты меню:

```qsp
$stone[0]='Взять камень:takestone'
$stone[1]='Кинуть камень:throwstone'
$stone[2]='Осмотреть камень:lookstone'
```

Здесь название массива (`$stone`) - это название меню, а текстовые значения массива - действия, для которых указаны названия пунктов и названия локаций-обработчиков выбора пунктов меню. При выборе пункта "Взять камень" произойдёт вызов локации с названием "takestone". Аналогично будет происходить с другими пунктами.

Чтобы вывести меню на экран, нужно воспользоваться оператором `MENU`:

```qsp
menu '$stone'
```

Поиск символов ":" в пунктах начинается с конца строки, то есть название пункта меню может содержать двоеточия, однако тогда обязательно после названия локации должно стоять двоеточие, даже если вы не используете иконки для пунктов меню.

```qsp
$stone[0]='Камень: взять:takestone:'
$stone[1]='Камень: кинуть:throwstone:'
$stone[2]='Камень: осмотреть:lookstone:'
```

Пример создания меню с иконками:

```qsp
! нет иконки
$usr_menu[0] = 'Взять предмет:take_item'
! иконка задана gif-файлом
$usr_menu[1] = 'Положить предмет:put_item:images/put_item.gif'
! иконка задана значением $icon_file
$usr_menu[2] = 'Осмотреть предмет:look_item:<<$icon_file>>'
! пункт меню задан 3-мя переменными
$usr_menu[3] = '<<$name>>:<<$location>>:<<$file>>'

menu 'usr_menu' &! покажет меню из 4-х пунктов
```

Меню заканчивается на элементе массива со значением `""` (пустая строка). Т.е. если массив меню состоит из элементов `"Взять"`,`"Осмотреть"`,`""`,`"Бросить"`, то 2 последних пункта не будут созданы:

```qsp
$usr_menu[0]='Взять предмет:take_item' & ! этот пункт мы увидим на экране
$usr_menu[1]='Осмотреть предмет:look_item' & ! и этот пункт мы увидим на экране
$usr_menu[2]='' & ! здесь пустое значение, плеер посчитает, что меню кончилось
$usr_menu[3]='Положить предмет:put_item' & ! этот пункт мы не увидим
```

Чтобы вставить разделитель в меню, вместо соответствующего элемента массива напишите `"-:-"`. Т.е. если нужно поставить разделитель вместо 3-го элемента:

```qsp
$usr_menu[0]='Взять предмет:take_item'
$usr_menu[1]='Осмотреть предмет:look_item'
$usr_menu[2]='-:-'
$usr_menu[3]='Положить предмет:put_item'
```

## Примеры вызова меню

Пример вызова меню из гиперсылки:

```qsp
  '<a href="EXEC: menu ''$stone''">Камень</a>'
```

## F.A.Q. по созданию меню

Более подробно о том, как делать меню, можно почитать в соответствующих статьях нашего F.A.Q:

* [Как сделать меню предмета?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/menu_of_item)
* [Как сделать разные меню?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/different_menus)
* [Как сделать меню в ссылках?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/menu_in_hyperlinks)
* [Как передавать локациям-пунктам меню аргументы?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/args_to_menu_item)
* [Как делать контекстное меню?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/context_menu)
* [Как вставлять разделители?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/menu_separator)
* [Как вставлять картинки в меню?](https://aleksversus.github.io/howdo_faq/docs/howdo/contents/menu/image_in_menu)

## Порядок работы оператора MENU

Когда плеер встречает оператор `MENU` в коде, он выводит на экран всплывающее меню, сформированное на основе указанного массива, и прерывает выполнение кода, ожидая действий игрока.

Пока ни один из пунктов меню не выбран, или пока игрок не щёлкнул в области за пределами меню, дальнейший код не выполняется.

Если игрок щёлкнул по одному из пунктов меню, вызывается локация, соответствующая данному пункту меню. Эта локация называется локацией-обработчиком выбранного пункта меню. При этом вызов локации осуществляется так же, как осуществлялся бы при вызове этой локации с помощью оператора `GOSUB`.

После вызова локации продолжается выполнение кода со следующей команды после `MENU`.

Если игрок не выбрал ни одного пункта меню и щёлкнул по области вне меню, просто продолжается выполнение кода со следующей команды после `MENU`.

В локацию-обработчик выбранного пункта меню передаётся один аргумент - позиция выбранного пункта. Этот аргумент можно получить из `ARGS[0]`. Позиции пунктов меню нумеруются с 1.

Так же в локацию обработчик транслируются значения локальных переменных, объявленные до вызова меню с помощью оператора `MENU`. Точно так же, как для `GOSUB`. Пример:

```qsp
# start
i = 99
act 'run':
	local i = 137
	%stone = ['click', 'mp']
	menu '%stone'
end
-

# mp
*pl i
-
```

Если запустить игру с представленным выше кодом и щёлкнуть на действии "run", на экране появится меню с одним пунктом "click". Если игрок щёлкнет по этому пункту, на экране отобразиться значение 137, присвоенное локальной переменной внутри действия. То есть значение локальной переменной, объявленной в действии, будет доступно и в локации-обработчике пункта меню, вызванного из кода этого действия.

[Вперёд: Звук](sound)
