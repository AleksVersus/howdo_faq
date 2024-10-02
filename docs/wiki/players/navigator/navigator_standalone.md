[Назад: Quest Navigator](../../navigator.md)

# Независимая сборка игры для Quest Navigator

Не все игры, созданные для Навигатора, будут распространяться через "Полку игр". Например, автору захочется распространять игру в виде готового инсталлятора.

Все средства для этого в Навигаторе предусмотрены.

## Создание независимой сборки игры

1.  Переименуйте файл игры в `start.qsp`.
2.  В [файле настроек](../fajl_nastroek_igry_v_quest_navigator.md) укажите режим `standalone`.
3.  Скопируйте папку плеера целиком в отдельное место, допустим `D:\MyGames\CoolGame-release`.
4.  Удалите игру "по умолчанию" - `D:\MyGames\CoolGame-release\standalone_content\start.qsp`.
5.  Поместите все файлы своей игры в папку `D:\MyGames\CoolGame-release\standalone_content`.

Теперь в папке `D:\MyGames\CoolGame-release` находится полностью независимая сборка игры. При запуске плеера из этой папки, ваша игра запустится автоматически. Эту папку можно распространять в виде архива, либо сделать инсталлятор.

## Другие статьи

*  [Файлы игры на Quest Navigator](../navigator_game_files.md)
*  [Параметры запуска Quest Navigator](../navigator_command_line.md)
*  [Шаблон игры на Quest Navigator](../navigator_game_template.md)
*  [Создание игр для плеера Quest Navigator](../sozdanie_igr_na_quest_navigator.md)
*  [Использование шрифтов в Quest Navigator](../ispolzovanie_shriftov_v_quest_navigator.md)
*  [Файл настроек игры в Quest Navigator](../fajl_nastroek_igry_v_quest_navigator.md)
*  Независимая сборка игры для Quest Navigator
