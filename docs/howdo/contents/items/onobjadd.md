---
sidebar_position: 11
---

# 14.11. Как сделать, чтобы плеер выполнял определённый код при добавлении любого предмета?
<!-- [:faq_14_11] -->

**В:** Как сделать, чтобы плеер выполнял определённый код при добавлении любого предмета?

**О:**
Для этого используйте локацию-обработчик события "добавление предмета". Чтобы сделать это, нужно:
* создать локацию, например с названием "`предмет_добавлен`" (название может быть любым),
* указать плееру, какую локацию он должен использовать, как локацию-обработчик события "добавление предмета":
    ```qsp
    $onobjadd = "предмет_добавлен"
    ```
    
Теперь на локации "предмет_добавлен" можно прописать нужный вам код.

Локации-обработчику события "добавление предмета" передаются два значения, которые вы можете получить из массива `args`:
* `$args[0]` — название добавляемого предмета
* `$args[1]` — путь к файлу картинки добавляемого предмета

Код локации-обработчика события "добавление предмета" выполняется уже после того, как предмет добавлен в окно предметов. Учитывайте это, например, при использовании функции `countobj`.