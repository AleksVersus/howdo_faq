---
sidebar_position: 3
---

# 3.3. Как прикрутить возможность выбора варианта к окну msg?
<!-- [:faq_03_03] -->
**В:** Как прикрутить возможность выбора варианта к окну msg?
**В:** Подскажите аналог команды `confirm` в QSP.

**О:**
В классическом плеере у `msg` нет такой возможности, поскольку `msg` не возвращает значений. Вы можете использовать функцию `$input`, и ограничить для игрока возможные варианты ответов:
```qsp
:loop
! выводим на экран окошко с полем ввода, а результат,
! введёный игроком, возвращаем переменной $answer
$answer = $INPUT ('Хотите продолжить (д/н)?')
! чтобы не учитывать регистр, переводим значение в нижний регистр
$answer=$LCASE($answer)
! проверяем, правильный ли ответ ввёл игрок
IF $answer = 'д':
! если ответ "д" переходим к локации, продолжающей игру
    goto "далее"
ELSEIF $answer = 'н':
! если ответ "н" переходим к локации, прерывающей игру
    goto "конец"
ELSE
! если игрок ввёл неверный ответ, или не ввёл ничего
    ! перепрыгиваем на метку loop
    JUMP 'loop'
END
```

Есть вариант использовать всплывающее меню в качестве диалогового окна, но это не очень хороший вариант, так как всплывающее меню появляется точно под курсором мышки и выглядит совсем не как диалоговое окно. Тем не менее вариант рабочий:

```qsp
# start
*pl "На следующей локации демонстрируется использование меню в качестве даилогового окна для выбора двух вариантов"
$dialog[]="Сообщение: кошелёк или жизнь:dial_loc:?"
$dialog[]="> Кошелёк:dial_loc"
$dialog[]="> Жизнь:dial_loc"
act "Перейти в следующую локацию":
    goto 'room'
end
-- start

# room
refint & ! данная функция принудительно обновит содержимое окон плеера при входе на локацию
:loop
menu '$dialog'
if variant<>1: jump 'loop'
-- room

# dial_loc
if args[0]=1:
    ! данный пункт меню не работает
elseif args[0]=2:
    *pl "Вы выбрали вариант кошелёк"
    variant=1
elseif args[0]=3:
    *pl "Вы выбради вариант жизнь"
    variant=1
end
-- dial_loc
```

В qSpider вы можете написать собственное такое окошко, используя CSS и JavaScript.
