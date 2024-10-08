---
sidebar_position: 2
---

# 4.2. Как сделать разные меню для двух и более предметов?
<!-- [:faq_04_02] -->
**В:** Как сделать разные меню для двух и более предметов?
**О:**

На каждый предмет, для которого нужно меню, необходимо завести собственный массив.

Например, если у нас есть два предмета "Отвёртка" и "Апельсин":
```qsp
! заводим массив с пунктами меню для отвёртки
$меню_отвёртка[0]="Осмотреть:info_screw"
$меню_отвёртка[1]="Использовать:use_screw"
$меню_отвёртка[2]="Выбросить:put_screw"
! заводим массив с пунктами меню для апельсина
$меню_апельсин[0]="Осмотреть:info_orange"
$меню_апельсин[1]="Использовать:use_orange"
$меню_апельсин[2]="Выбросить:put_orange"
```
Само собой необходимо создать локации для каждого из этих пунктов. И на каждой локации прописать нужный код (см. ["Как сделать меню предмета?"](menu_of_item.md)).

Осталось только прописать вызов меню на локации-обработчике выделения предмета (название которой прописано в `$onobjsel`):
```qsp
if $selobj="Отвёртка":
! если выделен предмет "Отвёртка"
    ! вызываем меню отвёртки
    menu "$меню_отвёртка"
end
if $selobj="Апельсин":
! если выделен предмет "Апельсин"
    ! вызываем меню апельсина
    menu "$меню_апельсин"
end

! ...и так далее по каждому предмету

! не забываем снять выделение с предмета в конце
unselect
```
