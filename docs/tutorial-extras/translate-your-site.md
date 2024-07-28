---
sidebar_position: 2
---

# Переведите свой сайт

Давайте переведем `docs/intro.md` на французский.

## Настройте i18n

Измените `docusaurus.config.js`, чтобы добавить поддержку локали `fr`:

```js title="docusaurus.config.js"
export default {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
};
```

## Перевести документ

Скопируйте файл `docs/intro.md` в папку `i18n/fr`:

```bash
mkdir -p i18n/fr/docusaurus-plugin-content-docs/current/

cp docs/intro.md i18n/fr/docusaurus-plugin-content-docs/current/intro.md
```

Переведите `i18n/fr/docusaurus-plugin-content-docs/current/intro.md` на французский.

## Запустите свой локализованный сайт

Запустите свой сайт на французском языке:

```bash
npm run start -- --locale fr
```

Ваш локализованный сайт доступен по адресу [http://localhost:3000/fr/](http://localhost:3000/fr/), а страница `Начало работы` переведена.

:::caution

В процессе разработки можно использовать только одну локаль одновременно.

:::

## Добавьте раскрывающийся список локали

Чтобы легко перемещаться между языками, добавьте раскрывающийся список локали.

Измените файл `docusaurus.config.js`:

```js title="docusaurus.config.js"
export default {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'localeDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

Раскрывающийся список локали теперь отображается на панели навигации:

![Locale Dropdown](./img/localeDropdown.png)

## Создайте свой локализованный сайт

Создайте свой сайт для определенной локали:

```bash
npm run build -- --locale fr
```

Или создайте свой сайт так, чтобы он включал все локали одновременно:

```bash
npm run build
```
