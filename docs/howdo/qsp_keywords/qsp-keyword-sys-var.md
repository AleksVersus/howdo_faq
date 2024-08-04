---
sidebar_position: 4
---

# Системные переменные
<!-- [:faq_80_04] -->

### $BACKIMAGE
<!-- [:faq_80_04_backimage] -->

`$BACKIMAGE` —  содержит путь к файлу фонового изображения для окна основного описания. Фон в окне основного описания отображается в том случае, если значение данной переменной отлично от '' (т.е. не пустая строка) и файл изображения удалось загрузить.

	Пример:
```qsp
		$backimage="img/bg.png" & ! устанавливаем фоновым изображение, которое лежит в папке "img".
```
```qsp
		$backimage="" & ! убираем изображение из фона окна основного описания.
```
### $COUNTER
<!-- [:faq_80_04_counter] -->

`$COUNTER` —  содержит название локации-счётчика. Локация-счётчик может использоваться для реалтаймовых событий (то есть событий, происходящих в действительном времени); например, плавное изменение цвета фона, постепенный вывод текста на экран, плейлист для постоянного проигрывания музыки и другие.

	Локация-счетчик вызывается через одинаковые промежутки времени, по умолчанию каждые 500 мс, т.е. 2 раза в секунду. Автоматическое обновление интерфейса срабатывает с той же частотой. Промежутки задаются оператором `settimer` в миллисекундах.

	Если ваша локация-счётчик называется "Счётчик", на самой первой локации в игре нужно написать:
```qsp
		$counter='Счётчик'
```
	Как правило, чтобы не путаться, локацию называют так же, как и служебную переменную — "Counter":
```qsp		
		$counter='Counter'
```
	Чтобы отключить выполнение локации-счётчика, нужно задать пустое значение переменной `$COUNTER`:
```qsp
		$counter=""
```
### $FNAME
<!-- [:faq_80_04_fname] -->

`$FNAME` —  содержит название используемого в данный момент шрифта. Если равна `''` (пустая строка), то используется шрифт, заданный в настройках программы.

	Пример:
```qsp
		! устанавливаем для всей игры шрифт Courier New
		$fname="Courier New"
```
### $ONACTSEL
<!-- [:faq_80_04_onactsel] -->

`$ONACTSEL` —  содержит название локации-обработчика события "выделение действия". Иными словами, в этой переменной указывается название локации, код на которой срабатывает, когда одно из выведенных на экран действий выделено.

	Следует помнить, что выделение действия происходит при наведении на него указателя мыши, а не при непосредственном нажатии.

	Назначаем в качестве локации-обработчика события "выделение действия" локацию "on_mouse":
```qsp
		$onactsel="on_mouse"
```
	Данная локация полезна, к примеру, для вывода изображений или проигрывания звуков при выборе действий. Получить название выбранного действия можно через функцию `$selact`.
```qsp
		if instr(1,$selact,'пойти'): play 'sounds\walk.mp3'
```
	Чтобы отключить локацию-обработчик события "выделение действия", нужно задать переменной `$onactsel` пустое значение:
```qsp
		$onactsel=""
```
### $ONGLOAD
<!-- [:faq_80_04_ongload] -->

`$ONGLOAD` —  содержит название локации-обработчика события "загрузка состояния игры" (далее "обработчик загрузки состояния"). Иными словами, в эту переменную записывается название локации, код которой будет выполняться всякий раз после того, как был загружен файл сохранения состояния игры ("файл сохранения") с помощью команды opengame.

	Назначаем в качестве обработчика загрузки состояния локацию "on_game_load":
```qsp
		$ongload="on_game_load"
```
	Чтобы отключить обработчик загрузки состояния, нужно задать переменной `$ongload` пустое значение:
```qsp
		$ongload=""
```

### $ONGSAVE
<!-- [:faq_80_04_ongsave] -->
`$ONGSAVE` - содержит название локации-обработчика события "сохранение состояния игры" (далее "обработчик сохранения состояния"). Иными словами, в эту переменную записывается название локации, код которой будет выполняться всякий раз после того, как было записано состояние игры в новый или уже существующий файл сохранения состояния игры ("файл сохранения") с помощью команды `savegame`.

	Назначаем в качестве обработчика сохранения состояния локацию "on_game_save":
