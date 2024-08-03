---
authors:
  - alex
tags:
  - документация
  - docusaurus
  - highlighting
---
# Подсветка синтаксиса QSP в Docusaurus

Добавил в документацию Docusaurus подсветку синтаксиса для кода QSP, которая пока что умеет не много.

В частности, пока не удалось победить многострочные комментарии и звёздочку перед названием операторов работы с окном основного описания. Тем не менее кое-что уже работает и простые примеры будут отображаться довольно симпатично.

Например:

```qsp title="Действие по условию"
if ваза_на_столе=1:
  ! если переменная-маркер ваза_на_столе равна 1

  ! создаём действие
  act "Взять вазу со стола":
    ! в действии изменяем значение переменной-маркера
    ваза_на_столе=0
    addobj "Ваза"
    goto $curloc
  end
end
```
Или вот ещё пример:

```qsp title="Код в формате qsps с двумя локациями"
# start
result = 123	& ! записываем число в переменную result
N=24
*pl func('square')	& ! выведет на экран 576
*pl result	& ! выведет на экран 123
- start -

vase_on_desk = 0

# square
result = N * N
- square -
```

:::warning[Проверяйте окончания строк]
LineEndings при использовании подсветки в markdown-файлах для Docusaurus должны быть строго `LF`! Не `CRLF`, иначе вылезают артефакты в виде лишних отступов.
:::

Установка подсветки в ваш Docusaurus весьма проста:
1. Используйте swizzle для того, чтобы добавить неподдерживаемые языки, введя команду в терминале:
	```bash
	npm run swizzle @docusaurus/theme-classic prism-include-languages
	```
	При этом будет создан файл "`src/theme/prism-include-languages.ts`" (или `.js`).
2. В папке "`src/theme"` создайте папку `qsp-syntax` и скопируйте в неё файл "`prism-qsp.js`", например, [отсюда](). <!-- TODO: не забыть добавить ссылку -->
3. В файле "`src/theme/prism-include-languages.ts`" отредактируйте функцию `prismIncludeLanguages`:
	```js
	export default function prismIncludeLanguages(PrismObject: typeof PrismNamespace,): void {
	  // ...
	  additionalLanguages.forEach((lang) => {
	    // ...
	    require(`prismjs/components/prism-${lang}`);
	  });
	  require('./qsp-syntax/prism-qsp.js');
	  // ..
	}
	```

После сохранения и перезапуска сервера, или при сборке проекта, подсветка QSP-кода подхватится.

Больше примеров работы подсветки можно посмотреть в **[онлайн-версии справочника](https://aleksversus.github.io/howdo_faq/)** по самым часто задаваемым вопросам о QSP.

:::tip
Параллельно была написана подсветка для Obsidian: **[qsp-syntax-obsidian](https://github.com/AleksVersus/qsp-syntax-obsidian)**.
::