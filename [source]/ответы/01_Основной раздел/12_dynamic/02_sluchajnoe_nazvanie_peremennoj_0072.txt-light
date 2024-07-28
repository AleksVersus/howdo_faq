## 12.2. Можно ли сделать переменную с рандомным (случайным) названием?
<!-- [:faq_12_02] -->
В: Можно ли сделать переменную с рандомным (случайным) названием?

О:
Да конечно, можно. Используйте для этого оператор `dynamic`.

Например, можно забить в массив уже готовые названия, или части названия:
```qsp
$name_var[0]="blue"
$name_var[1]="violet"
$name_var[2]="red"
$name_var[3]="orange"
$name_var[4]="yello"
$name_var[5]="green"

dynamic "<<$name_var[rand(0,5)]>>_<<$name_var[rand(0,5)]>>=999"
```

Или набрать название из случайных символов:
```qsp
$letter[0]="A"
$letter[1]="B"
$letter[2]="C"
$letter[3]="D"
$letter[4]="E"
$letter[5]="F"

loop local i=0 while i<4 step i+=1:
	$name_var+=$letter[rand(0,5)]
end

dynamic "<<$name_var>>=984
*pl 'Имя переменной: <<$name_var>>'
*pl 'Значение: '+<<$name_var>>"
```
