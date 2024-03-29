# howdo_faq
Справочник по самым часто задаваемым вопросам из темы "Как сделать?" на форуме QSP.SU

Пути в html.json должны записываться относительно папки, в которой расположен билдер HTML-файлов.

Этот проект начинался как "Справочник по самым часто задаваемым вопросам из темы «Как сделать?» на форуме QSP.org", однако теперь он разросся вширь и помимо непосредственно справочника теперь здесь есть ещё два раздела: "ИнформАрхив QSP" и "Статьи о QSP".

**ИнформАрхив QSP** — это раздел, в котором я собираю и компилирую старые статьи по QSP, которые мне нужны в одном месте для удобства.

**Статьи о QSP** — это раздел, в котором я размещаю статьи о QSP, написанные непосредственно мной.

Необходимо было генерировать справочник из исходников в виде готовых HTML-страниц и в виде fb2-файла. Поэтому были написаны два конвертера из моего формата текстовых файлов, похожего на markdown в HTML, и в FB2.

[онлайн-версия справочника](https://aleksversus.github.io/howdo_faq/)

## Конвертер в HTML

Конвертирует исходники в набор готовых страниц HTML, между которыми создаются перекрёстные ссылки, в т.ч. ссылки для перелистывания страниц по порядку.

При конвертировании опирается на специальный опорный файл `html.json`, в котором прописывается некоторая структура:

```json
{
	// все пути прописываются относительно билдера

	// папка исходников.
	"source-folder": "..\\..\\[source]\\ИнформАрхив QSP",
	// папка, в которой будут размещаться страницы и fb2-документ после билдинга
	"output-folder": "..\\..\\informarch",

	// сборочник для html-версии справочника
	"project-html":
	{
		// начало перекрёстных ссылок внутри справочника
		"cross-link": "https://aleksversus.github.io/howdo_faq/informarch/",
		// верх html-страницы
		"head": "..\\..\\[source]\\ИнформАрхив QSP\\add\\02_start.html",
		// низ html-страницы
		"foot": "..\\..\\[source]\\ИнформАрхив QSP\\add\\03_end.html",
		// файл с содержанием справочника
		"head-contents": "..\\..\\[source]\\ИнформАрхив QSP\\000_soderzhanie_0000.txt-light"
	},
	
	// сборочник для fb2-версии справочника
	"project-fb2":
	{
		// название выходного файла
		"output-file":"informarch.%TIME%.fb2",
		// начальные строки файла
		"book-info": "..\\..\\[source]\\ИнформАрхив QSP\\add\\fb2_head.xml",
		// конечные строки файла со всеми бинарниками
		"binary": "..\\..\\[source]\\ИнформАрхив QSP\\add\\fb2_footer.xml"
	}
}
```

Файлы исходников должны именоваться только латиницей.

В конце каждого исходника ставится порядковый номер (в порядке создания, а не в порядке следования в папке). 

В начале имени каждого исходника можно вставлять число и символ нижнего подчёркивания. Это помогает размещать исходники в нужном порядке, как страницы. Эти числа удаляются из имени при генерации HTML-файла, таким образом, даже если мы меняем расположение исходников в папках и разделах, имена конечных HTML-файлов останутся неизменны и уникальны, и таким образом ссылки на эти файлы не будут затираться.

Необходимо фиксировать номера последних файлов по каждому разделу. Для этого в папке `res` предусмотрена папка `[count]`. В ней лежат файлы с последним числом для каждого нового файла раздела. 

Альт-архив для wiki.qsp.org. Редакция 2022.12.29: [Справка по QSP](https://aleksversus.github.io/howdo_faq/wiki/start.html).
