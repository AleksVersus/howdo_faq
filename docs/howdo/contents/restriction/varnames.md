---
sidebar_position: 3
---

# 22.3. Генерирую переменные с помощью оператора dynamic, и вдруг выходит ошибка 123. Что это, и как с этим бороться?
<!-- [:faq_23_03] -->
**В:** Генерирую переменные с помощью оператора dynamic, и вдруг выходит ошибка 123. Что это, и как с этим бороться?

**О:**

Бороться с этим нельзя, можно только стараться не использовать такое большое количество переменных. QSP не позволяет работать более, чем с пятью десятками переменных с одинаковым хэшем имени. При этом массив считается за одну переменную. Всего можно использовать 12800 различных переменных в игре. Поэтому, когда вы превышаете это число, плеер ругается.
