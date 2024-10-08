[Назад: Quest Navigator](../navigator)

## Файлы игры на Quest Navigator

В папке с игрой должны быть две папки:

* **qsplib** - стандартная папка для всех игр, содержащая часть игрового движка, лезть туда не советую, позже она перестанет быть обязательной, пока папку нужно скопировать из папки с плеером.
* **standalone_content** - здесь находится сама игра

Папка **standalone_content**:

* *game.qsp* - файл игры QSP ((Вместо "game" может быть любое название игры))
* шаблоны оформления для разных игровых платформ:
    * *[gameAwesomium.html](navigator_game_template)* - устройства на Windows
    * *gamePG-android.html* - устройства на Android
    * *gamePG-ios.html* - устройства на iOS
* *[config.xml](fajl_nastroek_igry_v_quest_navigator)* - файл настроек игры
* *[game.css](navigator_game_template)* - файл стилей, от этого файла зависит внешний вид игры
* *game.js* - файл JS, в котором программируются дополнительные функции
* все остальные файлы.

*В корне папки **standalone_content** должны находиться файлы из первых трёх пунктов перечисления. Остальные можно и рекомендуется держать в подпапках для удобства.*\
*Все дополнительные QSP файлы (подключаемые модули) должны **обязательно** быть в подпапках ((Т.к. игра запускается из первого найденного файла .qsp в корне **standalone_content**)).*

————————————————————————

## Другие статьи

*  Файлы игры на Quest Navigator
*  [Параметры запуска Quest Navigator](navigator_command_line)
*  [Шаблон игры на Quest Navigator](navigator_game_template)
*  [Создание игр для плеера Quest Navigator](sozdanie_igr_na_quest_navigator)
*  [Использование шрифтов в Quest Navigator](ispolzovanie_shriftov_v_quest_navigator)
*  [Файл настроек игры в Quest Navigator](fajl_nastroek_igry_v_quest_navigator)
*  [Независимая сборка игры для Quest Navigator](navigator_standalone) 
