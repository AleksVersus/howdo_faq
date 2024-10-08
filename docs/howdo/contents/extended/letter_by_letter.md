---
sidebar_position: 3
---

# 19.3. Как сделать так, чтобы текст появлялся на экране постепенно? По буквам?
<!-- [:faq_19_03] -->
**В:** Как сделать так, чтобы текст появлялся на экране постепенно? По буквам?

**О:**
В самом простом виде это можно реализовать через цикл с задержкой:

```qsp
! вносим текст в переменную
$stroka='А можно ли сделать так, чтобы текст появлялся постепенно?'
! выставляем счётчик
i=1
loop local i=1 while i<len($stroka)+1 step i+=1:
! пока значение счётчика не превысило длину строки
    ! задержка 250 мс
    wait 250
    ! выводим следущую букву из нашей строки
    *p $mid($stroka,i,1)
end
```

Однако оператор `wait` "подвешивает" игру на время задержки, в результате чего игрок не может ничего сделать, пока текст не будет выведен полностью. Если нужно вывести текст побуквенно, но при этом сохранить для игрока возможность взаимодействовать с игрой, необходимо использовать локацию-счётчик.

Для начала нужно создать локацию-счётчик (если ещё не создана):
* создаём локацию, название может быть любым, например "реалтайм".
* указываем плееру, какую локацию ему нужно использовать, как локацию-счётчик. Пишем, например, на самой первой локации в игре:
    ```qsp
    $counter="реалтайм"
    ```

На локации-счётчик можно написать вот такой код:

```qsp
if $stroka<>'':
! если в переменной строка есть какое либо значение
    ! выставляем контрольную переменную (она же значение таймера)
    control=50
    ! выставляем период обращения к локации-счётчику
    settimer control
    ! выводим первую букву из оставшейся строки
    *p $mid($stroka,1,1)
    ! если длина строки больше 1
    if len($stroka)>1:
        ! вырезаем из неё все буквы, начиная со второй
        ! и присваиваем той же переменной
        $stroka=$mid($stroka,2)
    else
        ! иначе
        ! выводим перевод строки
        *pl
        ! присваиваем пустое значение
        $stroka=''
    end
elseif control=50:
! иначе если в контрольной переменной стоит значение 50
    ! меняем значение контрольной переменной
    control=500
    ! выставляем период обращения к локации-счётчику
    settimer control
end
```

Теперь, чтобы строка вывелась побуквенно, достаточно присвоить текст переменной `$stroka` на любой локации:

```qsp
$stroka = "А можно ли сделать так, чтобы текст появлялся постепенно, но игрок продолжал взаимодействовать с игрой?" 
```
