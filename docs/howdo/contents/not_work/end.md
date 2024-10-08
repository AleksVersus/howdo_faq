---
sidebar_position: 11
---

# 13.11. Сколько END'ов нужно добавить?
<!-- [:faq_13_11] -->

**В:** Сколько `END`ов нужно добавить?
    
Пишу такой код:
```qsp
if силы>0:
    if энергия>9:
        act "Носить воду с колодца":
        ведро=ведро+2
        энергия=энергия-10
        "Я принёс воды с колодца."
    elseif энергия>3:
        act "Уныло лежать и ждать, когда восстановятся силы":
        энергия=энергия+1
        "Я немного полежал. Голова уже не кружится"
end
END
end
end
end
```
Плеер говорит, что в многострочной форме оператора остуствует `END`. Но сколько бы `END`ов я ни добавлял, ошибка не пропадает.

**О:**

Если понимаешь, зачем нужны `END`ы, то становится проще. `END`ом закрывается многострочная форма оператора.

Так выглядит многострочная форма действия:
```qsp
! ОТКРЫВАЕМ ДЕЙСТВИЕ
act 'действие': 
    ! команда 1
    ! команда 2
    ! ...
    ! команда N
! ЗАКРЫВАЕМ ДЕЙСТВИЕ
end
```
Так может выглядеть многострочная форма условия:
```qsp
! ОТКРЫВАЕМ УСЛОВИЕ
if условие=1:
! если условие 1 сработало
    ! команда 1
    ! команда 2
    ! ...
elseif условие=2: 
! если условия 1 не сработало, но сработало условие 2
    ! команда 15
    ! команда 16
    ! ... 
else
! иначе, если ни одно условие не сработало
    ! команда 49
    ! команда 50
    ! ...
! ЗАКРЫВАЕМ УСЛОВИЕ
end
```

Если действие лежит внутри условия, то и закрываться оно должно внутри условия: 
```qsp
! ОТКРЫВАЕМ УСЛОВИЕ
if условие=1:
! если условие 1 сработало
    ! ОТКРЫВАЕМ ДЕЙСТВИЕ
    act 'действие': 
        ! команда 102
        ! команда 103
        ! ...
    ! ЗАКРЫВАЕМ ДЕЙСТВИЕ
    end
    ! команда 1
    ! команда 2
    ! ...
elseif условие=2: 
! если условия 1 не сработало, но сработало условие 2
    ! команда 15
    ! команда 16
    ! ... 
else
! иначе, если ни одно условие не сработало
    ! команда 49
    ! команда 50
    ! ...
! ЗАКРЫВАЕМ УСЛОВИЕ
end
```
Таким образом исходный пример можно исправить так:
```qsp
! открываем общее условие
if сила>0:
    ! открываем вложенное условие
    if энергия>9:
        ! открываем действие
        act "Носить воду с колодца":
            ведро=ведро+2
            энергия=энергия-10
            "Я принёс воды с колодца."
        ! закрываем действие
        end
    ! если первое условие не сработало
    elseif энергия>3:
        ! открываем действие
        act "Уныло лежать и ждать, когда восстановятся силы":
            энергия=энергия+1
            "Я немного полежал. Голова уже не кружится"
        ! закрываем действие
        end
    ! закрываем вложенное условие
    end
! закрываем общее условие
end
```
