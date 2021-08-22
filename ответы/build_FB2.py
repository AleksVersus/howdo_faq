# Builder fb2-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime
from foo import *

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
		self.sections=[]
		self.tempfile=self.body[:]
	def printAll(self):
		text=[]
		text.append(f"==section: {self.id} open!==\n")
		text.append(f"section: {self.id}, iclude body: \n")
		text.extend(self.tempfile)
		text.append(f"section: {self.id}, bodies strings enough!\n")
		text.append(f"section: {self.id}, include sections: \n")
		for i in self.sections:
			text.extend(i.printAll())
		text.append(f"section: {self.id}, sections enough!\n")
		text.append(f"==section: {self.id} close!==\n")
		return text
	def chAttr(self, attr_, string_):
		if attr_=="id":
			self.id=string_
		if attr_=="title":
			self.title=string_
	def addInBody(self,string_):
		if type(string_)==str:
			self.body.append(string_)
			self.tempfile.append(string_)
		elif type(string_)==list:
			self.body.extend(string_)
			self.tempfile.extend(string_)
	def bodyLen(self):
		return len(self.body)
	def popString(self):
		string=self.body.pop(0)
		return typeString(string),string
	def split(self):
		level=5
		no_split=True
		no_search=False
		# получаем наибольший уровень заголовка
		for string in self.body:
			if re.match(r'^\s*<section_of_head>\s*$',string)!=None:
				no_search=True
			elif re.match(r'^\s*</section_of_head>\s*$',string)!=None:
				no_search=False
			if no_search!=True:
				type_=typeString(string)
				if re.match(r'h\d+',type_)!=None:
					no_split=False
					level_=int(type_[1:])
					if level_<level:
						level=level_
		split_type='h'+str(level)
		# разбиваем на секции только если есть возможность, т.е. найдены заголовки
		if no_split!=True:
			# теперь, когда уровень получен, можно разбивать
			section_=NewSection()
			mode={'give_id':False,'give_id_off':False,'no_spliting':False} 
			while len(self.body)>0:
				# пока не будут выбраны все строки
				type_,string=self.popString() # выбираем строку
				if type_=="section_of_head-open":
					section_.split() # похожий метод применяем к секции
					self.sections.append(section_)
					section_=NewSection()
					mode['no_spliting']=True
				elif mode['no_spliting']==False:
					if type_==split_type:
						# строка нужного нам типа заголовок
						if section_.bodyLen()==0 and section_.title=="":
							# секция пока пуста
							pass
						else:
							# если секция не пуста, создаём новую секцию
							section_.split() # похожий метод применяем к секции
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
						section_.addInBody(string)
					# отключает режим приёма ай-ди только на второй проход после заголовка
					if mode['give_id_off']==True:
						mode['give_id_off']=False
					else:
						mode['give_id']=False
				elif type_=="section_of_head-close":
					section_.split() # похожий метод применяем к секции
					self.sections.append(section_)
					section_=NewSection()
					mode['no_spliting']=False
				else:
					section_.addInBody(string)
			if section_.bodyLen()!=0 or section_.title!="":
				# когда мы перебрали все строки, а набираемая секция не пуста
				section_.split() # похожий метод применяем к секции
				self.sections.append(section_)
	def getFB2(self):
		global generate_id
		text_strings=[]
		if self.id!="":
			id_=self.id
		else:
			generate_id+=1
			id_=f"generate_{generate_id}"
		text_strings.append(f'<section id="{id_}">\n')
		# данный метод получает Структуру fb2-документа из содержимого секции
		if len(self.title)!=0:
			text_strings.append(f'<title>{self.title}</title>\n')
		if len(self.sections)==0 and len(self.body)!=0:
			# если в секции нет секций, она содержит только строки
			text_strings.extend(self.body)
		elif len(self.sections)!=0 and len(self.body)==0:
			# может быть либо список строк, либо список секций
			for section_ in self.sections:
				text_strings.extend(section_.getFB2())
		text_strings.append('</section>\n')
		return text_strings