```qsp
		$ongsave="on_game_save"
```
	Чтобы отключить обработчик сохранения состояния, нужно задать переменной `$ongsave` пустое значение:
```qsp
		$ongsave=""
```
### $ONNEWLOC
<!-- [:faq_80_04_onnewloc] -->

`$ONNEWLOC` —  содержит название локации-обработчика перехода на новую локацию (аналог локации "common" в URQ). Иными словами, в эту переменную записывается название локации, код которой выполняется каждый раз после выполнения кода локации, на которую был осуществлён переход с помощью операторов `goto` или `xgoto`. Управление игрой передаётся игроку уже после выполнения кода на этой локации-обработчике.

	Назначаем в качестве обработчика перехода на новую локацию локацию "on_goto_newloc":
```qsp
		$onnewloc="on_goto_newloc"
```
	Получить название локации, на которую был осуществлён переход, можно с помощью функции `$curloc`.
```qsp		
		if $curloc = 'дом': кошка = 1
```
	Чтобы отключить локацию-обработчик перехода на новую локацию, нужно задать переменной `$onnewloc` пустое значение:
```qsp
		$onnewloc=""
```
### $ONOBJADD
<!-- [:faq_80_04_onobjadd] -->

`$ONOBJADD` —  содержит название локации-обработчика события "добавление предмета". Иными словами, в эту переменную записывается название локации, код которой выполняется всякий раз после добавления предмета в окно предметов с помощью команды `addobj`.

	При добавлении предмета этой локации-обработчику передаются два аргумента, значения которых можно получить из `$args[0]` и `$args[1]` соответственно:

		* $ARGS[0] - название добавленного предмета
		* $ARGS[1] - путь к картинке добавленного предмета

	Данная локация полезна, к примеру, для ограничения вместительности рюкзака.

	Назначаем в качестве локации-обработчика события "добавление предмета" локацию "on_object_add":
```qsp
		$onobjadd="on_object_add"
```
	Чтобы отключить локацию-обработчик события "добавление предмета", нужно задать переменной `$onobjadd` пустое значение:
```qsp
		$onobjadd=""
```

### $ONOBJDEL
<!-- [:faq_80_04_onobjdel] -->

`$ONOBJDEL` —  содержит название локации-обработчика события "удаление предмета". Иными словами, в эту переменную записывается название локации, код которой вполняется всякий раз при удалении предмета с помощью команды `delobj`. Если воспользоваться командой `killobj`, то это будет аналогично серии команд `delobj`, соответственно и локация-обработчик будет вызвана столько раз, сколько предметов будет удалено с помощью `killobj`.

	При использовании команды `killall` локация-обработчик удаления предмета не вызывается, поскольку системная переменная `$onobjdel` уничтожается.

	При удалении предмета этой локации-обработчику передаётся аргумент, значение которого можно получить из `$args[0]`:

		* $ARGS[0] - название удалённого предмета

	Назначаем в качестве локации-обработчика события "удаление предмета" локацию "on_object_del":
```qsp
		$onobjdel="on_object_del"
```
	Данная локация полезна, к примеру, для проверки возможности удаления предмета:
```qsp
		! например есть предмет, который нам пригодится по сюжету
		if $args[0]="Важный артефакт":
			! восстанавливаем предмет
			addobj $args[0]
		end
```
	Чтобы отключить локацию-обработчик события "удаление предмета", нужно задать переменной `$onobjdel` пустое значение:
```qsp
		$onobjdel=""
```
### $ONOBJSEL
<!-- [:faq_80_04_onobjsel] -->

`$ONOBJSEL` —  содержит название локации-обработчика события "выделение предмета" (далее "локация-обработчик выделения предмета"). Иными словами, в этой переменной указывается название локации, код на которой выполняется всякий раз при выделении предмета. Выделение предмета происходит непосредственно при "нажатии" на предмет (щелчок мышью по предмету).

	Назначаем в качестве локации-обработчика выделения предмета локацию "on_object_select":
```qsp
		$onobjsel="on_object_select"
```
	Данная локация полезна, к примеру, для выводаинформации о предмете, или меню предмета. Получить название выбранного предмета можно через функцию `$selobj`.
