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
		self.addition=[] # добавочная секция в файл
	def proveAdd(self):
		if len(self.addition)!=0:
			return True
		else:
			return False
	def addAdd(self,source):
		self.addition.extend(source)
	def delAdd(self):
		self.addition=[]
	def getLastID(self):
		# получаем последний айди
		return '0'*(8-len(str(self.filecount)))+str(self.filecount)
	def addFile(self, path,**args):
		# добавляем файл
		if not "section_id" in args:
			args["section_id"]=''
		file=[path,self.getLastID(),args["section_id"]]
		self.base.append(file)
		self.filecount+=1
	def getBase(self):
		return self.base
	def searchFile(self,**args):
		result=None
		for file_path,file_id,section_id in self.base:
			if ("section_id" in args) and (section_id==args["section_id"]):
				result=[file_path,file_id,section_id]
				break
			if ("file_id" in args) and (file_id==args["file_id"]):
				result=[file_path,file_id,section_id]
				break
			if ("file_path" in args) and (file_path==args["file_path"]):
				result=[file_path,file_id,section_id]
				break
		if "result" in args:
			# если мы хотим получить какой-то определённый результат
			if args["result"]=="file_path":
				return result[0]
			if args["result"]=="file_id":
				return result[1]
			if args["result"]=="section_id":
				return result[2]
			if args["result"]=="index":
				return self.base.index(result)
		else:
			return result[0]
	def getID(self,path):
		return self.searchFile(file_path=path,result='section_id')
	def changeID(self,path,section_id):
		idx=self.searchFile(file_path=path,result='index')
		self.base[idx][2]=section_id
class NewSection():
	"""Части файла представляют собой блоки"""
	def __init__(self):
		self.type="" # тип блока
		self.id="" # id блока
		self.source=[] # список строк блока
		self.HTML=[] # html форма секции
	def addString(self,string):
		self.source.append(string)
	def changeType(self,type_):
		self.type=type_
	def changeID(self,id_):
		self.id=id_
	def getLen(self):
		return len(self.source)
	def getAttr(self,**args):
		if not "attr" in args:
			args["attr"]='source'
		if args['attr']=='type':
			return self.type
		if args['attr']=='id':
			return self.id
		if args['attr']=='source':
			return self.source
	def getType(self):
		return self.getAttr(attr='type')
	def getSource(self):
		return self.getAttr(attr='source')
	def convert2HTML(self,base):
		if self.type=="":
			# имеем дело с параграфом. Каждая строка - отдельный параграф
			for string in self.source:
				self.HTML.append(convertInParagraph(string))

class NewFile():
	"""Каждый файл представляет собой список строк"""
	def __init__(self,path,base):
		self.path=path
		with open(path,'r',encoding='utf-8') as file:
			source_list=file.readlines()
		self.source=clearStringList(source_list)
		self.sections=[] # блоки, составляющие файл
		self.HTML=[] # блоки с конвертацией уже в HTML
		if base.proveAdd()==True:
			self.sections=base.addition+self.sections
		if self.getFileName()=='00.txt-light':
			# если это файл заголовка, этот заголовок будет добавляться ко всем последующим файлам
			base.addAdd(self.source)
		else:
			base.addFile(path) # добавляем файл в базу
			self.fileSplit(base) # разбиваем файл на блоки
			self.convert2HTML(base)
	def getFileName(self):
		return os.path.split(self.path)[1]
	def fileSplit(self,base):
		section_=NewSection()
		mode={"give_id":False,
			"give_id_off":False,
			"section_of_head":False,
			"code-block":False,
			"quote-block":False}
		for i in self.source:
			if typeString(i)=='section_of_head-open':
				mode["section_of_head"]=True
				self.sections.append(section_)
				section_=NewSection()
				section_.changeType('section_of_head')
			elif mode["section_of_head"]==False:
				if re.match(r'h\d+',typeString(i))!=None:
					if section_.getLen()!=0:
						# если по какой-то причине предыдущая секция не закрыта
						self.sections.append(section_)
						section_=NewSection()
					section_.changeType(typeString(i))
					section_.addString(getTitle(i))
					mode["give_id"]=True
					mode["give_id_off"]=True
				elif typeString(i)=='id' and mode["give_id"]==True:
					section_.changeID(getID(i))
					mode["give_id_off"]=False
					# первый встреченный айдишник становится идентификатором файла
					if base.getID(self.path)=="":
						base.changeID(self.path,getID(i))
				elif typeString(i)=='ul':
					if section_.getAttr(attr='type')!='ul':
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType(typeString(i))
					section_.addString(i)
				elif typeString(i)=='ol':
					if section_.getAttr(attr='type')!='ol':
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType(typeString(i))
					section_.addString(i)
				elif typeString(i)=='code':
					# метки кода только переключают режим
					if mode["code-block"]==False:
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType('code-block')
						section_.addString(i) # необходимо добавить строку, чтоб определить, что за код
						mode["code-block"]=True
					else:
						self.sections.append(section_)
						section_=NewSection()
						mode["code-block"]=False
				elif typeString(i)=='quote':
					# метки кода только переключают режим
					if mode["quote-block"]==False:
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType('quote-block')
						mode["quote-block"]=True
					else:
						self.sections.append(section_)
						section_=NewSection()
						mode["quote-block"]=False
				elif typeString(i)=='quote-string':
					if section_.getAttr(attr='type')!='quote-block':
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType('quote-block')
					section_.addString(i)
				elif typeString(i)=='empty' and mode["code-block"]==False:
					self.sections.append(section_)
					section_=NewSection()
				else:
					if re.match(r'h\d+',section_.getAttr(attr='type'))!=None:
						self.sections.append(section_)
						section_=NewSection()
					section_.addString(i)
					if typeString(i)=='id':
						mode["give_id_off"]=False
			elif typeString(i)=='section_of_head-close':
				mode["section_of_head"]=False
				self.sections.append(section_)
				section_=NewSection()
				section_.changeType('section_of_head')
			else:
				section_.addString(i)
			if mode["give_id_off"]==True:
				mode["give_id_off"]=False
			else:
				mode["give_id"]=False
		if section_.getLen()!=0:
			self.sections.append(section_)
	def convert2HTML(self,base):
		# перебираем список секций
		for section_ in self.sections:
			section_.convert2HTML(base)
	def printAll(self):
		text=""
		text+=f"'File Path: {self.path}'\n"
		for i in self.sections:
			text+=f"'Type Section: {i.getAttr(attr='type')}, ID: {i.getAttr(attr='id')}, len: {i.getLen()}'\n"
			if i.getAttr(attr='type')=='h1':
				text+=f"'H1: "
				for sec in i.getAttr():
					text+=f"string: {sec},"
				text+="'\n"
		text+=f"'File End: {self.path}'\n"
		return text

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
		base.delAdd() # удаляем дополнительные заголовки перед перебором файлов
		for file in files_list:
			self.files.append(NewFile(file,base))
	def printAll(self):
		text=""
		text+=f"'Folder Path: {self.path}'\n"
		for i in self.files:
			text+=i.printAll()
		for i in self.folders:
			text+=i.printAll()
		text+=f"'Folder End: {self.path}'\n"
		return text

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

print(file_base.getBase())