class NewFolder():
	"""docstring for NewFolder"""
	def __init__(self, path_):
		self.path=path_ # объект папка обладает атрибутом путь
		files_list, folders_list = dirList(path_)
		self.file=getStringList(files_list) # атрибут file - это по сути список всех строк из всех файлов в папке
		self.tempfile=self.file[:]
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
		for i in self.tempfile:
			text+=i+'\n'
		return text
	def printFolders(self):
		text=""
		for i in self.folders:
			text+=i.path+"\n"
		return text
	def printSections(self):
		text=f"number of sections: {len(self.sections)}\n"
		for i in self.sections:
			text+=f"{i.title}\n[:{i.id}]\n"
		return text
	def printAll(self):
		text=[]
		text.append(f"==folder: {self.path} open!==\n")
		text.append(f"folder: {self.path}, iclude file: \n")
		text.extend(self.tempfile)
		text.append(f"folder: {self.path}, files strings enough!\n")
		text.append(f"folder: {self.path}, include folders: \n")
		for i in self.folders:
			text.extend(i.printAll())
		text.append(f"folder: {self.path}, folders enough!\n")
		text.append(f"folder: {self.path}, include sections: \n")
		for i in self.sections:
			text.extend(i.printAll())
		text.append(f"folder: {self.path}, sections enough!\n")
		text.append(f"==folder: {self.path} close!==\n")
		return text
	def popString(self):
		string=self.file.pop(0)
		return typeString(string),string
	def fileSplit(self):
		level=5
		no_split=True
		no_search=False
		# численно более высокий уровень имеет меньшее значение
		for string in self.file:
			if re.match(r'^<section_of_head>$',string)!=None:
				no_search=True
			elif re.match(r'^</section_of_head>$',string)!=None:
				no_search=False
			if no_search!=True:
				type_=typeString(string)
				if re.match(r'h\d+',type_)!=None:
					no_split=False
					level_=int(type_[1:])
					if level_<level:
						level=level_
		split_type='h'+str(level)
		# теперь, когда уровень получен, можно разбивать
		if no_split!=True:
			section_=NewSection()
			mode={'give_id':False,'give_id_off':False,'no_spliting':False} 
			while len(self.file)>0:
				# пока не будут выбраны все строки
				type_,string=self.popString() # выбираем строку
				if type_=="section_of_head-open":
					section_.split() # похожий метод применяем к секции
					self.sections.append(section_)
					section_=NewSection()
					mode['no_spliting']=True
				elif mode['no_spliting']==False:
					if type_==split_type:
						# строка нужного нам типа заголовок
						if section_.bodyLen()==0 and section_.title=="":
							# секция пока пуста
							pass
						else:
							# если секция не пуста, создаём новую секцию
							section_.split() # похожий метод применяем к секции
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
						section_.addInBody(string)
					# отключает режим приёма ай-ди только на второй проход после заголовка
					if mode['give_id_off']==True:
						mode['give_id_off']=False
					else:
						mode['give_id']=False
				elif type_=="section_of_head-close":
					section_.split() # похожий метод применяем к секции
					self.sections.append(section_)
					section_=NewSection()
					mode['no_spliting']=False
				else:
					section_.addInBody(string)
			if section_.bodyLen()!=0 or section_.title!="":
				# когда мы перебрали все строки, а набираемая секция не пуста
				section_.split() # похожий метод применяем к секции
				self.sections.append(section_)
	def getFB2(self,**args_):
		global generate_id
		text_strings=[]
		if len(self.sections)!=0 or len(self.file)!=0 or len(self.folders)!=0:
			# чтобы не плодить пустые секции, нужно чтобы хотябы какой-то атрибут папки существовал
			if not "start" in args_:
				args_["start"]=False
			if args_["start"]:
				open_='<body>\n'
				close_='</body>\n'
			elif len(self.sections)==0 and len(self.file)==0:
				open_=f'<section id="{self.path}">\n'
				close_='</section>\n'
			else:
				open_=''
				close_=''
			text_strings.append(open_)
			# данный метод получает Структуру fb2-документа из содержимого папки
			if len(self.sections)==0 and len(self.file)!=0:
				# если в папке нет натуральных секций, значит весь файл является секцией
				text_strings.append(f'<section id="{self.path}">\n')
				text_strings.extend(self.file)
				text_strings.append('</section>\n')
			elif len(self.sections)==1:
				if self.sections[0].id!="":
					id_=self.sections[0].id
				else:
					generate_id+=1
					id_=f"generate_{generate_id}"
				text_strings.append(f'<section id="{id_}">\n')
				text_strings.extend(self.sections[0].getFB2()[1:-1])
				close_='</section>\n'
			elif len(self.sections)!=0 and len(self.file)==0:
				# может быть либо файл, либо секция, третьего не дано
				for section_ in self.sections:
					text_strings.extend(section_.getFB2())
			if len(self.folders)!=0:
				for folder_ in self.folders:
					text_strings.extend(folder_.getFB2())
			text_strings.append(close_)
		return text_strings