```qsp
		if $selobj = 'чайник':
			p 'Cамый обычный чугунный чайник.'
		end
```
	При выборе играющим какого-либо предмета, он остаётся выделенным. Снять выделение можно командой `unselect`.

### $USERCOM
<!-- [:faq_80_04_usercom] -->

`$USERCOM` —  содержит название локации-обработчика строки ввода (поля ввода). Код данной локации-обработчика выполняется, если курсор установлен в строку ввода в момент нажатия клавиши "Enter" .

	Назначаем в качестве локации-обработчика строки ввода локацию "user_command_line":
```qsp
		$usercom="user_command_line"
```
	Полезна при организации парсера (управление игрой с помощью строки ввода), или для организации отладчика. Пример кода для локации-обработчика:
```qsp
		! если введённый текст соответствует названию существующей локации
		if (loc $user_text)=-1:
			! осуществляем переход на эту локацию
			goto $user_text
		end
```
### ARGS ($ARGS)
<!-- [:faq_80_04_args] -->

`ARGS` —  специфический системный массив, в который помещаются значения аргументов, передаваемых пользователем при обращении к локации или коду, записанному в виде текста. Пример:

```qsp
		gosub "#array.srtd#","$mass","rug","$time_ar"
```

	Здесь на локацию "#array.srtd#" будут переданы три аргумента, которые поместятся в первые три ячейки массива `$args` соответсвенно. То есть в момент начала выполнения кода на локации "#array.srtd#" в `$args[0]` уже будет присутствовать значение "$mass", в `$args[1]` — значение "rug", в `$args[2]` — значение "$time_ar".

	При использовании операторов `gosub`, `goto`, `xgoto`, `dynamic` и функций `dyneval`, `func` можно указать до девяти таких аргументов, и все они будут помещены в ячейки массива args с нулевой по восьмую. Однако, поскольку `args` — это всё же массив, вы можете работать с ним, как с обычным массивом, т.е. использовать больше десяти ячеек, назначать текстовые индексы и т.д.

	Отличительной особенностью массива `args` является то, что для каждого отдельного блока кода создаётся свой собственный массив `args`. То есть если вы из локации 1 вызываете локацию 2, то на локации 1 действует собственный массив `args`, а на локации 2 — собственный, и значения в этих массивах не пересекаются.

	Пример:

```qsp
	# локация_1
	args[0]=23
	gosub "локация_2",34
	args[0]
	-

	# локация_2
	args[0]
	-
```
	Запустив этот код, вы увидите, что сначала будет выведено число 34, и только затем 23.

	Более того, если вы сделаете рекурсивный вывод локации самой из себя, то для каждого вызова локации будет создан собственный набор массивов. Таким образом массив `args` является локальным для каждого отдельного вызова блока кода.

	Отдельными блоками кода в QSP считаются:

		* код локаций
		* код действий
		* код, передаваемый `dynamic`/`dyneval`
		* код в гиперссылках

	Для каждой отдельной сессии таких блоков кода плеер будет создавать собственный массив `args`.

### BCOLOR
<!-- [:faq_80_04_bcolor] -->

`BCOLOR` —  содержит цвет текущего фона. Если равна 0, то используется цвет, заданный в настройках программы. Примеры:

```qsp
		! чёрный цвет фона
		bcolor=-16777216
		! красный цвет фона
		bcolor=-16776961
		! белый цвет фона
		bcolor=-1
```
	Поскольку цвет фона кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `rgb`, которой в качестве аргументов передаются три составляющие цвета:
```qsp
		! задаём цвет фона через функцию rgb(red,green,blue)
		! фон синего цвета
		bcolor=rgb(0,0,255)
		! фон жёлтого цвета
		bcolor=rgb(255,255,0)
		! фон оранжевого цвета
		bcolor=rgb(255,130,0)
		! фон голубого цвета
		bcolor=rgb(0,255,255)
		! фон малинового цвета
		bcolor=rgb(255,0,255)
```

### DEBUG
<!-- [:faq_80_04_debug] -->

