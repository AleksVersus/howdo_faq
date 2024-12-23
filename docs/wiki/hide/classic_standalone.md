# Standalone-сборка игры на классическом плеере

По этому вопросу записано отдельное видео на ютубе: [https://youtu.be/Ca4ynD_1BqQ](https://youtu.be/Ca4ynD_1BqQ)

О создании файла запуска: Genryzz. #3912 21.Фев.16 21:30:40: [как сделать пусковой файл?](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=157&prc=25&Itemid=57#p23065)

Статья Серого Волка в теме [Возможности) Помогите разобраться](https://qsp.su/index.php?option=com_agora&task=topic&id=88&Itemid=57)

Непосредственно без плеера ни одна игра QSP не запустится.

Но если вам лень объяснять всем и каждому, что игры QSP запускаются на специальном плеере, что надо отдельно качать плеер, отдельно — игры, то есть специальная инструкция по упаковке и файла плеера и файла игры в самораспаковывающийся sfx-архив, который заменит привычный для игрока установщик.

Выше есть ссылка на изначальную версию данной инструкции, мы же сейчас рассмотрим вариант распространяемой standalone-сборки, включающий как изначальную версию, так и работу с пакетным файлом `.bat`, который позволит игроку запускать игру одним кликом (прямо с рабочего стола).

Названия всех файлов и папок, которые вы будете использовать при сборке игры, должны быть только латинскими буквами.

Для того, чтобы проделать нижеследующие шаги, вам потребуется заранее установить на компьютер программу WinRAR. Она условно-бесплатная. После того, как установите WinRAR, выполните следующее:

## Подготовка файлов для сборки

1. В первую очередь необходимо завести отдельную папку, назовём её "Standalone". Можете создать её прямо на рабочем столе, это папка, в которую мы скопируем все необходимые нам файлы, чтобы затем создать sfx-архив.
2. Если вы хотите добавить оригинальную иконку на сам sfx-архив и на ярлык, с которого будет запускаться игра, скопируйте файлы иконок в папку "Standalone". Далее в инструкции будет указано, что и где прописать, чтобы эти иконки задействовать.
3. Скопируйте игру и все сопутствующие ей файлы и папки в папку "Standalone". Например, файл игры называется "moonlight.qsp", он должен оказаться в папке "Standalone".
4. Создайте в папке "Standalone" папку "Player"
5. Скачайте архив с плеером и распакуйте в папку "Player" всё содержимое архива. Таким образом в папке "Player" будет "qspgui.exe" и другие файлы и папки.

## Создание bat-файла

1. Создаём в папке "Standalone" текстовый файл, называем его "Start", а вместо расширения ".txt" пишем расширение ".bat"
2. Открываем файл "Start.bat" с помощью любого текстового редактора. В этом файле прописываем такую команду:
  
  ```plain
  start "Player/qspgui.exe" "moonlight.qsp"
  ```

  * start — это команда, запускающая исполняемый файл,
  * первым аргументом указываем путь к исполняемому файлу, то есть к нашему плееру,
  * вторым аргументом — путь к игре.
  * Поскольку плеер лежит во вложенной папке, а файл игры в той же папке, что и "start.bat" можно указывать относительные пути. Но если вы точно знаете, в какие папки будут распакованы игра и плеер, можете указать и абсолютные пути.

## Упаковка подготовленных файлов в SFX-архив

1. Теперь в папке "Standalone" выделяем папку "Player", выделяем игру ("moonlight.qsp") и все сопутствующие ей файлы и папки, выделяем файл "start.bat", щёлкаем правой кнопкой мыши по любому из выделенных файлов и из всплывающего контекстного меню выбираем пункт "Добавить в архив\..."
2. Откроется диалоговое окно по добавлению файлов в архив. Указываем имя архива. Можно написать например "moonline_setup".
3. На вкладке "Дополнительно" заходим в "параметры SFX".
4. На вкладке "Общие" указываем путь для распаковки. Рекомендую указывать абсолютный путь, так как неизвестно, откуда игрок запустит ваш "установщик". Например, можно прописать такой путь:

    ```plain
    C:\QSP_Games\MoonLight
    ```

5. На вкладке "Дополнительно" можно добавить ярлык:
    * Нажимаем кнопку "Добавить ярлык\...", откроетя диалоговое окно.
    * Отмечаем в списке "Место создания ярлыка" пункт "На рабочем столе".
    * В поле "Имя файла для которого будет создан ярлык" пишем:

    ```plain
    start.bat
    ```

    * В поле "Имя ярлыка" можно написать название игры ("MoonLight").
    * В поле "Значок ярлыка" прописываем относительный путь к файлу иконки, которую мы хотим увидеть на ярлыке (эта иконка лежит у нас в папке "Standalone" и тоже должна быть упакована в архив).
    * Нажимаем "ОК".
6. На вкладке "Текст и графика" можно прописать некоторые данные. Например, вы можете установить свой логотип, написать текст приветствия для игрока и заголовок окна. Если вы подготовили оригинальный значок/иконку для своего sfx-архива, на этой вкладке можно указать путь к файлу этого значка (эта иконка опять же у нас уже лежит в папке "Standalone").
7. На вкладке "Обновление" отмечаем пункты "извлечь и заменить файлы" и "перезаписывать файлы без запроса".
8. Нажимаем кнопку "ОК", и снова "ОК" в основном окне.

В папке "Satndalone" должен появиться файл с расширением ".exe" ("moonline_setup.exe"). Остаётся только проверить, как данный "установщик" работает, и можно распространять игру среди друзей и знакомых.
