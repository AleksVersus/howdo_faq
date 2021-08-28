# Builder fb2-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime
from HTML_foo import *

class NewBD():
	"""База данных представляет собой список файлов с их идентификаторами:
	путь, уникальный идентификатор, идентификатор в привязке к структуре"""
	def __init__(self):
		self.base=[] # сама по себе база является списком списков
		self.filecount=0
	def getLastID(self):
		# получаем последний айди
		return '0'*(8-len(str(self.filecount)))+str(self.filecount)
	def addFile(self, path,**args):
		# добавляем файл
		if not "section_id" in args:
			args["section_id"]=''
		file=[path,self.getLastID(),args["section_id"]]
		self.base.append(file)
	def getBase(self):
		return self.base

class NewFile():
	"""Каждый файл представляет собой список строк"""
	def __init__(self,path,base):
		self.path=path
		with open(path,'r',encoding='utf-8') as file:
			source_list=file.readlines()
		self.source=clearStringList(source_list)
		base.addFile(path) # добавляем файл в базу

class NewFolder():
	"""Каждая папка включает в себя другие папки и файлы.
	Непосредственно сама папка на структуру не влияет, влияет только наполнение."""
	def __init__(self,path,base):
		self.path=path # полный путь к папке
		self.files=[] # список вложенных файлов!
		self.folders=[] # список вложенных папок!
		files_list, folders_list = dirList(path)
		for folder in folders_list:
			self.folders.append(NewFolder(folder,base))
		for file in files_list:
			self.files.append(NewFile(file,base))


work_dir=os.getcwd()
generate_id=0
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("html.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
export_path=os.path.abspath(project_dict["export_folder"]) # папка, в которую помещаем файлы
# создаём базу данных
file_base=NewBD()
# создаём объект папка верхнего уровня
roof_folder=NewFolder(folder_path,file_base)
# теперь разматываем папку и файлы, получая HTML
#roof_folder.getHTML()
print(file_base.getBase())