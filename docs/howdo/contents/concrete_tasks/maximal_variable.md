---
sidebar_position: 7
---

# 20.7. Есть несколько переменных с разными значениями. Как получить имя переменной, в которой находится наибольшее значение?
<!-- [:faq_20_07] -->
**В:** Есть несколько переменных с разными значениями. Как получить имя переменной, в которой находится наибольшее значение?

**О:**
Для примера возьмём несколько переменных и значений:

```qsp
VariableA = 1
VariableB = 2
VariableC = 3
VariableD = 4
```

1. Вносим названия этих переменных и их значения в два разных массива под одним индексом:
	```qsp
	$varname[0]="VariableA" & varvalue[0]=VariableA
	$varname[1]="VariableB" & varvalue[1]=VariableB
	$varname[2]="VariableC" & varvalue[2]=VariableC
	$varname[3]="VariableD" & varvalue[3]=VariableВ
	```
2. Теперь определяем максимальное значение в массиве varvalue:
	```qsp
	varmax=max('varvalue')
	```
3. Осталось определить индекс элемента с этим значением:
	```qsp
	indexMax=arrpos('varvalue',varmax)
	```
4. Имя переменной получить уже несложно:
	```qsp
	*pl "Максимальное значение в переменной "+$varname[indexMax]
	```

Можно написать функцию, которая будет возвращать название переменной с максимальным значением:

```qsp
!#maxVar
! $args[0] — $args[18] — названия переменных
! массивы для временного хранения названий переменных и их значений:
local $varname, varvalue
! 1
loop local i=0 while $args[i]<>'' step i+=1:
	dynamic "$varname[] = '<<$args[i]>>' & varvalue[] = <<$args[i]>>"
end
! 2
local max_ = max('varvalue')
! 3
local index_=arrpos('varvalue',max_)
! 4
$result=$varname[index_]
```

Вызов функции:

```qsp
@maxVar('VariableA','VariableB','VariableC','VariableD')
```

Поскольку для работы данной функции в любом случае требуется цикл, можно несколько изменить алгоритм:

```qsp
!#varMax
local $max_ = 'args[19]'
loop local i=0 while $args[i]<>'' step i+=1:
	$max_ = $dyneval("if <<$args[i]>> > <<$max_>>:
		$result = '<<$args[i]>>'
	else
		$result = '<<$max_>>'
	end")
end
$result = $max_
```
Или, без использования `dyneval`:
```qsp
local max_, cur_
$result = $args[0]
loop local i = 0 while $args[i] <> '' step i += 1:
	cur_ = arritem($args[i], 0)
	if cur_ > max_:
		$result = $args[i]
		max_ = cur_
	end
end
```