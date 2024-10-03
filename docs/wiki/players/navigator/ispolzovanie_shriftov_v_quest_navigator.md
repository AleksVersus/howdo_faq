[Назад: Quest Navigator](../navigator)

# Использование шрифтов в Quest Navigator

Шрифты в Quest Navigator подключаются с помощью CSS-правила \@font-face.

Поддерживаемый формат шрифта - ".otf". Если у вас есть шрифт в формате True Type (".ttf"), то вы можете сконвертировать его в ".otf". Например, с помощью этого онлайн-сервиса: <http://everythingfonts.com/ttf-to-otf>

Пример использования: вставьте этот код в CSS-файл игры ("game.css").

Замените имя шрифта "Aksent" и путь к файлу "fonts/Aksent.otf" на ваши значения.

    /* 
    Указываем, откуда загружать шрифт с именем Aksent.
    Формат шрифта должен быть ".otf".
    Если у вас шрифт формата TrueType (".ttf"), 
    то сконвертируйте его в ".otf".
    Сконвертировать можно, например, через этот онлайн-сервис:
    http://everythingfonts.com/ttf-to-otf
    Путь к файлу шрифта указывается относительно CSS-файла.
    */
    @font-face {
      font-family: Aksent;
      src: url(fonts/Aksent.otf);
    }
    /* Назначаем шрифт Aksent для всей страницы */
    body {
      font-family: Aksent;
    }

————————————————————————

## Другие статьи

*  [Файлы игры на Quest Navigator](navigator_game_files)
*  [Параметры запуска Quest Navigator](navigator_command_line)
*  [Шаблон игры на Quest Navigator](navigator_game_template)
*  [Создание игр для плеера Quest Navigator](sozdanie_igr_na_quest_navigator)
*  Использование шрифтов в Quest Navigator
*  [Файл настроек игры в Quest Navigator](fajl_nastroek_igry_v_quest_navigator)
*  [Независимая сборка игры для Quest Navigator](navigator_standalone)
