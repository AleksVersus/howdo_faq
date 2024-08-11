---
sidebar_position: 6
---

# 6.6. Как зациклить мелодию?
<!-- [:faq_06_06] -->

**В:** Как зациклить мелодию?

**О:**

Зациклить одну мелодию во всей игре довольно просто.

* Создаём локацию и называем её, например, "счётчик". Это будет наша локация-счётчик.
* В самой первой локации в игре указываем плееру, какую локацию он должен использовать, как локацию-счётчик, прописывая вот такую команду:
    ```qsp
    $counter="счётчик"
    ```
* На локации "счётчик" пишем код вроде этого:
    ```qsp
    if ISPLAY("путь к файлу/мелодия.wav")=0:
    ! если мелодия не воспроизводится (isplay возвращает 0)
        ! запускаем мелодию по-новой.
        PLAY "путь к файлу/мелодия.wav"
    end
    ```

Чтобы зацикливать определённую мелодию в пределах одной локации, а на другой локации зациклить другую мелодию, в локации-счётчике потребуется прописать более сложный код:

```qsp
if $curloc="комната":
! если мы на локации "комната"
    ! запускаем воспроизведение мелодии, если она закончилась
    if ISPLAY("путь к файлу/мелодия_комната.wav")=0:
        PLAY "путь к файлу/мелодия_комната.wav"
    end
else
! если мы не на локации комната,
    ! закрываем мелодию комнаты
    CLOSE "путь к файлу/мелодия_комната.wav"
end

if $curloc="коридор":
! если мы на локации "коридор"
    ! запускаем воспроизведение мелодии, если она закончилась
    if ISPLAY("путь к файлу/музыка_коридор.mp3")=0:
        PLAY "путь к файлу/музыка_коридор.mp3"
    end
else
! если мы не на локации "коридор",
    ! закрываем мелодию коридора
    CLOSE "путь к файлу/музыка_коридор.mp3"
end
```

и т.д.

Или воспользуйтесь уже готовым решением в виде [гибкого плейлиста](../../../informarch/program/lib_flex_playlist.md).