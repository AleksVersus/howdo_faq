---
sidebar_position: 9
---

# 14.9. Как снять выделение предмета?
<!-- [:faq_14_09] -->

**В:** Как снять выделение предмета?
**В:** Как сделать, чтобы выбранный предмет можно было кликнуть ещё раз?

**О:**
Выделение с предмета снимается с помощью команды `unselect`. Обычно её прописывают в конце локации-обработчика выделения предмета:

```qsp
unselect
```

Однако эта команда не успеет выполниться, если при щелчке по предмету происходит переход с помощью оператора `goto`/`xgoto`. В этом случае можно воспользоваться таким решением:

```qsp
! запоминаем название выделенного предмета
$object=$selobj
! снимаем выделение
unselect

! далее работаем с сохранённым названием выделенного предмета
if $object="Камень телепортации":
! если был выделен Камень телепортации
    ! переходим на локацию Эверест
    goto "Эверест"
end
```
