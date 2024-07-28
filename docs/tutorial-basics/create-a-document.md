---
sidebar_position: 2
---

# Создать документ

Документы — это **группы страниц**, связанные посредством:

- **боковой панели**
- **предыдущей/следующей навигации**
- **управления версиями**

## Создайте свой первый документ

Создайте файл Markdown в `docs/hello.md`:

```md title="docs/hello.md"
# Hello

This is my **first Docusaurus document**!
```

Новый документ теперь доступен по адресу [http://localhost:3000/docs/hello](http://localhost:3000/docs/hello).

## Настройка боковой панели

Docusaurus автоматически **создает боковую панель** из папки `docs`.

Добавьте метаданные для настройки метки и положения боковой панели:

```md title="docs/hello.md" {1-4}
---
sidebar_label: 'Hi!'
sidebar_position: 3
---

# Hello

This is my **first Docusaurus document**!
```

Также можно создать боковую панель явно в `sidebars.js`:

```js title="sidebars.js"
export default {
  tutorialSidebar: [
    'intro',
    // highlight-next-line
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
};
```
