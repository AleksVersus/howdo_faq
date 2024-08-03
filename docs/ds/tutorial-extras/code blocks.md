# Блоки кода

Блоки кода в документации обладают сверхмощью 💪.

## Заголовок кода

Вы можете добавить заголовок к блоку кода, добавив ключ `title` после языка (оставьте пробел между ними).

````
```jsx title="/src/components/HelloCodeTitle.js"
function HelloCodeTitle(props) {  return <h1>Hello, {props.name}</h1>;}
```
````

![[Pasted image 20240803140518.png]]

## Подсветка синтаксиса

Блоки кода — это текстовые блоки, заключенные в строки из 3 обратных кавычек. Вы можете ознакомиться с [этой ссылкой](https://github.com/mdx-js/specification) для спецификаций MDX.

````
```
jsconsole.log('Every repo must come with a mascot.');
```
````

Используйте соответствующую строку метаданных языка для вашего блока кода, и Docusaurus автоматически подберет подсветку синтаксиса, работающую на [Prism React Renderer](https://github.com/FormidableLabs/prism-react-renderer).

![[Pasted image 20240803140637.png]]

### Темы

По умолчанию мы используем [тему подсветки синтаксиса](https://github.com/FormidableLabs/prism-react-renderer#theming) Prism  [Palenight](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/prism-react-renderer/src/themes/palenight.ts). Вы можете изменить ее на другую тему, передав поле `theme` в `prism` как `themeConfig` в вашем docusaurus.config.js.

Например, если вы предпочитаете использовать тему подсветки `dracula`:

```js title="docusaurus.config.js"
import {themes as prismThemes} from 'prism-react-renderer';
export default {
	themeConfig: {
	    prism: {
	          theme: prismThemes.dracula,
	    },
	},
};
```

Поскольку тема Prism — это всего лишь объект JS, вы также можете написать свою собственную тему, если вас не устраивает тема по умолчанию. Docusaurus улучшает темы `github` и `vsDark`, чтобы обеспечить более богатую подсветку, и вы можете проверить наши реализации для тем блока кода [light](https://github.com/facebook/docusaurus/blob/main/website/src/utils/prismLight.ts) и [dark](https://github.com/facebook/docusaurus/blob/main/website/src/utils/prismDark.ts).

### Поддерживаемые языки

По умолчанию Docusaurus поставляется с подмножеством [часто используемых языков](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/generate-prism-languages/index.ts#L9-L23).

:::warning[ПРЕДУПРЕЖДЕНИЕ]
Некоторые популярные языки, такие как Java, C# или PHP, по умолчанию не включены.
:::

Чтобы добавить подсветку синтаксиса для любого другого [языка, поддерживаемого Prism](https://prismjs.com/#supported-languages), определите его в массиве дополнительных языков.

:::note[ПРИМЕЧАНИЕ]
Каждый дополнительный язык должен быть допустимым именем компонента Prism. Например, Prism сопоставил бы _language_ `cs` с `csharp`, но только `prism-csharp.js` существует как _component_, поэтому вам нужно использовать `additionalLanguages: ['csharp']`. Вы можете заглянуть в `node_modules/prismjs/components`, чтобы найти все доступные компоненты (языки).
:::

Например, если вы хотите добавить подсветку для языка PowerShell:

```js title="docusaurus.config.js"
export default {
	// ...
	themeConfig: {
	    prism: {
	          additionalLanguages: ['powershell'],
	    },
	// ...
	},
};
```

После добавления `additionalLanguages` перезапустите Docusaurus.

Если вы хотите добавить подсветку для языков, которые еще не поддерживаются Prism, вы можете использовать `prism-include-languages`:

```bash npm
npm run swizzle @docusaurus/theme-classic prism-include-languages
```

Он создаст `prism-include-languages.js` в вашей папке `src/theme` . Вы можете добавить поддержку подсветки для пользовательских языков, отредактировав `prism-include-languages.js`:

```js title="src/theme/prism-include-languages.js"
const prismIncludeLanguages = (Prism) => {
	// ...
	additionalLanguages.forEach((lang) => {
		require(`prismjs/components/prism-${lang}`);
	});
	require('/path/to/your/prism-language-definition');
	// ...
};
```

Вы можете обратиться к [официальным определениям языков Prism](https://github.com/PrismJS/prism/tree/master/components) при написании собственных определений языков.

При добавлении пользовательского определения языка вам не нужно добавлять язык в массив конфигурации `additionalLanguages`, поскольку Docusaurus ищет только строки `additionalLanguages` на языках, которые предоставляет Prism. Достаточно добавить импорт языка в `prism-include-languages.js`.
## Выделение строк
### Выделение с помощью комментариев

Вы можете использовать комментарии с `highlight-next-line`, `highlight-start` и `highlight-end` для выбора выделяемых строк.

````
```jsfunction HighlightSomeText(highlight) {
	if (highlight) {
	// highlight-next-line
	return 'This text is highlighted!';
	}
	
	return 'Nothing highlighted';
}

function HighlightMoreText(highlight) {
	// highlight-start
	if (highlight) {
		return 'This range is highlighted!';
	}
	// highlight-end
	return 'Nothing highlighted';
}```
````

![[Pasted image 20240803130936.png]]

Supported commenting syntax:

|Style|Syntax|
|---|---|
|C-style|`/* ... */` and `// ...`|
|JSX-style|`{/* ... */}`|
|Bash-style|`# ...`|
|HTML-style|`<!-- ... -->`|

Мы сделаем все возможное, чтобы определить, какой набор стилей комментариев использовать на основе языка, и по умолчанию разрешить _все_ стили комментариев. Если есть стиль комментариев, который в настоящее время не поддерживается, мы открыты для их добавления! Запросы на извлечение приветствуются. Обратите внимание, что разные стили комментариев не имеют семантической разницы, есть только их содержимое.

Вы можете установить свой собственный цвет фона для выделенной строки кода в вашем `src/css/custom.css`, который будет лучше соответствовать выбранной вами теме подсветки синтаксиса. Цвет, указанный ниже, подходит для темы подсветки по умолчанию (Palenight), поэтому, если вы используете другую тему, вам придется соответствующим образом настроить цвет.

/src/css/custom.css

```css title="/src/css/custom.css"
:root {
	--docusaurus-highlighted-code-line-bg: rgb(72, 77, 91);
}

/* If you have a different syntax highlighting theme for dark mode. */
[data-theme='dark'] {
	/* Color which works with dark mode syntax highlighting theme */
	--docusaurus-highlighted-code-line-bg: rgb(100, 100, 100);
}
```

Если вам также нужно стилизовать выделенную строку кода каким-либо другим способом, вы можете нацелиться на класс CSS `theme-code-block-highlighted-line`.
### Выделение с помощью строки метаданных

Вы также можете указать выделенные диапазоны строк в метастроке языка (оставьте пробел после языка). Чтобы выделить несколько строк, разделите номера строк запятыми или используйте синтаксис диапазона, чтобы выбрать фрагмент строк. Эта функция использует библиотеку `parse-number-range`, и вы можете найти [больше синтаксиса](https://www.npmjs.com/package/parse-numeric-range) в их деталях проекта.

````
```jsx {1,4-6,11}
import React from 'react';

function MyComponent(props) {
	if (props.isBar) {
		return <div>Bar</div>;
	}
	return <div>Foo</div>;
}
export default MyComponent;
```
````

![[Pasted image 20240803131439.png]]

:::tip[Комментарии предпочтений]

Предпочитайте подсветку с комментариями, где это возможно. Встраивая подсветку в код, вам не придется вручную подсчитывать строки, если ваш блок кода станет длинным. Если вы добавляете/удаляете строки, вам также не придется смещать диапазоны строк.

````
- ```jsx {3}
+ ```jsx {4}
  function HighlightSomeText(highlight) {
	if (highlight) {
+     console.log('Highlighted text found');
	  return 'This text is highlighted!';
	}
	
	return 'Nothing highlighted';
  }
  ```
````

Ниже мы покажем, как можно расширить систему магических комментариев для определения пользовательских директив и их функций. Магические комментарии будут анализироваться только в том случае, если метастрока подсветки отсутствует.

### Пользовательские магические комментарии

`// highlight-next-line` и `// highlight-start` и т. д. называются "магическими комментариями", потому что они будут проанализированы и удалены, а их цель — добавить метаданные в следующую строку или раздел, который включает пара начальных и конечных комментариев. Вы можете объявить пользовательские магические комментарии через конфигурацию темы. Например, вы можете зарегистрировать другой магический комментарий, который добавляет имя класса `code-block-error-line`:
- 
- src/css/custom.css
- myDoc.md

- js
```js title="docusaurus.config.js"
export default {
	themeConfig: {
		prism: {
			magicComments: [
				// Remember to extend the default highlight class name as well!
				{
					className: 'theme-code-block-highlighted-line',
					line: 'highlight-next-line',
					block: {start: 'highlight-start', end: 'highlight-end'},
				},
				{
					className: 'code-block-error-line',
					line: 'This will error',
				},
			],
		},
	},
};
	```
- css
  ```css title="src/css/custom.css"
  .code-block-error-line {  
background-color: #ff000020;  
display: block;  
margin: 0 calc(-1 * var(--ifm-pre-padding));  
padding: 0 var(--ifm-pre-padding);  
border-left: 3px solid #ff000080;  
}
```
- md
  ````md title="myDoc.md"
	  In JavaScript, trying to access properties on `null` will error.  
  
		```js  
		const name = null;  
		// This will error  
		console.log(name.toUpperCase());  
		// Uncaught TypeError: Cannot read properties of null (reading 'toUpperCase')  
		```
	````

![[Pasted image 20240803132628.png]]

Если вы используете диапазоны чисел в metastring (синтаксис `{1,3-4}`), Docusaurus применит имя класса **первой записи** `magicComments`. По умолчанию это `theme-code-block-highlighted-line`, но если вы измените конфигурацию `magicComments` и используете другую запись в качестве первой, значение диапазона metastring также изменится.

Вы можете отключить подсветку комментариев по умолчанию с помощью `magicComments: []`. Если конфигурации магических комментариев нет, но Docusaurus обнаружит блок кода, содержащий диапазон metastring, он выдаст ошибку, потому что не будет имени класса для применения — в конце концов, имя класса подсветки — это всего лишь запись магического комментария.

Каждая запись магического комментария будет содержать три ключа: `className` (обязательно), `line`, который применяется к следующей строке, или `block` (содержащий `start` и `end`), который применяется ко всему блоку, заключенному между двумя комментариями.

Использование CSS для нацеливания на класс уже может многое сделать, но вы можете раскрыть весь потенциал этой функции с помощью [swizzling](https://docusaurus.io/docs/swizzling).

```bash
npm run swizzle @docusaurus/theme-classic CodeBlock/Line
```

Компонент `Line` получит список имен классов, на основе которых вы можете условно отображать различную разметку.

## Нумерация строк

Вы можете включить нумерацию строк для своего блока кода, используя ключ `showLineNumbers` в метастроке языка (не забудьте добавить пробел непосредственно перед ключом).

````
```jsx {1,4-6,11} showLineNumbers
import React from 'react';

function MyComponent(props) {
	if (props.isBar) {
		return <div>Bar</div>;
	}
	
	return <div>Foo</div>;
}

export default MyComponent;
```
````

![[Pasted image 20240803133026.png]]

## Интерактивный редактор кода

(Работает на [React Live](https://github.com/FormidableLabs/react-live))

Вы можете создать интерактивный редактор кода с плагином `@docusaurus/theme-live-codeblock`. Сначала добавьте плагин в свой пакет.

```bash
npm install --save @docusaurus/theme-live-codeblock
```

You will also need to add the plugin to your `docusaurus.config.js`.

```js
export default {
	// ...
	themes: ['@docusaurus/theme-live-codeblock'],
	// ...
};
```

Чтобы использовать плагин, создайте блок кода с `live`, прикрепленным к метастроке языка.

````
```jsx live
function Clock(props) {
	const [date, setDate] = useState(new Date());
	useEffect(() => {
		const timerID = setInterval(() => tick(), 1000);
		
		return function cleanup() {
			clearInterval(timerID);
		};
	});
	
	function tick() {
		setDate(new Date());
	}
	
	return (
		<div>
			<h2>It is {date.toLocaleTimeString()}.</h2>
		</div>
	);
}
```
````

Блок кода будет отображаться как интерактивный редактор. Изменения в коде будут отображаться на панели результатов в реальном времени.

![[Pasted image 20240803133508.png]]

### Импорты

:::warning[REACT-LIVE И ИМПОРТЫ]
Невозможно импортировать компоненты напрямую из редактора кода React-Live, вам необходимо заранее определить доступные импорты.
:::

По умолчанию доступны все импорты React. Если вам нужно больше доступных импортов, измените область действия React-Live:

```bash
npm run swizzle @docusaurus/theme-live-codeblock ReactLiveScope -- --eject
```

```jsx title="src/theme/ReactLiveScope/index.js"
import React from 'react';

const ButtonExample = (props) => (
	<button
		{...props}
		style={{
			backgroundColor: 'white',
			color: 'black',
			border: 'solid red',
			borderRadius: 20,
			padding: 10,
			cursor: 'pointer',
			...props.style,
		}}
	/>
);

// Add react-live imports you need here
const ReactLiveScope = {
	React,
	...React,
	ButtonExample,
};

export default ReactLiveScope;
```

Компонент `ButtonExample` теперь доступен для использования:

![[Pasted image 20240803133939.png]]

### Императивный рендеринг (noInline)

Опцию noInline следует использовать, чтобы избежать ошибок, когда ваш код охватывает несколько компонентов или переменных.

````
```jsx live noInline
const project = 'Docusaurus';

const Greeting = () => <p>Hello {project}!</p>;

render(<Greeting />);
```
````

В отличие от обычного интерактивного блока кода, при использовании `noInline` React Live не будет оборачивать ваш код во встроенную функцию для его рендеринга.

Вам нужно будет явно вызвать `render()` в конце вашего кода, чтобы отобразить вывод.

![[Pasted image 20240803134151.png]]

## Использование разметки JSX в блоках кода

Блок кода в Markdown всегда сохраняет свое содержимое в виде обычного текста, что означает, что вы не можете сделать что-то вроде:
```jsx
type EditUrlFunction = (params: {
	// This doesn't turn into a link (for good reason!)
	version: <a href="/docs/versioning">Version</a>;
	versionDocsDirPath: string;
	docPath: string;
	permalink: string;
	locale: string;
}) => string | undefined;
```

Если вы хотите внедрить HTML-разметку, например ссылки-якоря или жирный шрифт, вы можете использовать тег `<pre>`, тег `<code>` или компонент `<CodeBlock>`.

```jsx
<pre>
	<b>Input: </b>1 2 3 4{'\n'}
	<b>Output: </b>"366300745"{'\n'}
</pre>
```

![[Pasted image 20240803134506.png]]

:::warning[MDX нечувствителен к пробелам]

MDX соответствует поведению JSX: символы переноса строки, даже если они находятся внутри `<pre>`, преобразуются в пробелы. Вам необходимо явно написать символ новой строки, чтобы он был выведен.
:::
:::warning[ПРЕДУПРЕЖДЕНИЕ]
Подсветка синтаксиса работает только для простых строк. Docusaurus не будет пытаться анализировать содержимое блока кода, содержащего дочерние элементы JSX.
:::

## Блоки кода поддержки нескольких языков

С помощью MDX вы можете легко создавать интерактивные компоненты в своей документации, например, для отображения кода на нескольких языках программирования и переключения между ними с помощью компонента вкладок.

Вместо реализации специального компонента для блоков кода поддержки нескольких языков мы реализовали компонент общего назначения `<Tabs>` в классической теме, чтобы вы могли использовать его и для других сценариев, не связанных с кодом.

В следующем примере показано, как можно использовать вкладки кода нескольких языков в своих документах. Обратите внимание, что пустые строки над и под каждым языковым блоком являются намеренными. Это текущее ограничение MDX: вам нужно оставлять пустые строки вокруг синтаксиса Markdown, чтобы анализатор MDX знал, что это синтаксис Markdown, а не JSX.

````jsx
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="js" label="JavaScript">

```js
function helloWorld() {
	console.log('Hello, world!');
}
```

</TabItem>
<TabItem value="py" label="Python">

```py
def hello_world():
	print("Hello, world!")
```

</TabItem>
<TabItem value="java" label="Java">

```java
class HelloWorld {
	public static void main(String args[]) {
		System.out.println("Hello, World");
	}
}
```

</TabItem>
</Tabs>
````

И вы получите следующее:

![[Pasted image 20240803135118.png]]

- JavaScript
  ```js
	function helloWorld() {  
		console.log('Hello, world!');  
	}
	```
- Python
  ```python
	def hello_world():  
		print("Hello, world!")
	```
- Java
  ```java
	class HelloWorld {  
		public static void main(String args[]) {  
			System.out.println("Hello, World");  
		}  
	}
	```

Если у вас несколько таких многоязычных вкладок кода и вы хотите синхронизировать выбор между экземплярами вкладок, обратитесь к разделу [Синхронизация вариантов выбора вкладок](https://docusaurus.io/docs/markdown-features/tabs#syncing-tab-choices).

### Плагин примечания Docusaurus npm2yarn

Отображение команд CLI как в npm, так и в Yarn — очень распространенная потребность, например:

![[Pasted image 20240803135453.png]]

Docusaurus предоставляет такую ​​утилиту из коробки, освобождая вас от использования компонента `Tabs` каждый раз. Чтобы включить эту функцию, сначала установите пакет `@docusaurus/remark-plugin-npm2yarn`, как указано выше, а затем в `docusaurus.config.js` для плагинов, где вам нужна эта функция (doc, blog, pages и т. д.), зарегистрируйте ее в параметре `remarkPlugins`. (См. [Конфигурация документов](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#ex-config) для получения более подробной информации о формате конфигурации)

```js title="docusaurus.config.js"
export default {
	// ...
	presets: [
		[
			'@docusaurus/preset-classic',
			{
				docs: {
					remarkPlugins: [
						[require('@docusaurus/remark-plugin-npm2yarn'), {sync: true}],
					],
				},
				pages: {
					remarkPlugins: [require('@docusaurus/remark-plugin-npm2yarn')],
				},
				blog: {
					remarkPlugins: [
						[
							require('@docusaurus/remark-plugin-npm2yarn'),
							{converters: ['pnpm']},
						],
					],
					// ...
				},
			},
		],
	],
};
```

А затем используйте его, добавив ключ `npm2yarn` в блок кода:

````
```bash npm2yarn
npm install @docusaurus/remark-plugin-npm2yarn
```
````

#### Configuration[​](https://docusaurus.io/docs/markdown-features/code-blocks#npm2yarn-remark-plugin-configuration "Direct link to Configuration")

| Option       | Type      | Default            | Description                                                                                                                       |
| ------------ | --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `sync`       | `boolean` | `false`            | Синхронизировать ли выбранный преобразователь по всем блокам кода.                                                                |
| `converters` | `array`   | `'yarn'`, `'pnpm'` | Список используемых конвертеров. Порядок конвертеров важен, так как первый конвертер будет использоваться как выбор по умолчанию. |

## Использование в JSX

Вне Markdown вы можете использовать компонент `@theme/CodeBlock`, чтобы получить тот же вывод.

```jsx
import CodeBlock from '@theme/CodeBlock';

export default function MyReactPage() {
	return (
		<div>
			<CodeBlock
				language="jsx"
				title="/src/components/HelloCodeTitle.js"
				showLineNumbers>
				{`function HelloCodeTitle(props) {
					return <h1>Hello, {props.name}</h1>;
				}`}
			</CodeBlock>
		</div>
	);
}
```

![[Pasted image 20240803140243.png]]

Принимаются свойства `language`, `title` и `showLineNumbers`, так же, как вы пишете блоки кода Markdown.

Хотя это и не рекомендуется, вы также можете передать свойство `metastring`, например `metastring='{1-2} title="/src/components/HelloCodeTitle.js" showLineNumbers'`, так блоки кода Markdown обрабатываются изнутри. Однако мы рекомендуем вам [использовать комментарии для выделения строк](https://docusaurus.io/docs/markdown-features/code-blocks#highlighting-with-comments).

Как [указывалось ранее](https://docusaurus.io/docs/markdown-features/code-blocks#using-jsx-markup), подсветка синтаксиса применяется только тогда, когда дочерние элементы являются простой строкой.