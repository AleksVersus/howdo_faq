---
sidebar_position: 4
---

# 7.4. Как сделать гиперссылки без подчёркивания?
<!-- [:faq_07_04] -->
**В:** Как сделать гиперссылки без подчёркивания?

**О:**
В классическом плеере подчёркивание отключается присвоением гиперссылке класса "plain":

```qsp
*pl "На берёзе созрело несколько <a href='exec:яблоко=яблоко+1 & addobj ""Яблоко""' class='plain'>яблок</a>."
```

В qSpider вы можете прописать собственные классы для ссылок, в т.ч. и сделать все ссылки без подчёркивания, с помощью подключаемых CSS-файлов.