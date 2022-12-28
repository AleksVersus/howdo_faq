# Builder HTML-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime
from HTML_lib import *


def main(html_json):
	work_dir=os.getcwd() # получаем путь рабочей папки
	# открываем файл проекта для чтения и получаем его структуру в переменную root
	with open(html_json,"r",encoding="utf-8") as project_file:
		root_dict=json.load(project_file)
	project_dict=root_dict["project"] # словарь помещаем в переменную
	folder_path=os.path.abspath(project_dict["source_folder"]) # папка, из которой подтягиваем файлы
	export_path=os.path.abspath(project_dict["export_folder"]) # папка, в которую помещаем файлы
	# print(folder_path,export_path)
	if os.path.exists(export_path)!=True:
		os.makedirs(export_path)
	content_path=os.path.abspath(root_dict["head_contents"])
	# получаем заготовку вершины html-документа
	with open(os.path.abspath(root_dict["head"]),'r',encoding='utf-8') as header:
		head_strings=header.readlines()
	# получаем заготовку подвала html-документа
	with open(os.path.abspath(root_dict["foot"]),'r',encoding='utf-8') as footer:
		foot_strings=footer.readlines()
	file_base=NewDataBase() # создаём базу данных
	file_base.addHeader(head_strings) # добавляем в базу верхнюю часть html-документа
	file_base.addFooter(foot_strings) # добавляем в базу нижнюю часть html-документа
	file_base.addExportPath(export_path) # добавляем экспортный путь в базу
	file_base.setContentFile(content_path) # добавляем путь к файлу с содержанием
	file_base.addCrossLink(project_dict["cross-link"])
	roof_folder=NewFolder(folder_path,file_base) # создаём объект папка верхнего уровня
	# теперь разматываем папку и файлы, получая HTML
	roof_folder.convert2HTML(file_base)

if __name__=="__main__":
	# названия файлов, из которых берём сборку
	html_json=[
		# "..\\..\\[source]\\готовые статьи\\html.json",
		# "..\\..\\[source]\\ответы\\html.json",
		"..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		main(path)
