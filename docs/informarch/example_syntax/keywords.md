# Keywords: functions, statements, sysvars and vars

## string_functions

```qsp
! Строковые функции: допустимы $func(...) и func(...);
! #func(...) и %func(...) — ошибка типа
$curacts & curacts & #curacts & %curacts

$curloc & curloc & #curloc & %curloc

$curobjs & curobjs & #curobjs & %curobjs

$desc($curloc)
desc($curloc)
#desc($curloc)
%desc($curloc)

$getobj(12) & getobj(12) & #getobj(12) & %getobj(12)

$input('Enter the text!')
input('Enter the text!')
#input('Enter the text!')
%input('Enter the text!')

$lcase('low case THIS TEXT')
lcase('low case THIS TEXT')
#lcase('low case THIS TEXT')
%lcase('low case THIS TEXT')

$maintxt & maintxt & #maintxt & %maintxt

$mid('cut THIS TEXT', 5, 4)
mid('cut THIS TEXT', 5, 4)
#mid('cut THIS TEXT', 5, 4)
%mid('cut THIS TEXT', 5, 4)

$qspver & qspver & #qspver & %qspver

$replace($string, $old, $new, 1)
replace($string, $old, $new, 1)
#replace($string, $old, $new, 1)
%replace($string, $old, $new, 1)

$selact & selact & #selact & %selact

$selobj & selobj & #selobj & %selobj

$stattxt & stattxt & #stattxt & %stattxt

$str(123) & str(123) & #str(123) & %str(123)

$strfind($string, $regexp, 0)
strfind($string, $regexp, 0)
#strfind($string, $regexp, 0)
%strfind($string, $regexp, 0)

$trim('   TRIM this TEXT    ')
trim('   TRIM this TEXT    ')
#trim('   TRIM this TEXT    ')
%trim('   TRIM this TEXT    ')

$ucase('upper case THIS TEXT')
ucase('upper case THIS TEXT')
#ucase('upper case THIS TEXT')
%ucase('upper case THIS TEXT')

$user_text & user_text & #user_text & %user_text
$usrtxt & usrtxt & #usrtxt & %usrtxt

$arrtype($array_name, 0)
arrtype($array_name, 0)
#arrtype($array_name, 0)
%arrtype($array_name, 0)

$arrkey($array_name, 0)
arrkey($array_name, 0)
#arrkey($array_name, 0)
%arrkey($array_name, 0)
```


## mixtype_functions

```qsp
! Функции любого типа (iif, dyneval, func, max, min, arritem):
! допустимы ВСЕ четыре формы — func, #func, $func, %func
$dyneval('$result = "string"')
%dyneval('%result = ["tuple", 1]')
dyneval('result = 123')
#dyneval('#result = 123')

$func('foo', 'str')
%func('foo', 'tpl')
func('foo', 'num')
#func('foo', 'num')

$iif(x mod 2 = 0, 'even', 'not even')
%iif(x, [1, 2], [2, 3])
iif(x mod 2 = 0, 1, 0)
#iif(x mod 2 = 0, 1, 0)

$max('aa', 'ab', 'abz')			& $max('$a')
%max([1, 2], [], [999, 1, 23])	& %max('%a')
max(12, 34, 56)				& max('a')
#max(12, 34, 56)			& #max('$a')

$min('aa', 'ab', 'abz')			& $min('$a')
%min([1, 2], [], [999, 1, 23])	& %min('%a')
min(12, 34, 56)				& min('a')
#min(12, 34, 56)			& #min('$a')

$arritem('$array_name', 99)
%arritem('%array_name', 45)
arritem('array_name', 5)
#arritem('array_name', 5)
```

## numeric_functions

```qsp
! Числовые функции: допустимы func(...) и #func(...);
! $func(...) и %func(...) — ошибка типа
arrcomp($array_name,$regexp,0)		& !@ valid (универсальный)
#arrcomp($array_name,$regexp,0)		& !@ valid (числовой)
$arrcomp($array_name,$regexp,0)		& !@ invalid
%arrcomp($array_name,$regexp,0)		& !@ invalid

arrpos($array_name,value,0)			& !@ valid
#arrpos($array_name,value,0)		& !@ valid
$arrpos($array_name,value,0)		& !@ invalid
%arrpos($array_name,value,0)		& !@ invalid

arrsize($array_name)			& !@ valid
#arrsize($array_name)			& !@ valid
$arrsize($array_name)			& !@ invalid
%arrsize($array_name)			& !@ invalid

countobj & #countobj			& !@ valid
$countobj & %countobj			& !@ invalid

instr($string,$substr,0)		& !@ valid
#instr($string,$substr,0)		& !@ valid
$instr($string,$substr,0)		& !@ invalid
%instr($string,$substr,0)		& !@ invalid

isnum($string)				& !@ valid
#isnum($string)				& !@ valid
$isnum($string)				& !@ invalid
%isnum($string)				& !@ invalid

isplay('путь к файлу')			& !@ valid
#isplay('путь к файлу')			& !@ valid
$isplay('путь к файлу')			& !@ invalid
%isplay('путь к файлу')			& !@ invalid

len($string)				& !@ valid
#len($string)				& !@ valid
$len($string)				& !@ invalid
%len($string)				& !@ invalid

msecscount & #msecscount		& !@ valid
$msecscount & %msecscount		& !@ invalid

rand(0,1) & #rand(0,1)			& !@ valid
$rand(0,1) & %rand(0,1)			& !@ invalid

rgb(red,green,blue)			& !@ valid
#rgb(red,green,blue)			& !@ valid
$rgb(red,green,blue)			& !@ invalid
%rgb(red,green,blue)			& !@ invalid

rnd & #rnd				& !@ valid
$rnd & %rnd				& !@ invalid

strcomp($string,$regexp)		& !@ valid
#strcomp($string,$regexp)		& !@ valid
$strcomp($string,$regexp)		& !@ invalid
%strcomp($string,$regexp)		& !@ invalid

strpos($string,$regexp,1)		& !@ valid
#strpos($string,$regexp,1)		& !@ valid
$strpos($string,$regexp,1)		& !@ invalid
%strpos($string,$regexp,1)		& !@ invalid

val($string) & #val($string)		& !@ valid
$val($string) & %val($string)		& !@ invalid

loc('label') & #loc('label')		& !@ valid
$loc('label') & %loc('label')		& !@ invalid

obj('item') & #obj('item')		& !@ valid
$obj('item') & %obj('item')		& !@ invalid
```

