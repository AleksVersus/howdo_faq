import sys, os, re, json # импорт необходимых модлулей
import datetime

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
	def __str__(self):
		return f"'{self.type},{self.id},{len(self.source)},{len(self.HTML)},{type(self)}'\n"
	def convert2HTML(self,base):
		if self.type=="":
			# имеем дело с параграфом. Каждая строка - отдельный параграф
			for string in self.source:
				self.HTML.append('<p>\n'+convertString(string,'string',base)+'\n</p>\n')
		elif re.match(r'h\d+',self.type)!=None:
			# имеем дело с заголовком
			for string in self.source:
				self.HTML.append(convertString(string,'string',base))
		elif self.type=="code-block":
			# имеем дело с блоком кода
			self.HTML.extend(convertCodeBlock(self.source))
		elif self.type=="ul" or self.type=="ol":
			self.HTML.extend(convertListBlock(self.source,base_))
		elif self.type=="section_of_head":
			# имеем дело с секцией заголовков
			self.HTML.extend(convertSOHBlock(self.source,base_))
	def getHTML(self):
		return self.HTML
class NewQuazy():
	"""Квази-файл. Класс, почти точно такой же, как и настоящий файл, но с отличиями"""
	def __init__(self,source_list,base_):
		self.source=clearStringList(source_list)
		self.sections=[] # блоки, составляющие файл
		self.HTML=[] # блоки с конвертацией уже в HTML
		self.fileSplit(base_) # разбиваем файл на блоки
		self.convert2HTML(base_)
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
					# маркированные и нумерованные списки идут в общую секцию, если следуют друг за другом 
					if section_.getAttr(attr='type')!='ul' and section_.getAttr(attr='type')!='ol':
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType(typeString(i))
					section_.addString(i)
				elif typeString(i)=='ol':
					# маркированные и нумерованные списки идут в общую секцию, если следуют друг за другом 
					if section_.getAttr(attr='type')!='ol' and section_.getAttr(attr='type')!='ul':
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
	def getHTML(self):
		new_string_list=[]
		for section_ in self.sections:
			new_string_list.extend(section_.getHTML())
		return new_string_list
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
			self.source=base.addition[:1]+self.source
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
					# маркированные и нумерованные списки идут в общую секцию, если следуют друг за другом 
					if section_.getAttr(attr='type')!='ul' and section_.getAttr(attr='type')!='ol':
						self.sections.append(section_)
						section_=NewSection()
						section_.changeType(typeString(i))
					section_.addString(i)
				elif typeString(i)=='ol':
					# маркированные и нумерованные списки идут в общую секцию, если следуют друг за другом 
					if section_.getAttr(attr='type')!='ol' and section_.getAttr(attr='type')!='ul':
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
	def getHTML(self):
		new_string_list=[]
		for section_ in self.sections:
			new_string_list.extend(section_.getHTML())
		return new_string_list
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