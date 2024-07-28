---
sidebar_position: 3
---

# Создайте запись в блоге

Docusaurus создает **страницу для каждой записи в блоге**, а также **страницу индекса блога**, **систему тегов**, **RSS**-канал...

## Создайте свою первую запись

Создайте файл по адресу `blog/2021-02-28-greetings.md`:

```md title="blog/2021-02-28-greetings.md"
---
slug: greetings
title: Greetings!
authors:
  - name: Joel Marcey
    title: Co-creator of Docusaurus 1
    url: https://github.com/JoelMarcey
    image_url: https://github.com/JoelMarcey.png
  - name: Sébastien Lorber
    title: Docusaurus maintainer
    url: https://sebastienlorber.com
    image_url: https://github.com/slorber.png
tags: [greetings]
---

Congratulations, you have made your first post!

Feel free to play around and edit this post as much as you like.
```

Новая запись в блоге теперь доступна по адресу [http://localhost:3000/blog/greetings](http://localhost:3000/blog/greetings).
