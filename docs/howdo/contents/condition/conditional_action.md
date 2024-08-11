---
sidebar_position: 2
---

# 11.2. Как сделать так, чтобы действие появлялось только при определённом условии?
<!-- [:faq_11_02] -->
**В:** Как сделать так, чтобы действие появлялось только при определённом условии?

**О:**
Всё достаточно просто. Необходимо завести отдельную переменную, которая будет определять возможность выполнения действия. Самый простой пример — отслеживаем подъём предмета через переменную-маркер:

```qsp
! открываем условие
if ключ_взял=0:
! если ключ не взят — переменная маркер равна нулю
    ! можно вывести какой-то сопроводительный текст
    *pl "На столе лежит ключ"
    ! добавляем действие
    act "Взять ключ":
    ! код действия
        ! добавить предмет ключ
        addobj "Ключ"
        ! переменной маркер присваиваем значение 1
        ключ_взял=1
        ! перезаходим на локацию
        goto $curloc
    ! закрыли действие
    end
!закрыли условие
end
```

Более сложный пример:

```qsp
if кувшин_полон=0:
! если кувшин пуст
    act "Наполнить кувшин из фонтана":
        кувшин_полон=1
        ! другой код
        goto $curloc
    end
else
! иначе кувшин полон
    act "Вылить воду из кувшина":
        кувшин_полон=0
        ! другой код
        goto $curloc
    end
end
```

Сложный пример с последовательностью действий:

```qsp
if хомяк=0: 
! если хомяка в руках нет
    ! сопроводительный текст
    *pl "На земле сидит хомяк"

    act 'Поднять хомяка': 
    ! начало действия поднять хомяка 
        ! выставляем маркер, чтобы знать, что хомяк в руках 
        хомяк=1 
        ! возвращаемся на текущую локацию 
        goto $curloc 
    ! конец действия поднять хомяка 
    end 
elseif хомяк=1: 
! в противном случае, если хомяк в руках 
    ! выводим сопроводительный текст в основное описание 
    *pl 'Вы взяли хомяка на руки, но он стал отчаянно вырываться.' 
    act 'Отпустить хомяка': 
    ! начало действия отпустить хомяка 
        ! выставляем маркер, чтобы знать, что хомяк отпущен 
        хомяк=2 
        ! возвращаемся на текущую локацию 
        goto $curloc 
    ! конец действия отпустить хомяка 
    end 
elseif хомяк=2: 
! в противном случае, если хомяк убежал
    ! выводим сопроводительный текст в основное описание 
    *pl 'Вы отпустили хомяка, и он тут же исчез в кустах.'  
    act 'Догнать хомяка': 
    ! начало действия догнать хомяка 
        ! выставляем маркер, чтобы знать, что хомяк полетел
        хомяк=3 
        ! возвращаемся на текущую локацию 
        goto $curloc 
    ! конец действия поднять хомяка 
    end
elseif хомяк=3:
! в противном случае, если хомяк улетел
    ! выводим сопроводительный текст в основное описание 
    *pl 'Вы догнали хомяка и отвесили ему пендель. Хомяк расправил крылья и полетел.' 
! конец многострочной конструкции условия 
end
```

Иногда можно обойтись без переменной-маркера. Например, в случае, если вам нужно проверить наличие предмета в инвентаре:

```qsp
if (obj "Пустой кувшин"):
    act "Наполнить кувшин":
        delobj "Пустой кувшин"
        addobj "Полный кувшин"
        goto $curloc
    end
elseif (obj "Полный кувшин"):
    act "Опустошить кувшин":
        addobj "Пустой кувшин"
        delobj "Полный кувшин"
        goto $curloc
    end
end
```