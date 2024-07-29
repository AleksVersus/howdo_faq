# Инструкция по использованию AeroQSP совместно с Quest Generator
<!-- [:informarch_aeroqsp_instr] -->

1. Скачиваем https://qsp.org/misc/aero/aerodev.zip
2. Скачиваем https://qsp.org/attachments/aeroshell.zip
3. Черновик документации по новым фичам - https://qsp.org/misc/aero/help.htm
4. В файле "`run_flash.bat`" из "aerodev.zip" редактируем путь к "`AeroQSP.exe`" - AEROQSP.
5. В QGen указываем вместо "`qspgui.exe`" - файл "`run_flash.bat`"

Для игр нужно создавать отдельные папки - при запуске всё содержимое папки с игрой архивируется в ZIP и ссылка передается в "`AeroQSP.exe`".

При запуске "`run_flash.bat`" вручную, необходимо указывать полный путь к файлу с игрой ("`.qsp`"). Например, `run_flash.bat "d:\aero\file.qsp"`


Для работы Aeroshell требуется предустановленный плагин Flash для Internet Explorer. Брать здесь: http://get.adobe.com/ru/flashplayer/otherversions

#### Примечание Aleks Versus:
	
 > AeroQSP — плеер, работающий на устаревшей и отжившей своё технологии Flash. Adobe прекратила поддержку данной технологии, что означает, что AeroQSP стало невозможно использовать. Игры AeroQSP можно пробовать запустить на [qSpider](https://aleksversus.github.io/howdo_faq/articles/qspider_0004#qspider_0120), но это так же потребует танцев с бубнами. Лучше писать игры сразу для qSpider, не уповая на то, что он поддерживает AeroQSP.

Следующий раздел перенесён из справочника по самым часто задаваемым вопросам.

## 24.1. Как сделать так, чтобы AeroQSP запускался прямо из Quest Generator?
<!-- [:faq_24_01] -->
В: Как сделать так, чтобы AeroQSP запускался прямо из Quest Generator?

О:
Всё довольно просто. Вам необходимо воспользоваться инструкцией по этой ссылке https://qsp.org/misc/aero/readme.txt

Если что-то не получается, от себя лично могу посоветовать следующее:

1. Скачайте все три архива по этим ссылкам:
	* [AeroShell](https://qsp.org/attachments/aeroshell.zip)
	* [AeroDev](https://qsp.org/misc/aero/aerodev.zip)
	* [QGen 4.0.0b](https://qsp.org/attachments/qgen400b1.zip)
2. Распакуйте их содержимое в одну папку
3. Откройте файл "run_flash.bat" с помощью любого текстового редактора, найдите строку, содержащую `SET AEROQSP=` и после знака равенства замените путь к файлу "AeroQSP.exe" просто на "AeroQSP.exe", так как сейчас файл плеера лежит в той же папке, что и "run_flash.bat". То есть теперь строка должна выглядеть так:
	```
	SET AEROQSP=AeroQSP.exe
	```
4. Откройте Quest Generator, зайдите в меню "Утилиты", выберите пункт "Настройки...", откройте вкладку "Пути"
5. Здесь рядом с полем "Путь к плееру" нажмите на кнопку "Выбрать путь...". Откроется окно, которое будет предлагать вам указать на файл, который нужно использовать как плеер.
6. Вместо типа файла "Файл плеера (`*.exe`)", укажите "Все файлы (*.*)". Вам станет доступным файл "`run_flash.bat`", нажмите на него и нажмите кнопку "открыть". После этого окно настроек можно закрывать нажатием "Ок".
7. Создайте локацию, напишите на ней пару команд для проверки (чтоб выводился текст, действие, предмет и т.п.), затем сохраните игру в ОТДЕЛЬНОЙ папке
8. Запустите игру нажатием кнопки "Запустить игру" в Quest Generator или клавиши "`F5`" на клавиатуре. После того, как на экране пройдут различные команды, запустится оболочка AeroQSP. Убедитесь, что игра работает.

Если оболочка AeroQSP не запустится, или запустится с чёрным экраном, обновите версию флеш-плеера

###### 23.1.  Как сделать так, чтобы AeroQSP запускался прямо из Quest Generator?
<!-- [:link_24_01] -->
- Смотреть ответ на ютубе: [https://youtu.be/UqcQhd-HFzw](https://youtu.be/UqcQhd-HFzw)
- NickoAilus. #5647 18.Май.19 10:50:55: [Что надо сделать с QGen, чтобы он заработал на AeroQSP?](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=226&prc=25&Itemid=57#p25202)
- Инструкция по работе с AeroQSP: [https://qsp.org/misc/aero/help.htm](https://qsp.org/misc/aero/help.htm)
- Инструкция по запуску AeroQSP из QGen: [https://qsp.org/misc/aero/readme.txt](https://qsp.org/misc/aero/readme.txt)
- Запуск AeroQSP из Quest Generator: [Тема на форуме QSP.su](https://qsp.org/index.php?option=com_agora&task=topic&id=297&Itemid=57)
- Stand-alone сборка на AeroQSP: [статья на QSP.su](https://qsp.org/index.php?option=com_content&view=article&id=117&Itemid=56)
- Lisichka. #3849 05.Фев.16 00:51:59: [можно ли как-то в аэру добавить второе окно доп описания?](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=154&prc=25&Itemid=57#p22877)
- Mira. #4952 28.Фев.17 22:49:27: [Создала на аеро свой хелоуворд, через standalone не работает, swf создается, грузится и черный экран дальше](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=199&prc=25&Itemid=57#p25311)
- BlooDwareN. #5182 10.Янв.18 22:00:22: [как установить AeroQSP!](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=208&prc=25&Itemid=57#p26298)
