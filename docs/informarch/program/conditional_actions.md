---
sidebar_position: 306
---

# Действие по условию
<!-- [:informarch_ifacts] -->

Иногда требуется сделать, чтобы действие "появлялось" только при выполнении определенного условия.

Делается это так.

1. Все действия, которые могут быть "отключены" по каким-либо условиям, переносим в область "Выполнить при посещении"
2. В конце каждого действия, в котором есть влияние на любое из этих условий(!), ставим "GOTO $CURLOC".
3. Помещаем действия внутрь соотв. блоков IF, с проверками на условия.
4. При написании кода "Выполнить при посещении" локации учитываем, что код будет выполняться более одного раза.

Также внутрь блока IF удобно внести часть описания, относящуюся к показываемому действию.

## Пример

```qsp
'Вы находитесь в пустой комнате.'
IF ключ=0:
    'На полу лежит ключ.'
    ACT 'Взять ключ':
        ключ = 1
        ADDOBJ 'ключ'
        GOTO $CURLOC
    END
END
```

## Второй пример

Допустим, в игре можно что-то покупать за деньги. Количество денег хранится в переменной "деньги". Когда денег становится мало, нам нужно, чтобы игроку были недоступны некоторые покупки. Если не выполнять проверку, то количество денег игрока уйдет в минус, и покупать можно будет бесконечно. Проверку можно реализовать двумя способами, на усмотрение автора.

Первый - действие по условию, как в предыдущем примере. Если условие не выполняется, то действие не показывается вообще. Игрок видит в списке действий только те вещи, на которые у него хватает денег.

```qsp
IF деньги >= 100:
    ACT 'Купить плащ (100)':
        деньги = деньги - 100
        PL 'Вы купили плащ за 100 монет.'
        ADDOBJ 'плащ'
        GOTO $CURLOC
    END
END
IF деньги >= 10:
    ACT 'Купить хлеб (10)':
        деньги = деньги - 10
        PL 'Вы купили хлеб за 10 монет.'
        хлеб = хлеб + 1
        GOTO $CURLOC
    END
END
IF деньги >= 200:
    ACT 'Купить меч (200)':
        деньги = деньги - 200
        PL 'Вы купили меч за 200 монет.'
        ADDOBJ 'меч'
        GOTO $CURLOC
    END
END
```

Второй способ - условие внутри действия. При выполнении действия выполняется проверка, и если денег недостаточно, выдается соответствующее сообщение. Игрок видит весь список вещей, но купить может только те, на которые хватает денег.

```qsp
ACT 'Купить плащ (100)':
    IF деньги >= 100:
        деньги = деньги - 100
        PL 'Вы купили плащ за 100 монет.'
        ADDOBJ 'плащ'
        GOTO $CURLOC
    ELSE
        PL 'У вас нехватает денег.'
    END
END
ACT 'Купить хлеб (10)':
    IF деньги >= 10:
        деньги = деньги - 10
        PL 'Вы купили хлеб за 10 монет.'
        хлеб = хлеб + 1
        GOTO $CURLOC
    ELSE
        PL 'У вас нехватает денег.'
    END
END
ACT 'Купить меч (200)':
    IF деньги >= 200:
        деньги = деньги - 200
        PL 'Вы купили меч за 200 монет.'
        ADDOBJ 'меч'
        GOTO $CURLOC
    ELSE
        PL 'У вас нехватает денег.'
    END
END
```

## Третий пример

Допустим, в игре для продвижения по сюжету нам нужно что-то узнать. Кто-то рассказывает нам, что в библиотеке замка есть потайной ход. Когда мы это узнали, то при посещении библиотеки у нас появится соответствующее действие. Пока игрок не выяснил про потайной ход, действие скрыто.

```qsp
! Локация "Слепой старец"
'Старец усмехнулся. - Они лишили меня зрения, но память осталась при мне. Я расскажу тебе, как добраться до сокровищницы. В библиотеке есть потайной ход: загляни в книгу, четырнадцатую от окна на нижней полке.'
! Меняем состояние игры - отмечаем, что игрок узнал секрет.
потайной_ход = 1

! Локация "Библиотека"
IF потайной_ход = 1:
    ACT 'Заглянуть в четырнадцатую книгу':
        GOTO 'Потайной ход'
    END
END
```

Автор: **Nex**
26.Июл.11 06:51:46

Оригинал в теме: [Действие по условию](https://qsp.org/index.php?option=com_agora&task=topic&id=348&Itemid=57)

