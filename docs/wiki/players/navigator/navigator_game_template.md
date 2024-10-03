[Назад: Quest Navigator](../navigator)

## Шаблон игры на Quest Navigator

Шаблон игры отвечает за внешний вид игры. В шаблон игры входят: страницы html для соответствующих платформ, файлы стилей для соответствующих платформ [^1], файлы JavaScript для соответствующих платформ [^2] и другие файлы (например, изображения и шрифты).

***Файл шаблона рассмотрен на примере gameAwesomium.htm из одной из работающих игр .***

## Файл шаблона игры в Quest Navigator

### Заголовок (head) страницы

```html5
<head>
  <meta charset="utf-8"> <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <meta name="format-detection" content="telephone=no">
  <link type="text/css" href="../standalone_content/folder/game.css" rel="stylesheet" />
  <script type="text/javascript" src="../qsplib/js/core.js"></script>
  <script type="text/javascript" src="../qsplib/js/coreAwesomium.js"></script>
  <script type="text/javascript" src="../qsplib/js/QspLibAwesomium.js"></script>
  <script type="text/javascript" src="../qsplib/js/api.js"></script>
  <script type="text/javascript" src="../standalone_content/folder/js/game.js"></script>
  <script type="text/javascript">
    $(document).ready(function(){
        qspInitApi();
      });
  </script>
</head>
```

Я не буду разбирать каждую строчку, т.к. это излишне и я сам многого не понимаю. Нас интересуют только следующие строчки:

```html5
<link type="text/css" href="../standalone_content/folder/game.css" rel="stylesheet" />
<script type="text/javascript" src="../standalone_content/folder/js/game.js"></script>
```

В первой строке адрес [файла стилей (CSS)](fajl_css_igry_v_quest_navigator) игры. Во второй адрес [файла JavaScript](fajl_js_igry_v_quest_navigator) игры. Нужно следить, чтобы эти адреса соответствовали действительности. В данном примере файл *game.css* лежит по адресу *folder/game.css*, а файл *game.js* лежит по адресу *folder/js/game.js* относительно папки *standalone_content*.

### Тело (body) страницы

А вот в структуре body без участия разработчика разобраться будет сложно. По моему мнению здесь стоило бы вставить табличку соответствия id\<-\>назначение, а потом примеры популярных конструкций.

    <div id="qsp-main">Пример использования id</div>
    <div class="qsp-center">Пример использования class</div>

Таблица id, используемых QSP Navigator\'ом:

  ———————————————————————————————--
  id                                                 Назначение
  ————————————————-- ——————————————--
  qsp-js-sandbox                                     Не добавлять в body [^3], служебный [^4]

  qsp-back-image                                     Контейнер для фонового изображения

  qsp-wrapper-main, qsp-scroller-main, qsp-main      Контейнер для описания локации

  qsp-wrapper-acts, qsp-scroller-acts, qsp-acts      Контейнер для списка действий локации[^5]

  qsp-wrapper-objs, qsp-scroller-objs, qsp-inv       Контейнер для инвентаря[^6]

  qsp-wrapper-vars, qsp-scroller-vars, qsp-vars      Контейнер для дополнительного описания[^7]

  qsp-input-line input                               Строка ввода [^8] [^9]

  qsp-dialog-view, qsp-dialog-view-image-container   Контейнер для просмотра картинок [^10]

  qsp-dialog-msg, qsp-wrapper-msg,\                  Контейнер для диалоговых окон
  qsp-scroller-msg, qsp-dialog-msg-content           

  qsp-dialog-error, qsp-dialog-error-content         Контейнер для ошибок

  qsp-dialog-user-menu                               Контейнер для пользовательского интерфейса

  qsp-dialog-input                                   Контейнер диалога ввода

  qsp-dialog-input-content                           Текст приглашения для ввода

  qsp-dialog-input-text                              Поле для ввода текста

  qsp-button-input-ok                                Кнопка подтверждения ввода текста

  qsp-dialog-system-menu                             

  qsp-dialog-save-slots,\                            Контейнер для меню сохранения/загрузки
  qsp-dialog-save-slots-container                    
  ———————————————————————————————--

  class                    Назначение
  ———————— —————————————————————
  qsp-center               автоматическое выравнивание по центру экрана
  qsp-skin-overlay         оверлей для системного меню (system-menu)
  qsp-skin-dialog          
  qsp-save-slot-enabled    Не добавлять в body[^11]
  qsp-save-slot-disabled   Не добавлять в body[^12]
  qsp-user-menu-item       Не добавлять в body[^13]
  qsp-action               Не добавлять в body[^14]
  qsp-skin-button          Не добавлять в body[^15]. Используется для action и save-slot
  qsp-object               Не добавлять в body[^16]

————————————————————————

## Другие статьи

*  [Файлы игры на Quest Navigator](navigator_game_files)
*  [Параметры запуска Quest Navigator](navigator_command_line)
*  Шаблон игры на Quest Navigator
*  [Создание игр для плеера Quest Navigator](sozdanie_igr_na_quest_navigator)
*  [Использование шрифтов в Quest Navigator](ispolzovanie_shriftov_v_quest_navigator)
*  [Файл настроек игры в Quest Navigator](fajl_nastroek_igry_v_quest_navigator)
*  [Независимая сборка игры для Quest Navigator](navigator_standalone)

[^1]: чаще всего один файл на все платформы

[^2]: чаще всего один файл на все платформы

[^3]: Генерируется автоматически

[^4]: используется для выполнения команды EXEC

[^5]: см. SHOWACTS

[^6]: см. SHOWOBJS

[^7]: см. SHOWSTATS

[^8]: обратите внимание - это должно быть \<input class="qsp-input-line"\> \</input\>, на данный момент поддержка этой области сильно ограничена

[^9]: см. SHOWINPUT

[^10]: см. VIEW

[^11]: Генерируется автоматически

[^12]: Генерируется автоматически

[^13]: Генерируется автоматически

[^14]: Генерируется автоматически

[^15]: Генерируется автоматически

[^16]: Генерируется автоматически
