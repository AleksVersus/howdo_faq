---
sidebar_position: 4
---

# TXT2GAM. Сборка для Linux
<!-- [:informarch_forlinux] -->

Исходники: [github/QSPFoundation/txt2gam](https://github.com/QSPFoundation/txt2gam)

**Порядок сборки:**

1. Скачиваем все файлы с расширениями `*.c` и `*.h` и помещаем их в один каталог.
2. Открываем ваш терминал(gnome-terminal, xfce4-terminal, konsole или какой у вас там).
3. Пишем в консоли
    ```bash
    cd путь/до/директории/куда/скачали/файлы
    ```
4. Пишем в консоли
    ```bash
    gcc main.c coding.c locations.c memwatch.c text.c -o txt2gam
    ```
5. Ждем, пока оно компилируется.
6. ???
7. PROFIT

Теперь можете запустить программу, набрав в консоли

```bash
./txt2gam
```

из той директории, где лежит откомпилированный файл.
