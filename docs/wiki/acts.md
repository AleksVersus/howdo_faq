---
sidebar_position: 5
---
[Назад: Диалоговое окно](../text_print/msgbox.md)

# Действия

"Менюшные" игры с точки зрения геймплея, как правило, предоставляют игроку на выбор несколько вариантов действий, которыми он может воспользоваться. Выбрав действие, игрок двигает игру дальше по сюжету, и волне возможно, главный герой при этом совершает описанное действие: съедает кусок пирога, или проникает в чужой сад.

Обычно действия отделены от основного описания и представляют собой ряд кликабельных кнопок. В **QSP** для размещения действий есть отдельное окно, оно так и называется **Окно действий**, или **Список действий** (в плеере просто **Действия**).

С этим окном, в зависимости от нужд вашей игры, вы можете проделывать разные манипуляции. Вы можете:

* Отключать и включать **Окно действий** по своему желанию
* Добавлять действия в **Окно действий**
* Удалять действия из **Окна действий**
* Полностью очищать **Окно действий**

В названиях действий не важен регистр букв, то есть "Пойти" и "поЙти" - одно и то же действие.

При создании действия, весь код, относящийся к действию, "прикрепляется" к этому действию, но не выполняется. Этот код будет выполнен только тогда, когда игрок нажмёт на действие (щёлкнет по нему мышью).

## Команды для работы с Окном действий

### Включение и выключение Окна действий

*  `SHOWACTS [#выражение]` - если значение выражения отлично от 0, то показывает **Список действий**, иначе скрывает его. Пример:
    ``` qsp
  showacts 0 & ! скрываем Окно действий
      showacts 1 & ! выводим Окно действий на экран
    
```
 Для удобства чтения кода можно заранее определить переменные `on` и `off` с соответствующими значениями:
    ``` qsp
  on,off = 1,0
      showacts on & ! включаем Окно действий
      showacts off & ! выключаем Окно действий
    
```


### Команды для управления действиями

*  `ACT` — данная команда добавляет в **Окно действий** кнопку действия.
    * У этой команды есть две формы записи:
        * Однострочная форма записи:
    ``` qsp
ACT [$название], [$путь к файлу изображения]: {оператор 1} & {оператор 2} & {оператор 3}
            
```
 Здесь `[$название]` — это надпись (название), которая будет выводиться на кнопке действия, а `[$путь к файлу изображения]` — путь к файлу изображения, которое так же будет выводиться на кнопке действия перед названием.
            * И команда `ACT` и название, и операторы после двоеточия при такой форме записи должны быть записаны в одну строку.
            * Когда игрок нажмёт кнопку действия с указанным названием, будут выполнены перечисленные операторы.
            * Параметр `[$путь к файлу изображения]` может отсутствовать, при этом действие добавится без изображения.
        * Многострочная форма записи:
    ``` qsp
      ACT [$название], [$путь к файлу изображения]:
                    {оператор 1}
                    {оператор 2}
                    {оператор 3}
                  END
            
```
 Здесь точно так же будет создано действие с названием `[$название]`, перед названием будет выводиться изображение, путь к которому мы указали с помощью параметра `[$путь к файлу изображения]`, а когда игрок нажмёт на действие, будут выполнены перечисленные операторы. Обратите внимание:
            * При многострочной форме записи после двоеточия в той же строке, где находится команда `ACT` не должно быть ничего.
            * Все операторы записываются со следующей строки после двоеточия
            * Многострочная форма обязательно должна завершаться командой `END` или `END ACT`.
    * Примеры:
    ``` qsp
    ! действие в однострочной форме записи
            act "Сорвать с берёзы яблоко": яблоко+=1 & *pl "Вы сорвали яблоко, спелое белое."

            ! действие в многострочной форме записи, с изображением
            act "Сорвать арбуз с куста","img/watermelon.png":
              арбуз+=1
              *pl "Вы сорвали арбуз с куста"
            end
        
```

*  `DELACT [$название]` - удаляет действие с указанным названием из списка действий на локации. Если действие с указанным названием не существует, ошибки не будет, плеер просто проигнорирует команду. Примеры:
    ``` qsp
    ! удаляем действие с конкретным названием
        delact 'Идти вперед'

        ! удаляем выделенное действие
        delact $selact
    
```


### Команды очистки Окна действий

*  `CLA` - очистка списка текущих действий (удаление всех действий из окна действий). Пример:
    ``` qsp
  ! это действие при нажатии выведет текст
      act "Действие 1":
        *pl "Ехал Грека Через Реку"
      end
      ! это действие при нажатии выведет текст и удалится
      act "Действие 2":
        *pl "Видит Грека В Реке Рак"
        delact $selact
      end
      ! это действие при нажатии удалит все действия
      act "Очистить окно действий":
        cla
      end
    
```

*  `CLS` - эквивалентно конструкции "`CLEAR & *CLEAR & CLA & CMDCLEAR`", т.е. очищает все окна кроме списка предметов.

### Функции для обработки действий

*  `$CURACTS` - данная функция возвращает текущий список действий в виде QSP-кода.
    *  Действия сохраняются в виде набора операторов `ACT` с ответствующими параметрами и операциями.
    *  Записав возвращённое функцией значение в переменную, можно восстановить действия с помощью оператора **[DYNAMIC](../programming/dynamical.md)**. Пример:
    ``` qsp
    ! записываем текущие действия в переменную
            $actlist=$curacts
            ! восстанавливаем действия из переменной
            dynamic $actlist
        
```

*  `$SELACT` - данная функция возвращает название выделенного действия в любом месте игры. Пример:
    ``` qsp
    act "Съесть яблоко":
          *pl "Это было очень вкусное яблоко. Жаль, что червивое."
          здоровье=здоровье+100
          delact $selact
        end
    
```


## Событие "Выделение действия"

Когда вы наводите курсор мыши на действие, в классическом плеере это действие подсвечивается голубым цветом, и это означает, что действие выделено. При этом функция `$SELACT`, вызванная в любом месте игры, будет возвращать название такого выделенного действия.

**Выделение действия** — это событие, к которому вы можете привязать автоматическое выполнение кода. Делается это с помощью системной переменной `$ONACTSEL`:

* `$ONACTSEL` — системная переменная, куда можно прописать название локации, код на которой будет выполняться при очередном выделении действия.

Более подробная информация в разделе ["Служебные локации"](../programming/service_locations.md).

## Локальные переменные в действии

Каждое действие в **QSP** вляется отдельным блоком кода, и потому для него можно назначить локальные переменные. Таким образом можно проводить различные расчёты внутри действия, не затрагивая переменные на локации.

``` qsp
яблоки=245
act "Наколдовать яблоки":
  local яблоки
  яблоки=val($input('Сколько вам нужно яблок?'))
  яблоки_у_Миши+=яблоки
  *pl "Наколдовано яблок: <<яблоки>>"
end
act "Сколько яблок на локации?":
  ! это действие работает с глобальной переменной
  *pl "Яблок на локации: <<яблоки>>"
end
```

## Ограничения

* Максимальное количество одновременно видимых действий на локации — 50. То есть игрок не сможет увидеть больше пятидесяти действий на экране, сколько бы вы их не добавляли.
* Если в списке действий уже есть действие с указанным названием, то новое действие не создаётся, и не заменяет собой уже существующее, плеер просто игнорирует команду **act**. Таким образом нельзя вывести действия с одинаковыми названиями. Пример:
    ``` qsp
    act "Действие 1": *pl "Старое действие."
        act "Действие 1": *pl "Новое действие."
    
```


————————————————————————

[Вперёд: Переходы](../goto.md)