## tuple_functions

```qsp
! Кортежная функция arrpack: допустимы %arrpack(...) и arrpack(...);
! $arrpack(...) и #arrpack(...) — ошибка типа
%arrpack('$array_name',0,arrsize('$array_name'))	& !@ valid (кортежный)
arrpack('$array_name',0,arrsize('$array_name'))		& !@ valid (универсальный)
$arrpack('$array_name',0,arrsize('$array_name'))	& !@ invalid
#arrpack('$array_name',0,arrsize('$array_name'))	& !@ invalid
```

## sign `?`

```qsp
!example of location-function
if 0:
	elseif $args[0] = 'tpl': %result = ["tuple", 1]
	elseif $args[0] = 'str': $result = "string"
	elseif $args[0] = 'num': #result = 123
	else: result = ?
end
```

## main_and_stat_statements
```qsp

pl 'text' & *pl 'text'
nl 'text' & *nl 'text'
p ' text' & *p ' text'

clr & *clr
clear & *clear
```

## other_statements
```qsp

addobj 'Название предмета','путь к файлу картинки/picture.jpg',позиция
modobj 'название предмета', 'описание предмета', 'путь/к/изображению.png'
resetobj 'название предмета'

cla

close 'путь к звуковому файлу.mp3'
close
close all

cls

cmdclear & cmdclr

copyarr '$новый_массив','$старый_массив'

delact '$название действия'

delobj 'Название предмета'

dynamic $code
dynamic

exit

freelib

gosub 'название локации' & gs 'kdkkdkdkd'
gosub & gs & ! gosub без аргумента

goto 'location name' & gt 'dlldldlslsala'
goto & gt & ! goto без аргумента

inclib 'path to file'

jump 'МЕТКА'
jump & ! без аргумента

killall

killobj 0

killvar 'название массива', индекс_элемента

menu 'название массива'

msg 'текст сообщения'

opengame 'path to file'

openqst 'path to file'

play 'путь к звуковому файлу.mp3'

refint

savegame 'path to file'

scanstr '$массив', 'строка для разбора', 'регулярка', 0

settimer 500

setvar 'название_массива', значение, 0
insvar $a, 'x', 0

showacts 0
showinput 0
showobjs 0
showstat 0

sortarr '$сортируемый_массив',0

unpackarr 'название_массива', %кортеж, 0, arrsize('название_массива')

unselect & unsel

view 'путь к картинке.png'

wait 1000

xgoto 'location name' & xgt 'jfjfjfjjfjfjf'
xgoto & xgt & ! xgoto без аргумента
```

## definite_var_statements

```qsp
let num = 1234

set $string = 'dkkdkkdkd'

local a, b, $s = 1, 2, 'f333f'
```

## controls_statements

```qsp
act 'Название действия', 'путь к картинке.png':
	!@ Код действия
end комментарий после end & *pl 'other operator'

act 'Название действия', 'путь к картинке.png':
	!@ Код действия
end act комментарий после end & *pl 'other operator'

act 'Название действия': однострочное = действие

loop local i=0 while i<10 step i+=1:
	!@ Тело цикла
end комментарий после end & *pl 'other operator'

loop local i=0 while i<10 step i+=1:
	!@ Тело цикла
end loop комментарий после end & *pl 'other operator'

loop local i=0 while i<10 step i+=1: *pl '> [<<i>>]'

if условие_выполнено:
!@ Если условие выполнено
	!@ Код, который выполняется, если условие выполнено
elseif условие_2_выполнено:
	!@ ветвление
else:
!@ Если условие не выполнено
	!@ Код, который выполняется, если условие не выполнено
end комментарий после end & *pl 'other operator'

if условие_выполнено:
	!@ Если условие выполнено
	!@ Код, который выполняется, если условие не выполнено
end if комментарий после end & *pl 'other operator'

if a = b elseif z = v: kdkdkd else: dkkdkdk
```
