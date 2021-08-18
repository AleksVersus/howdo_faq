# Builder fb2-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime

def getDate():
	when=datetime.datetime.now()
	time=f"{when.year}.{when.month}.{when.day}"
	return time

def typeString(string_):
	if re.match(r'^==.*?==$',string_)!=None:
		return 'h1'
	elif re.match(r'^=.*?=$',string_)!=None:
		return 'h2'
	elif re.match(r'^--.*?--$',string_)!=None:
		return 'h3'
	elif re.match(r'^-.*?-$',string_)!=None:
		return 'h4'
	elif re.match(r'^\+\+.*?\+\+$',string_)!=None:
		return 'h5'
	elif re.match(r'^\+.*?\+$',string_)!=None:
		return 'h6'
	elif re.match(r'^\s*<section_of_head>\s*$',string_)!=None:
		return 'section_of_head'
	elif re.match(r'^\[:.*?\]$',string_)!=None:
		return 'id'
	else:
		return 'other'

def getTitle(string_):
	return re.findall(r'(={1,2}|-{1,2}|\+)(.+?)(\1)',string_)[0][1]


def dirList(folder_path):
	files_list=[]
	folders_list=[] # локальные переменные
	# получаем список файлов и папок
	paths_list=os.listdir(folder_path)
	# обходим каждый адрес, проверяя является ли это файлом или папкой
	for path in paths_list:
		if os.path.isfile(folder_path+"\\"+path) and os.path.splitext(path)[1]=='.txt-light':
			files_list.append(folder_path+"\\"+path)
		elif os.path.isdir(folder_path+"\\"+path):
			folders_list.append(folder_path+"\\"+path)
	return files_list, folders_list

def getStringList(files_list):
	string_list=[] # локальная переменная
	# используем список файлов, чтобы генерировать секции
	for file in files_list:
		# открываем каждый файл последовательно
		with open(file,'r',encoding='utf-8') as this_file:
			string_list.extend(this_file.readlines())
	return string_list
	
class NewFolder():
	"""docstring for NewFolder"""
	def __init__(self, path_):
		self.path=path_ # объект папка обладает атрибутом путь
		files_list, folders_list = dirList(path_)
		self.file=getStringList(files_list) # атрибут file - это по сути список всех строк из всех файлов в папке
		self.folders=[] # атрибут folders - это по сути список вложенных объектов того же класса
		# перебираем все пути из списка папок и создаём на каждый по новому объекту
		for folder in folders_list:
			self.folders.append(NewFolder(folder))
	def __str__(self):
		return f'Folder Path: {self.path}; lenght of file: {len(self.file)}; number of includes: {len(self.folders)}.'
	def printFile(self):
		text=""
		for i in self.file:
			text+=i+'\n'
		return text
	def printFolders(self):
		text=""
		for i in self.folders:
			text+=i.path+"\n"
		return text

work_dir=os.getcwd()
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("fb2.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
export_file_path=os.path.abspath(project_dict["export_file"].replace('%TIME%',getDate()))
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
book_info_dict=root_dict["book-info"] # словарь с информацией о книге
# создаём объект папка верхнего уровня
roof=NewFolder(folder_path)

print(roof)
print(roof.printFile())
print(roof.printFolders())
	
	
	