---
sidebar_position: 1
---

# Управление версиями документов

Docusaurus может управлять несколькими версиями ваших документов.

## Создание версии документов

Выпуск версии 1.0 вашего проекта:

```bash
npm run docusaurus docs:version 1.0
```

Папка `docs` копируется в `versioned_docs/version-1.0` и создается `versions.json`.

Теперь у ваших документов есть 2 версии:

- `1.0` по адресу `http://localhost:3000/docs/` для документов версии 1.0
- `current` по адресу `http://localhost:3000/docs/next/` для **будущих, невыпущенных документов**

## Добавить раскрывающийся список версий

Чтобы легко перемещаться между версиями, добавьте раскрывающийся список версий.

Измените файл `docusaurus.config.js`:

```js title="docusaurus.config.js"
export default {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'docsVersionDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

Раскрывающийся список версий документов отображается на панели навигации:

![Docs Version Dropdown](./img/docsVersionDropdown.png)

## Обновить существующую версию

Возможно редактировать версионные документы в соответствующей папке:

- `versioned_docs/version-1.0/hello.md` обновляет `http://localhost:3000/docs/hello`
- `docs/hello.md` обновляет `http://localhost:3000/docs/next/hello`
