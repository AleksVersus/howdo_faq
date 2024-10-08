---
sidebar_position: 3
---

# 21.3. Как свернуть кусочек кода, написанный под комментарием?
<!-- [:faq_21_03] -->
**В:** Как свернуть кусочек кода, написанный под комментарием? В идеале, чтоб остался один только комментарий.

Пример:

```qsp
! комментарий, до которого нужно свернуть код
    "Строчка кода"
    "Ещё строчка кода"
    a=b
```

**О:**
К сожалению Quest Generator не учитывает комментарии, когда высчитывает сворачиваемые участки кода, поэтому нельзя свернуть код до комментария. Можно использовать подобный костыль:

```qsp
$args['свернём код до этой переменной'] = $args['свернём код до этой переменной']
    ! комментарий
    "Строчка кода"
    "Ещё строчка кода"
    a=b
$args['свернём код до этой переменной'] = $args['свернём код до этой переменной']

com = com & ! комментарий, до которого сворачиваем блок кода
    ! комментарий
    "Строчка кода"
    "Ещё строчка кода"
    a=b
com = com & ! комментарий, до которого сворачиваем блок кода

local com & ! комментарий, до которого сворачиваем блок кода
    ! комментарий
    "Строчка кода"
    "Ещё строчка кода"
    a=b
local com & ! комментарий, до которого сворачиваем блок кода 
```
