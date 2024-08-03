# 20.9. Как сделать вытягивание случайных карт из колоды?
<!-- [:faq_20_09] -->
В: Как сделать вытягивание случайных карт из колоды? Карты вытягиваются несколько раз, но они не должны повторяться.

О:
В общем виде эта задача решается так:

1. Записываем данные в массив
2. Тем или иным способом (например, случайным образом) получаем номер ячейки этого массива
3. Используем данные из этой ячейки (например, выводим на экран, или помещаем в другой массив/переменную)
4. Уничтожаем ячейку, чтобы больше не получать из неё данные
5. При необходимости повторяем.

На основе этого общего алгоритма составим алгоритм под конкретную задачу. Будем вытягивать по шесть карт из колоды, пока карты не кончатся.

Поскольку все карты в колоде разные, можно присвоить каждой из них номер, и записать эти номера в массив:
```qsp
deck[0] = 1
deck[1] = 2
deck[2] = 3
!...
deck[51] = 52
deck[52] = 53
deck[53] = 54
```
Можно описать каждую карту строкой текста:
```qsp
$deck[0] = 'двойка треф'
$deck[1] = 'тройка треф'
$deck[2] = 'четвёрка треф'
!...
$deck[51] = "туз бубей"
$deck[52] = "джокер красный"
$deck[53] = "джокер чёрный"
```
Выбирайте способ, который вам будет удобен.

Алгоритм, который мы будем использовать далее, необходимо изменить под ваши конкретные нужды. В данном случае мы напишем действие, которое будет сдавать по шесть карт:
```qsp
! открываем действие
act "Сдать шесть карт":
	! Если колоду ещё не разобрали (условие 1)
	if arrsize('deck') > 0:
		! организуем цикл
		loop local i=0 while i<6 step i+=1:
		! пока счётчик не достиг 6
			! выбираем случайное число от 0
			! до индекса последнего элемента массива deck
			index=rand(0,arrsize('deck')-1)
			! запоминаем карту в очередном элементе массива hand
			hand[]=deck[index]
			! можем вывести на экран
			*p $str(deck[index])+','
			! удаляем карту из колоды
			! (элемент из массива)
			killvar 'deck',index
		end
		! добавляем перевод строки
		*pl
	else
	! если колоду уже разобрали
		*pl "Колода разобрана"
	! закрываем условие 1
	end
! закрываем действие
end
```
Данное решение можно применять для других задач. Например, в массиве есть несколько чисел, и их необходимо вывести в порядке от большего к меньшему:
```qsp
! массив
deck[0]=4
deck[1]=3
deck[2]=2
deck[3]=3
deck[4]=1
deck[5]=4
! чтобы не затирать исходный массив,
! копируем значения в другой, временный, массив
copyarr 'deck_temp','deck'
! вновь организуем цикл
loop while arrsize('deck_temp')>0: 
! если размер временного массива больше нуля
	! получаем максимальное значение
	maxVar=max('deck_temp')
	! определяем, в какой ячейке находится это значение
	index=arrpos('deck_temp',maxVar)
	! можно вывести на экран
	*pl deck_temp[index]
	! теперь удаляем элемент из массива
	killvar 'deck_temp',index
! закрываем цикла
end
```
В упрощённом виде алгоритм, выбрасывающий случайные карты из колоды (с первой по последнюю) можно записать так:
```qsp
!$deck[0]='двойка треф'
!$deck[1]='тройка треф'
!$deck[2]='четвёрка треф'
loop local i=0 while arrsize('$deck') > 0:
	i=rand(0,arrsize('$deck')-1)
	*pl $deck[i]
	killvar '$deck',i
end
```
Посмотрите так же предложенные решения по [ссылкам](#link_20_09).