`DEBUG` —  если значение переменной отлично от нуля, отключается проверка идентификатора игры при загрузке состояния. Иначе при каждом изменении файла игры нельзя будет использовать файлы сохранений, сделанные до изменения игры.

	Совет: во время разработки и тестов игры значение переменной `debug` всегда должно быть отлично от нуля, а когда вы выпускаете финальную версию игры (релиз), нужно выставить переменной `debug` значение 0, чтобы игроки не смогли загрузить файлы сохранений от других игр.

### DISABLESCROLL
<!-- [:faq_80_04_disablescroll] -->

`DISABLESCROLL` —  если значение переменной отлично от нуля, автопрокрутка текста в окнах основного и дополнительного описаний отключается.

`Что это значит`. Предположим, мы вывели на экран большой объём текста, а затем при нажатии на `действие` у нас выводится ещё один фрагментик текста. Если `DISABLESCROLL = 0`, этот фрагментик текста при выводе заставит экран прокрутиться вниз. Если мы не хотим, чтобы экран прокручивался вниз в этом случае, мы присваиваем переменной `DISABLESCROLL` единицу.

Довольно мутное поведение в классическом плеере — при некоторых обстоятельствах текст и так не прокручивается.

	

### DISABLESUBEX
<!-- [:faq_80_04_disablesubex] -->

`DISABLESUBEX` —  если значение переменной отлично от нуля, отключается вычисление подвыражений в строках. Пример:
```qsp
		var=123
		$text='<<var>>'		& ! переменной $text будет присвоена строка '123'
		'string <<var>>'	& ! на экран будет выведена строка 'string 123'
		'<<5+6>>'			& ! на экран будет выведена строка '11'

		disablesubex=1		& ! отключаем вычисление подвыражений
		$text='<<var>>'		& ! переменной $text будет присвоена строка '<<var>>'
		'string <<var>>'	& ! на экран будет выведена строка 'string <<var>>'
		'<<5+6>>'			& ! на экран будет выведена строка '<<5+6>>'
```

В плеерах версии 5.8.0 и выше эта переменная больше не используется.

### FCOLOR
<!-- [:faq_80_04_fcolor] -->

`FCOLOR` —  содержит цвет используемого в данный момент шрифта. Если равна 0, то используется цвет, заданный в настройках программы. Изменение значения переменной меняет цвет всего текста игры, кроме гиперссылок и текста, цвет которого переназначен через HTML. Пример:
```qsp
		! чёрный цвет текста
		fcolor=-16777216
		! красный цвет текста
		fcolor=-16776961
		! белый цвет текста
		fcolor=-1
```
	Поскольку цвет шрифта кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `rgb`, которой в качестве аргументов передаются три составляющие цвета:
```qsp
		! задаём цвет текста через функцию rgb(red,green,blue)
		! текст чёрного цвета
		fcolor=rgb(0,0,0)
		! текст белого цвета
		fcolor=rgb(255,255,255)
		! текст красного цвета
		fcolor=rgb(255,0,0)
		! текст зелёного цвета
		fcolor=rgb(0,255,0)
```
### FSIZE
<!-- [:faq_80_04_fsize] -->

`FSIZE` —  содержит размер используемого в данный момент шрифта. Если равна 0, то используется размер, заданный в настройках программы. Относительно данного значения в HTML-режиме вычисляются размеры шрифтов тега `<font>`. Пример:
```qsp
		fsize=18
```
	Размер шрифта устанавливается для всего текста в игре, кроме текста, размер которого переназначен через HTML.

### LCOLOR
<!-- [:faq_80_04_lcolor] -->

`LCOLOR` —  содержит текущий цвет шрифта гиперссылок. Если равна 0, то используется цвет, заданный в настройках программы. Изменение значения переменной меняет цвет текста всех гиперссылок, кроме тех, цвет которых переназначен через HTML. Пример:
```qsp
		! чёрный цвет гиперссылок
		lcolor=-16777216
		! красный цвет гиперссылок
		lcolor=-16776961
		! белый цвет гиперссылок
		lcolor=-1
```
	Поскольку цвет в QSP кодируется специальным числом, а вычислять это число самостоятельно неудобно, следует пользоваться функцией `rgb`, которой в качестве аргументов передаются три составляющие цвета:
