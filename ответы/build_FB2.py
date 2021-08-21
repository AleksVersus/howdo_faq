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
	
class NewSection():
	def __init__(self,**args_):
		if "id" in args_:
			self.id=args_['id']
		else:
			self.id=""
		if "title" in args_:
			self.title=args_['title']
		else:
			self.title=''
		if "body" in args_:
			self.body=args_['body']
		else:
			self.body=[]
	def chAttr(self, attr_, string_):
		if attr_=="id":
			self.id=string_
		if attr_=="title":
			self.title=string_
	def addInBody(self,string_)
		if type(string_)==str:
			self.body.append(string)
		elif type(string_)==list:
			self.body.extend(string_)
	def bodyLen(self):
		return len(self.body)


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
		self.sections=[]
		self.fileSplit()
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
	def popString(self):
		string=self.file.pop(0)
		return typeString(string),string
	def fileSplit(self):
		level=5
		for string in self.file:
			type_=typeString(string)
			if re.match(r'h\d+',type_)!=None:
				level_=int(type_[1:])
				if level_<level:
					level=level_
		split_type='h'+str(level)
		# теперь, когда уровень получен, можно разбивать
		section_=NewSection()
		mode={'give_id':False,'give_id_off':False} 
		while len(self.file)>0:
			# пока не будут выбраны все строки
			type_,string=self.popString() # выбираем строку
			if type_==split_type:
				# строка нужного нам типа заголовок
				if section_.bodyLen()==0 and section_.title=="":
					# секция пока пуста
					pass
				else:
					# если секция не пуста, создаём новую секцию
					self.sections.append(section_)
					section_=NewSection()
				section_.chAttr('title',getTitle(string))
				mode['give_id']=True # включаем режим приёма ай-ди. Следующая строка может рассматриваться, как ай-ди
				mode['give_id_off']=True
			elif type_=='id':
				# строка типа айди
				if mode['give_id']==True:
					section_.chAttr('id',getID(string))
				else:
					section_.addInBody(string)
				mode['give_id_off']=True
			else:
				section.addInBody(string)
			# отключает режим приёма ай-ди только на второй проход после заголовка
			if mode['give_id_off']==True:
				mode['give_id_off']=False
			else:
				mode['give_id']=False




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
roof_folder=NewFolder(folder_path)
# теперь нам необходимо разматывать этот объект в секции

	
	
	