work_dir=os.getcwd()
generate_id=0
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("fb2.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
export_file_path=os.path.abspath(project_dict["export_file"].replace('%TIME%',getDate()))
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
book_info_dict=root_dict["book-info"] # словарь с информацией о книге
document_info=root_dict["document-info"]
# создаём объект папка верхнего уровня
roof_folder=NewFolder(folder_path)
# теперь нам необходимо разматывать этот объект в секции
body_fb2=roof_folder.getFB2(start=True)
# теперь, когда объект размотан в список строк с секциями, можно начинать форматирование
fb2output=convertationFB2(body_fb2)
with open("fb2output.xml",'w',encoding='utf-8') as export_file:
	export_file.writelines(fb2output)
fb2_file=[]
fb2_file.append(f'<?xml version="1.0" encoding="utf-8"?>\n')
fb2_file.append(f'<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">\n')
fb2_file.append(f'<description>\n')
fb2_file.append(f'<title-info>\n')
genres=book_info_dict["genre"]
for i in genres:
	fb2_file.append(f'<genre>{i}</genre>\n')
fb2_file.append(f'<author>')
fn=book_info_dict["author"]['first-name']
mn=book_info_dict["author"]['middle-name']
ln=book_info_dict["author"]['last-name']
fb2_file.append(f'<first-name>{fn}</first-name>\n')
fb2_file.append(f'<middle-name>{mn}</middle-name>\n')
fb2_file.append(f'<last-name>{ln}</last-name>\n')
fb2_file.append(f'</author>\n')
fb2_file.append(f'<book-title>{book_info_dict["book-title"]}</book-title>\n')
fb2_file.append(f'<annotation>\n')
with open(book_info_dict["annotation"],"r",encoding='utf-8') as annotation:
	an_list=annotation.readlines()
for i in an_list:
	fb2_file.append(f'<p>{i}</p>\n')
fb2_file.append(f'</annotation>\n')
date_=book_info_dict['date']
fb2_file.append(f'<date value="{date_}">24 августа 2021</date>\n')
lang_=book_info_dict['lang']
fb2_file.append(f'<lang>{lang_}</lang>\n')
fb2_file.append(f'</title-info>\n')

fb2_file.append(f'<document-info>\n')
for i in book_info_dict["genre"]:
	fb2_file.append(f'<genre>{i}</genre>\n')
fb2_file.append(f'<author>\n')
fn=document_info["author"]['first-name']
mn=document_info["author"]['middle-name']
ln=document_info["author"]['last-name']
fb2_file.append(f'<first-name>{fn}</first-name>\n')
fb2_file.append(f'<middle-name>{mn}</middle-name>\n')
fb2_file.append(f'<last-name>{ln}</last-name>\n')
fb2_file.append(f'</author>\n')
fb2_file.append(f'<program-used>build_fb2.py</program-used>\n')
fb2_file.append(f'<date value="{getDate(mode="xml")}">{getDate(mode="xml")}</date>\n')
fb2_file.append(f'<id>691C3AD3-DB00-4DCD-8B3F-FE36355FD126</id>\n')
fb2_file.append(f'<version>{document_info["version"]}</version>\n')
fb2_file.append(f'<history>\n')
for i in document_info["history"]:
	fb2_file.append(f'<p>{i}</p>\n')
fb2_file.append(f'</history>\n')
fb2_file.append(f'</document-info>\n')
fb2_file.append(f'</description>\n')
fb2_file.extend(fb2output)
fb2_file.append(f'</FictionBook>\n')
with open(export_file_path,'w',encoding='utf-8') as export_file:
	export_file.writelines(fb2_file)