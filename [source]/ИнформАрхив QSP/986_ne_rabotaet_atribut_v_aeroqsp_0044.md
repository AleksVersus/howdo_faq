## 13.6. В AeroQSP не работает атрибут
<!-- [:faq_13_06] -->

> Примечание Aleks Versus: это статья об устаревшем плеере AeroQSP; данный плеер больше не работает в связи с прекращением поддержки и распространения Adobe Flash Player; статья представлена для ознакомительных целей, так как в ней достаточно полно отражены основные принципы написания игр на QSP.

В: В AeroQSP не работает атрибут.

Например, ''border=1'', ''bgcolor=#557700''.

О:

AeroQSP ориентирован на работу со стилями, поэтому для стилизации различных элементов пользуйтесь возможностями CSS.

Собственную таблицу стилей можно вписать в переменную ''$STYLESHEET''. Вот пример из игры "Один в снегах" от **Lisichk**`и:
```css
	$STYLESHEET='
		.main { 
			position:absolute; 
			height:330px; 
			width:500px; 
			left:0px; 
			text-align:center; 
		} 
		.stat1 { 
			position:absolute;
			height: 600px; 
			width: 210px; 
			top:50;
			right:650;
			text-align:center; 
		} 
		.stat2 { 
			position:absolute;
			height: 600px;
			width: 200px;
			left:750px;
			top:50;
			text-align:center; 
		}
		.roof {
			position:absolute;
			width:400px;
			top:5px;
			left:440px;
			text-align:center;
		}
		.radio {
			position:absolute;
			width:300px;
			height: 50px;
			top:300px;
			left:800px;
			text-align:center;
		}'
```
Стили для отдельного элемента можно прописать в атрибуте ''style'':
```qsp
	*p "<div style='color:#333333;width:350px;border:12;'>Текст внутри блока</div>"
```
Все поддерживаемые свойства перечисленны в сводной справке по AeroQSP [https://qsp.org/misc/aero/help.htm](https://qsp.org/misc/aero/help.htm)

###### 13.6. В AeroQSP не работает атрибут
<!-- [:link_13_06] -->
Смотреть ответ на ютубе: [https://www.youtube.com/watch?v=TCve-b6AQMs&](https://www.youtube.com/watch?v=TCve-b6AQMs&t=18s)
Storm. #2828 10.Май.15 18:33:19: [В классическом плеере и в Quest Navigator`е свойство "border" работает, а в Aero нет.](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=113&prc=25&Itemid=57#p19941)
Вета. #3784 24.Янв.16 14:50:18: [как в аере задать ячейке таблицы цвет? С bgcolor не работает что-то...](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=152&prc=25&Itemid=57#p22645)
DeathSpace. #4212 02.Апр.16 13:52:20: [перевожу игру на AeroQSP но не показывает таблицы который были в классической версии плеера](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=169&prc=25&Itemid=57#p23639)
DeathSpace. #4313 01.Май.16 02:05:59: [Ребят кто знает как в AeroQSP строить таблицы?](https://qsp.org/index.php?option=com_agora&task=topic&id=40&p=173&prc=25&Itemid=57#p23838)
