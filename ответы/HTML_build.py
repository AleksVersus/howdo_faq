# Builder fb2-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime
from HTML_foo import *


if __name__=="__main__":
	work_dir=os.getcwd()
	generate_id=0
	# открываем файл проекта для чтения и получаем его структуру в переменную root
	with open("html.json","r",encoding="utf-8") as project_file:
		root_dict=json.load(project_file)
	project_dict=root_dict["project"] # словарь помещаем в переменную
	# формируем название релизного файла
	folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
	export_path=os.path.abspath(project_dict["export_folder"]) # папка, в которую помещаем файлы
	head_path=os.path.abspath(root_dict["head"])
	foot_path=os.path.abspath(root_dict["foot"])
	with open(head_path,'r',encoding='utf-8') as header:
		head_strings=header.readlines()
	with open(foot_path,'r',encoding='utf-8') as footer:
		foot_strings=footer.readlines()
	# создаём базу данных
	file_base=NewBD()
	# создаём объект папка верхнего уровня
	roof_folder=NewFolder(folder_path,file_base)
	# print(file_base.getBase())
	# теперь разматываем папку и файлы, получая HTML
	roof_folder.convert2HTML(file_base,export_path,head_strings,foot_strings)
