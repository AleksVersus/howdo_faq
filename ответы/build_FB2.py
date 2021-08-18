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

class SectionObj():
	"""section"""
	def __init__(self, id_, type_, title_):
		self.id=id_ # идентификатор секции
		self.type=type_ # тип секции
		self.title=title_ # заголовок секции
		self.body=[] # тело секции - список
		global section_count
		section_count+=1
	def addInBody(self,string_):
		self.body.append(string_)
	def getBody(self):
		return self.body
	def change(self,element_,string_):
		# данный метод заменяет значение атрибута
		if element_=="id":
			self.id=string_
		elif element_=="type":
			self.type=string_
		elif element_=="title":
			self.title=string_
	def __str__(self):
		return f"{self.type}[{self.id}]: {self.title} (lenght {len(self.body)})"
	
section_count=0 # подсчёт числа создаваемых секций
work_dir=os.getcwd()
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("fb2.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
export_file_path=os.path.abspath(project_dict["export_file"].replace('%TIME%',getDate()))
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
book_info_dict=root_dict["book-info"] # словарь с информацией о книге

# генерируем первую секцию
section=SectionObj("body","body","")
files_list=[]
folders_list=[]
# получаем список файлов и папок
paths_list=os.listdir(folder_path)
print(folder_path,paths_list)
# обходим каждый адрес, проверяя является ли это файлом или папкой
for path in paths_list:
	if os.path.isfile(folder_path+"\\"+path) and os.path.splitext(path)[1]=='.txt-light':
		files_list.append(folder_path+"\\"+path)
	elif os.path.isdir(folder_path+"\\"+path):
		folders_list.append(folder_path+"\\"+path)
# теперь когда у нас есть список файлов и папок
# используем список файлов, чтобы генерировать секции
for file in files_list:
	# открываем каждый файл последовательно
	with open(file,'r',encoding='utf-8') as this_file:
		string_list=this_file.readlines()
	# получив список строк, перебираем эти строки
	for string in string_list:
		string_type=typeString(string)
		if string_type=='h1':
			# если мы имеем дело с заголовком