from nodes import (TextToHTML, NewDataBase, NewFolder, NewFile, NewNode)

def main():
	# названия файлов, из которых берём сборку
	html_json=[
		# "..\\..\\[source]\\example\\html.json",
		"..\\..\\[source]\\готовые статьи\\build-project.json",
		"..\\..\\[source]\\ответы\\build-project.json",
		"..\\..\\[source]\\ИнформАрхив QSP\\build-project.json",
		# "..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		TextToHTML(path).convert_to()

if __name__=="__main__":
	main()