```qsp
		! задаём цвет  гиперссылок через функцию rgb(red,green,blue)
		!  гиперссылки синего цвета
		lcolor=rgb(0,0,255)
		! гиперссылки жёлтого цвета
		lcolor=rgb(255,255,0)
		! гиперссылки оранжевого цвета
		lcolor=rgb(255,130,0)
		! гиперссылки голубого цвета
		lcolor=rgb(0,255,255)
		! гиперссылки малинового цвета
		lcolor=rgb(255,0,255)
```
### NOSAVE
<!-- [:faq_80_04_nosave] -->

`NOSAVE` —  если значение данной переменной отлично от 0, пункт меню плеера "Сохранить состояние игры" игроку становится недоступен, т.е. игрок не может самостоятельно сохранить игру. В то же время на уровне кода QSP продолжает работать оператор `savegame`. Пример:
```qsp
		! отключаем возможность сохранения игры
		nosave=1
		act "Бросить кости":
			cubes=rand(1,6)
			! включаем возможность сохранений обратно
			nosave=0
			delact $selact
		end
```
### RESULT ($RESULT)
<!-- [:faq_80_04_result] -->

`RESULT` —  специфическая системная переменная, предназначенная для получения значения в текущем блоке кода и передачи этого значения функции `func` или `dyneval`. Иными словами, чтобы функции `func` или `dyneval` вернули какое-то значение, необходимо в вызываемом ими блоке кода присвоить значение переменной `result`.

	Например:
```qsp
		$dyneval "
			if args[0] mod 2 = 0:
				$result='чётное число'
			else
				$result='нечётное число'
			end
		",279
```
	Для каждого отдельного блока кода плеером создаётся собственная переменная `result`. То есть если вы из локации 1 вызываете локацию 2, то на локации 1 создаётся собственная переменная `result`, а на локации 2 — собственная, и значения в этих переменных не пересекаются (хотя в плеере 5.7.0. есть небольшая проблема с этим, и использовать переменную `result` рекомендуется только в конце кода локации. В более новых версиях плееров, например в Quest Navigator, эту проблему исправили и `result` можно использовать наравне с `args`). Таким образом переменная `result` является локальной для каждого отдельного вызова блока кода.

	Если при обработке блока кода были установлены и `result`, и `$result`, то предпочтение отдаётся строковому значению.

### USEHTML
<!-- [:faq_80_04_usehtml] -->

`USEHTML` —  если значение данной переменной отлично от нуля, включается режим распознавания HTML. При этом HTML разметку можно использовать в названиях действий, предметов, в тексте, выводимом в окна основного и дополнтельного описаний, а так же в диалоговых окнах, вызываемых оператром `msg` и функцией `$input`.
```qsp
		! включение HTML
		usehtml=1
		! вывод текста с HTML-разметкой
		*pl "<font color=#ff8888>Красный текст.</font>"
```

### Примечания для любопытных

	1. Есть возможность определить любую системную переменную локальной для отдельного блока кода, и тогда эту системную переменную можно использовать как обычную локальную переменную, т.е. она не повлияет на работу плеера. Однако, строго не рекомендуется так делать, чтобы не допускать возможных ошибок.
	2. Как и все прочие переменные в QSP, системные переменные так же являются массивами.
		* Переменные настройки интерфейса позволяют без последствий использовать любые ячейки, кроме нулевой, это не повлияет на работу плеера, однако так всё же не рекомендуется делать, если только это не является каким-то необходимым техническим решением.
		* А вот системные переменные, в которых прописываются названия локаций-обработчиков событий, при последовательном заполнении ячеек дают очень своеобразный эффект. Если вписать подряд в несколько ячеек названия локаций, то последовательно будет вызвана каждая из внесённых в массив локаций. Таким образом можно разгружать от кода локации-обработчики событий. Например, локацию-счётчик:
			```qsp
			$counter[]='playlist'
			$counter[]='animation'
			$counter[]='time.acts'
			```
			При этом очень важно, чтобы названия локаций перечислялись в массиве подряд. Если между названиями локаций окажутся пустые ячейки, то выполнятся лишь те локации, которые находятся в массиве до первой встреченной пустой ячейки:
			```qsp
			! будут выполняться только локации 'playlist' и 'animation'
			$counter[]='playlist'
			$counter[]='animation'
			$counter[]=''
			$counter[]='time.acts'
			```