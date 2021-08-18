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
	# используем список файлов, чтобы генерировать секции
	for file in files_list:
		# открываем каждый файл последовательно
		with open(file,'r',encoding='utf-8') as this_file:
			string_list.extend(this_file.readlines())
	return string_list

class NewSection():
	"""section"""
	def __init__(self, path_, string_list_):
		global section_list
		# выставляем значения по умолчанию
		self.id=""
		self.title=""
		self.body=[]
		buffer=[]
		if len(path_)!=0:
			# если передан путь, получаем список файлов и папок
			files_list, folders_list = dirList(path_)
			# получаем список строк
			string_list=getStringList(files_list)
			# получив список строк, перебираем эти строки
			for string in string_list:
				string_type=typeString(string) # получаем тип строки
				if string_type=='h1': # если мы имеем дело с заголовком первого уровня
					if len(self.title)==0 and len(buffer)==0: # если ни в буффере, ни взаголовке текущей секции ничего нет
						self.title=getTitle(string)
					else:
						section
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
section_list=[]
work_dir=os.getcwd()
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("fb2.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
export_file_path=os.path.abspath(project_dict["export_file"].replace('%TIME%',getDate()))
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
book_info_dict=root_dict["book-info"] # словарь с информацией о книге

print(getTitle('==Заголовок=='))
	
	
	