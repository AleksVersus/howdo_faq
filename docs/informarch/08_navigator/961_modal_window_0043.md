# 22.11. Модальное окошко с вариантами выбора
<!-- [:faq_22_11] -->

:::danger[**Эта статья устарела!**]
Эта статья устарела. Новый плеер с поддержкой HTML - [qSpider](../../articles/04_qspider_0004).
:::

В Quest Navigator Вы можете самостоятельно написать такое окошко, даже не прибегая к помощи JavaScript.

Далее следует готовое решение от **evp** с комментариями от **Aleks Versus**.

В игре:
```qsp
! не забываем включать html
USEHTML = 1
! следующая строка заставит плеер обратиться к элементу
!  с id openModal когда игрок щёлкнет по ссылке
*nl'<a href="#openModal">Открыть диалог</a>'
! в переменную $life в виде текста вносим код, который
! должен выполняться при выборе варианта "Жизнь"
$life = { 
	*pl 'код, выполняемый при выборе варианта "Жизнь"'
}
! соответственно в переменную $money — код, который
! должен выполняться при выборе варианта "Деньги"
$money = { 
	*pl 'код, выполняемый при выборе варианта "Кошелёк"'
} 
! выводим на экран "окошко", а вернее блок, стилизованный под окошко, с двумя кнопками
! общий блок/затенение
*p '<div class="modalDialog" id="openModal">'
	! окошко
	*p '<div>' 
		*p '<p>Жизнь или кошелёк?</p>' 
		*p '<button style="float: left;"><a href="EXEC: dynamic $life">Жизнь</a></button>' 
		*p '<button style="float: right;"><a href="EXEC: dynamic $money">Кошелёк</a></button>' 
	*p '</div>' 
*pl '</div>'
```
В game.css вашего шаблона:
```css
/*
	данный стиль описывает внешний вид общего блока, играющего в т.ч. роль затенения
	(обратите внимание, на какую область в вашем шаблоне распространяется затенение)
 */
.modalDialog { 
	position: fixed; 
	top: 0;    right: 0;    bottom: 0; left: 0; 
	background: hsla(0,0%,0%,0.8); 
	z-index: 50; /* выводится одним из верхних слоёв */
	opacity: 0; /* видимость на нуле, чтобы игрок не видел содержимое */
	-webkit-transition: opacity 400ms ease-in; /* обеспечивает плавное появление */
	pointer-events: none; /* скрывает блок от курсора мыши */
} 
/* 
	псевдокласс :target применяется к тому элементу
	к которому обратился браузер/плеер по нажатию на ссылку (по id)
*/
.modalDialog:target { 
	opacity: 1; /* видимость повышается до 100% */
	pointer-events: auto; /* с блоком снова может работать мышь */
} 
/* стилизация дочернего блока, т.е. непосредственно окошка */
.modalDialog > div { 
	width: 400px; 
	position: relative; 
	margin: 10% auto; 
	padding: 5px 20px 13px 20px; 
	border-radius: 10px; 
	background: #fff; 
	background: -webkit-linear-gradient(#fff, #b8ecfb); 
}
```