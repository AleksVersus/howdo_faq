---
sidebar_position: 3
---

# 2.3. Как сделать, чтобы через пару секунд после входа на локацию появлялось новое действие?
<!-- [:faq_02_03] -->

**В:** Как сделать, чтобы через пару секунд после входа на локацию появлялось новое действие?

**О:**
Вы можете написать любое событие, происходящее с течением действительного времени, если будете использовать локацию-счётчик.

Для начала нужно создать локацию-счётчик:

* создаём локацию, название может быть любым, например "реалтайм".
* указываем плееру, какую локацию ему нужно использовать, как локацию-счётчик. Пишем, например на самой первой локации в игре:

```qsp
$counter = "реалтайм"
```

По умолчанию обращение к локации-счётчику выполняется каждые пол секунды. Если нужно изменить период обращения, воспользуйтесь оператором `settimer`. В качестве аргумента этому оператору указывается период обращения к локации-счётчику в миллисекундах:

```qsp
! обращение к локации-счётчику каждые 100 мс.
settimer 100
```

Теперь на локации-счётчике пишем требуемый код. Например, данный код будет создавать действие "Шагнуть в портал" через 7 секунд после входа на локацию "зал_с_порталами":

```qsp
! фиксируем, в какое время обратились к локации-счётчику
local time_now=msecscount
if $curloc="зал_с_порталами":
! если текущая локация "зал_с_порталами"
    ! фиксируем в timer время, когда должно появиться действие
    if timer=0: timer=time_now+7000
    if time_now>=timer and timer>0:
    ! если текущее время достигло нужного
        ! записываем в переменную timer -1,
        ! чтобы больше этот код не исполнялся
        timer=-1
        ! создаём действие
        act "Шагнуть в портал":
            ! код в действии
            goto "лес_темносилья"
        ! закрываем действие
        end
    ! закрываем условие
    end
! закрываем условие
end
! переменная timer являюется глобальной
```

Довольно простой код. Функция `msecscount` возвращает, сколько прошло миллисекунд с момента начала игры.