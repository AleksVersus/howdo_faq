# основа конвертирования. Исключительные классы и функции для преобразования в HTML
import sys, os, re, json
import random
from HTML_foo import * 

class NewDataBase():
	"""База данных — объект, содержащий описания якорей и секций
	в их привязке к файлам/секциям. Каждый файл обладает уникальным 
	путём, и каждый якорь уникален, поэтому:
	{file_path:file_id} - связка пути файла с его айди
	{anchor_id:file_id} - связка якоря и файла"""
	def __init__(self):
		self.filecount=0 # счётчик файлов
		self.files_dict={} # здесь связываем файлы и их идентификаторы
		self.anchors_dict={} # здесь связываем якоря и файлы, в которых они расположены
		self.curfile="" # идентификатор текущего файла (файл, с которым мы работаем)
		self.addition=[] # добавочная секция в файл
		self.header_list=[] # верх страницы html
		self.footer_list=[] # низ страницы html
		self.export_folder_path="" # путь к папке для экспорта
	def currentFile(self):
		# получаем идентификатор текущего файла
		return self.curfile
	def setCurFile(self,id_):
		# устанавливаем текущий файл. Выбираем его айди
		self.curfile=id_
	def proveAdd(self):
		# присутствует ли в базе добавочная секция
		return (True if len(self.addition)!=0 else False)
	def addAdd(self,string_list):
		# добавляем в базу добавочную секцию
		self.addition.extend(string_list)
	def delAdd(self):
		# удаляем из базы добавочную секцию
		self.addition=[]
	def getAdd(self):
		# получаем из базы добавочную секцию
		return self.addition[:1]
	def lastFileID(self):
		# получаем последний айди файлов
		if self.filecount==0:
			return None
		else:
			return '0'*(8-len(str(self.filecount-1)))+str(self.filecount-1)
	def genNewFileID(self):
		# генерируем айди из счётчика
		return '0'*(8-len(str(self.filecount)))+str(self.filecount)
	def addFile(self,path):
		# добавление нового файла
		id_=self.genNewFileID() # генерируем идентификатор файла
		self.filecount+=1 # увеличиваем счётчик
		self.files_dict[path]=id_ # вносим файл в словарь
		self.curfile=id_ # текущим файлом становится добавленный
	def addAnchor(self,anchor):
		# добавляем якорь к файлу
		if self.curfile!="":
			self.anchors_dict[anchor]=self.curfile
		else:
			print("Ошибка! Текущий Файл не определён. Якорь <<anchor>> не добавлен")
	def getFileID(self,path):
		# получаем айди файла по указанному пути
		return (self.files_dict[path] if path in self.files_dict else None)
	def getFilePath(self,id_):
		# получаем путь к файлу по ай-ди
		result=None
		for key in self.files_dict:
			if self.files_dict[key]==id_:
				result=key
				break
		return result
	def getFileName(self,anchor):
		# получаем айди файла по содержащемуся в нём якорю
		return (self.anchors_dict[anchor] if anchor in self.anchors_dict else None)
	def addHeader(self,string_list):
		self.header_list=string_list[:]
	def addFooter(self,string_list):
		self.footer_list=string_list[:]
	def getHeader(self):
		return self.header_list[:]
	def getFooter(self):
		return self.footer_list[:]
	def addExportPath(self,path):
		self.export_folder_path=path
	def getExportPath(self):
		return self.export_folder_path


class NewFolder():
	"""
	Каждая папка - объект, содержащий другие файлы и папки
	Непосредственно сама папка для html-документов на структуру не влияет, влияет только наполнение.
	"""
	def __init__(self,path,base):
		self.path=path # полный путь к папке является её уникальным идентификатором
		self.files=[] # список вложенных файлов
		self.folders=[] # список вложенных папок
		# получаем списки файлов и папок 
		files_list, folders_list = dirList(path)
		# создаём новые папки и помещаем их в список
		for folder in folders_list:
			self.folders.append(NewFolder(folder,base))
		base.delAdd() # удаляем дополнительные заголовки перед перебором файлов
		# создаём новые файлы и помещаем в другой список
		for file in files_list:
			self.files.append(NewFile(file,base))
	def convert2HTML(self,base):
		pass

class NewFile():
	"""
	Каждый файл представляет собой контейнер для секций.
	"""
	def __init__(self,path,base):
		self.path=path # путь к файлу является его уникальным идентификатором
		# получаем список строк, это и есть файл
		with open(path,'r',encoding='utf-8') as file:
			self.source=file.readlines()
		self.sections=[] # блоки составляющие файл
		self.HTML=[] # список строк готового HTML-файла
		if base.proveAdd():
			self.source=base.getAdd()+self.source
		if self.getFileName()=='00.txt-light':
			# если это файл заголовка, этот заголовок будет добавляться ко всем последующим файлам
			base.addAdd(self.source)
		else:
			# если это не файл заголовка
			base.addFile(path) # добавляем файл в базу
			self.sections.append(NewSection(self.source,'',base))
			self.convert2HTML(base)
	def getFileName(self):
		# получаем имя файла, отсекая путь
		return os.path.split(self.path)[1]
	def convert2HTML(self,base):
		# конвертируем секции файла в HTML
		for section in self.sections:
			section.convert2HTML(base)
	def getHTML(self,base):
		pass
