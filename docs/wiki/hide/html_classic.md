# Поддерживаемые классическим плеером HTML-теги и атрибуты

(для более подробной информации смотрите справочники по HTML)

**!!! Внимание !!!** Атрибут `align` применительно к тегу `table` в **QSP** выравнивает текст внутри таблицы. Это поведение отличается от поведения в браузере. В браузере данный атрибут выравнивает таблицу по левому или правому краю родительского элемента.

  ———— —————————————————————————————————————————- —————————————————————————————--
  **тег**      **назначение**                                                                                                               **атрибуты**
  A            [гиперссылка](http://htmlbook.ru/html/a)                                                                                     NAME=\[строка\]
  :::          :::                                                                                                                          HREF="EXEC:\[строка_кода\]"
  :::          :::                                                                                                                          HREF="\[ссылка кода\]"
  :::          :::                                                                                                                          class="plain" (отключает подчёркивание ссылки)
  ADDRESS      [информация об авторе](http://htmlbook.ru/html/address)                                                                      
  AREA         [активные области изображения, которые являются ссылками](http://htmlbook.ru/html/area). Используется вместе с тегом MAP     SHAPE=POLY
  :::          :::                                                                                                                          SHAPE=CIRCLE
  :::          :::                                                                                                                          SHAPE=RECT
  :::          :::                                                                                                                          COORDS=\[координаты\]
  :::          :::                                                                                                                          HREF=\[ссылка\]
  :::          :::                                                                                                                          HREF="EXEC:\[строка_кода\]"
  B            [делает текст жирнее](http://htmlbook.ru/html/b)                                                                             
  BIG          [делает текст чуть больше](http://htmlbook.ru/html/big)                                                                      
  BLOCKQUOTE   [цитаты](http://htmlbook.ru/html/blockquote)                                                                                 
  BR           [перевод строки без разрыва абзаца](http://htmlbook.ru/html/br)                                                              ALIGN=\[выравнивание\]
  CENTER       [выравнивание по центру](http://htmlbook.ru/html/center)                                                                     
  CITE         [цитата или сноска на другой метериал](http://htmlbook.ru/html/cite)                                                         
  CODE         [выделение программного кода](http://htmlbook.ru/html/code)                                                                  
  DD           [определение](http://htmlbook.ru/html/dd). Тег используется вместе с тегами DT и DL для создания списка определений          
  DIV          [выделение блока в документе](http://htmlbook.ru/html/div)                                                                   ALIGN=\[выравнивание\]
  DL           [список определений](http://htmlbook.ru/html/dl). Тег используется вместе с тегами DT и DD для создания списка определений   
  DT           [термин](http://htmlbook.ru/html/dt). Тег используется вместе с тегами DD и DL для создания списка определений               
  EM           [акцентирование](http://htmlbook.ru/html/em)                                                                                 
  FONT         [изменение шрифта](http://htmlbook.ru/html/font)                                                                             COLOR=\[цвет\]
  :::          :::                                                                                                                          SIZE=\[-2,-1,+0,+1,+2,+3,+4 или 1,2,3,4,5,6,7\]
  :::          :::                                                                                                                          FACE=\[список названий шрифтов\]
  HR           [горизонтальная линия](http://htmlbook.ru/html/hr)                                                                           ALIGN=\[выравнивание\]
  :::          :::                                                                                                                          SIZE=\[пиксели\]
  :::          :::                                                                                                                          WIDTH=\[проценты\|пиксели\]
  :::          :::                                                                                                                          NOSHADE
  H1, H2, H3   [заголовки](http://htmlbook.ru/html/h1)                                                                                      
  H4, H5, H6   :::                                                                                                                          :::
  I            [выделение текста курсивом](http://htmlbook.ru/html/i)                                                                       
  IMG          [вставка изображения](http://htmlbook.ru/html/img)                                                                           SRC=\[ссылка\]
  :::          :::                                                                                                                          WIDTH=\[пиксели\]
  :::          :::                                                                                                                          HEIGHT=\[пиксели\]
  :::          :::                                                                                                                          ALIGN=TEXTTOP
  :::          :::                                                                                                                          ALIGN=CENTER
  :::          :::                                                                                                                          ALIGN=ABSCENTER
  :::          :::                                                                                                                          ALIGN=BOTTOM
  :::          :::                                                                                                                          USEMAP=\[ссылка\]
  KBD          [текст на клавиатуре](http://htmlbook.ru/html/kbd)                                                                           
  LI           [элемент маркированного списка](http://htmlbook.ru/html/li). Используется совместно с тегами UL или OL                       
  MAP          [контейнер для элементов AREA](http://htmlbook.ru/html/map)                                                                  NAME=\[строка\]
  OL           [нумерованный список](http://htmlbook.ru/html/ol). Пункты списка устанавливаются тегами LI                                   
  P            [абзац, параграф](http://htmlbook.ru/html/p)                                                                                 ALIGN=\[выравнивание\]
  PRE          [предварительно отформатированный текст](http://htmlbook.ru/html/pre)                                                        
  SAMP         [результат вывода программы](http://htmlbook.ru/html/samp)                                                                   
  SMALL        [немного уменьшает шрифт](http://htmlbook.ru/html/small)                                                                     
  SPAN         [форматирование части текста](http://htmlbook.ru/html/span)                                                                  STYLE=\[свойства CSS\] (Работают лишь некоторые свойства, например font-weight и color)
  STRIKE       [перечёркнутый текст](http://htmlbook.ru/html/strike) (В классическом плеере текст не перечёркивается, а подчёркивается)     
  STRONG       [акцентирование текста](http://htmlbook.ru/html/strong). Жирный шрифт                                                        
  SUB          [нижний индекс](http://htmlbook.ru/html/sub)                                                                                 
  SUP          [верхний индекс](http://htmlbook.ru/html/sup)                                                                                
  TABLE        [таблица](http://htmlbook.ru/html/table)                                                                                     ALIGN=\[выравнивание\]
  :::          :::                                                                                                                          WIDTH=\[проценты\|пиксели\]
  :::          :::                                                                                                                          BORDER=\[пиксели\]
  :::          :::                                                                                                                          VALIGN=\[выравнивание\]
  :::          :::                                                                                                                          BGCOLOR=\[цвет\]
  :::          :::                                                                                                                          CELLSPACING=\[пиксели\]
  :::          :::                                                                                                                          CELLPADDING=\[пиксели\]
  TD           [ячейка таблицы](http://htmlbook.ru/html/td)                                                                                 ALIGN=\[выравнивание\]
  :::          :::                                                                                                                          VALIGN=\[выравнивание\]
  :::          :::                                                                                                                          BGCOLOR=\[цвет\]
  :::          :::                                                                                                                          WIDTH=\[проценты\|пиксели\]
  :::          :::                                                                                                                          COLSPAN=\[количество\]
  :::          :::                                                                                                                          ROWSPAN=\[количество\]
  :::          :::                                                                                                                          NOWRAP
  TH           [заголовок таблицы](http://htmlbook.ru/html/th)                                                                              ALIGN=\[выравнивание\]
  :::          :::                                                                                                                          VALIGN=\[выравнивание\]
  :::          :::                                                                                                                          BGCOLOR=\[цвет\]
  :::          :::                                                                                                                          WIDTH=\[проценты\|пиксели\]
  :::          :::                                                                                                                          COLSPAN=\[количество\]
  :::          :::                                                                                                                          ROWSPAN=\[количество\]
  TR           [строка таблицы](http://htmlbook.ru/html/tr)                                                                                 ALIGN=\[выравнивание\]
  :::          :::                                                                                                                          VALIGN=\[выравнивание\]
  :::          :::                                                                                                                          BGCOLOR=\[цвет\]
  TT           [моноширинный текст](http://htmlbook.ru/html/tt)                                                                             
  U            [подчёркивание текста](http://htmlbook.ru/html/u)                                                                            
  UL           [маркированный список](http://htmlbook.ru/html/ul). Пункты списка устанавливаются тегами LI                                  
  ———— —————————————————————————————————————————- —————————————————————————————--

————————————————————————

[Назад: HTML](../design/html)
