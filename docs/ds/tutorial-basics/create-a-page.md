---
sidebar_position: 1
---

# Создать страницу

Добавьте файлы **Markdown или React** в `src/pages`, чтобы создать **отдельную страницу**:

- `src/pages/index.js` → `localhost:3000/`
- `src/pages/foo.md` → `localhost:3000/foo`
- `src/pages/foo/bar.js` → `localhost:3000/foo/bar`

## Создайте свою первую страницу React

Создайте файл в `src/pages/my-react-page.js`:

```jsx title="src/pages/my-react-page.js"
import React from 'react';
import Layout from '@theme/Layout';

export default function MyReactPage() {
  return (
    <Layout>
      <h1>My React page</h1>
      <p>This is a React page</p>
    </Layout>
  );
}
```

Новая страница теперь доступна по адресу [http://localhost:3000/my-react-page](http://localhost:3000/my-react-page).

## Создайте свою первую страницу Markdown

Создайте файл по адресу `src/pages/my-markdown-page.md`:

```mdx title="src/pages/my-markdown-page.md"
# My Markdown page

This is a Markdown page
```

Новая страница теперь доступна по адресу [http://localhost:3000/my-markdown-page](http://localhost:3000/my-markdown-page).
