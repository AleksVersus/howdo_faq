


```qsp
msg "<<'>>'>>"
msg '<<"a"" >> b">>'
msg "<<len('a''>>b') + #args[0]>>"
msg "<<1>><<'>>'>>"
! {
comment
}
    msg "<<len('>>') + 中國>>"
msg "<<'unfinished >>"
msg 42
```

```qsp
msg 0 & :retry & msg 1
if 1:
    msg 2
end if { protected & } note & msg 3
:!label & ! ordinary comment & still comment
msg 4
```

```qsp
# room
#counter = 1
#args[0]
#len('abc')
#name
#
msg 42
```

```qsp
if 1:
    ! comment
    msg 1
    ! {
    multiline comment
    }

    msg 2
end
```

```qsp
# Bob's room
! {
msg 42
}
msg 43
-- Bob's room
! {
msg 44
}
msg 45
```

```qsp
! Всё подсвечивается корректно:
if ($a and $b):
    *pl "if baseline ok"
else:
    *pl "else baseline ok"
end

act ("desc", $x > 0):
    *pl "act baseline ok"
end

loop local $i while $i < 5 step $i += 1:
    *pl "<<$i>>"
end
```

```qsp
! Многострочный if с многострочным условием
if (1 +
    2) = 3:
    *pl "тело if"
elseif (4 +
    3) = 9:
!^^^^^ elseif валиден
    *pl "тело elseif"
else:
!^^^ else валиден
    *pl "тело else"
end
!^^ end валиден
```

```qsp
! Однострочный if с многострочным условием
if [1,
    2,
    3] = $arr: *pl "массив в условии"
else:
!^^^ else подсвечивается как invalid — ВЕРНО: однострочная форма if (утверждение после ':')
    *pl "else"
end
!^^ end подсвечивается как invalid — ВЕРНО: однострочная форма
```

```qsp
! Однострочная act c многострочным аргументом
act ("взять ключ",
    hp > 0): *pl "тело act"
end
!^^ end подсвечивается как invalid — ВЕРНО: однострочная форма act
```

```qsp
! многострочная скобка внутри while многострочного loop
loop while (i <
    (5 +
    1)) step i += 1:
    *pl "тело loop <<i>>"
end
!^^ end валиден

! многострочность в loop ДО while (Фаза 8): tuple в инициализирующей группе,
! 'while' приходит только после закрытия скобки — заголовок валиден.
loop local i = [1,
    2,
    3 ] while i = [1,
    2,3] step o+=1:
!^^^ loop валиден (Фаза 8 починена: guard «while на строке» снят с bracket-arm)
    *pl 'ffff'
end
!^^ end валиден (блок открыт: 'while' наступил до ':')
```

```qsp
! Многострочная скобка до 'while', но 'while' в заголовке НЕ появляется —
! битый код (grammar loopMultiLine требует whileMarker). Pending обязан НЕ
! открывать блок: ':' наступил раньше 'while'.
loop local i = [1,
    2,
    3 ] step o+=1:
    *pl 'broken loop'
end
!^^ end подсвечивается как invalid — ВЕРНО: блок не открыт (заголовок без while)
```

```qsp
! Тот же кейс Фазы 8 внутри {…} — зеркало multiline_loop_pending_prewhile_braced.
{
    loop local i = [1,
        2,
        3 ] while i = [1,2,3] step o = rand(1,
            23):
        *pl 'braced loop'
    end
    !^^ end валиден
}
```

```qsp
!!! ПОМЕТИ: act с многострочной ( ВНУТРИ многострочного if. Оба end не должны быть ошибками.
if (a and
    b):
    act ("дело",
        c >
        d):
        *pl "внутри if, внутри act"
    end
    !^^ end валиден
end
!^^ end валиден
```

```qsp
! Скобки внутри кавычек не ломают подсветку
! и закрывается на строке с ':'.
if ("текст (не скобка" +
    " ещё текст") = $s:
    *pl "проверка строковых скобок"
end
!^^ end валиден
```

```qsp
!!! '!' после ':' на строке закрытия заголовка — не должен мешать открытию.
if (a and
    b): ! обычный комментарий после двоеточия
    !^^^^^^^^^^^^^ комментарий после ':' валиден
    *pl "тело"
end
!^^ end валиден
```

```qsp
!!! 
{
    if (x and
        y):
        *pl "braced if тело"
    else:
    !^^^ else валиден
        *pl "braced else"
    end
    !^^ end валиден
}
```

```python
a = [1, 2, 3]
```
## list item

- lorem ipsum i td
- lorem ipsum
  ```qsp
  load = 'dkkdkdkdkdkd'
  ```
- ldldldldldldl
  ```qsp
    @foo(123, 'dddsd')
    @@stmt 123, 'dkdkka'
  ```
- ;d;d;d;d;d;d;d


```qsp
local $top_text = $args[0] & ! text from top
local $command = $iif($args[1]<>"", $args[1], "*pl") & ! command for print text
local $screen = $mid($args[1], 1, 1) & ! first symbol from command
local $text = ""
if $screen="*":
  ! if fist symbol is *
  ! main description wondow
  $text=$maintxt
else
  ! addition description window
  $text=$stattxt
end
! use dynamic for run command:
dynamic "
  <<$screen>>clr
  <<$command>> $args[0]
  <<$screen>>p $args[1]
", $top_text, $text
```
