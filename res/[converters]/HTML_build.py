# txt-light to html converter 
import sys
import os
import re
import json # импорт необходимых модлулей

from HTML_lib import TextToHTML

def main():
	# названия файлов, из которых берём сборку
	html_json=[
		"..\\..\\[source]\\готовые статьи\\html.json",
		# "..\\..\\[source]\\ответы\\html.json",
		# "..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		TextToHTML(path).convert_to_html()

if __name__=="__main__":
	main()
