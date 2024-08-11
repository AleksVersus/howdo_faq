---
sidebar_position: 2
---

# 6.2. Как запустить две звуковые дорожки?
<!-- [:faq_06_02] -->

**В:** Как запустить две звуковые дорожки?

**О:**
QSP поддерживает одновременное воспроизведение до 32-х звуковых файлов. Это значит, что для запуска двух звуковых файлов достаточно просто написать по команде на каждый:

```qsp
PLAY "путь к файлу/один музыкальный файл.mp3"
PLAY "путь к файлу/другой музыкальный файл.mp3"
```

Однако таким образом вы не сможете запустить две одинаковые звуковые дорожки. Повторный вызов оператора `PLAY` с тем же звуковым файлом, может лишь изменить громкость звучания:

```qsp
PLAY "путь к файлу/музыка.mp3" & ! запустили со 100% громкости
wait 1000 & ! подождали секунду
PLAY "путь к файлу/музыка.mp3",50 & ! снизили громкость до 50%
```