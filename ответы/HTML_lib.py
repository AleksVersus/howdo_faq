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
		self.content_file_path="" # путь к файлу-оглавлению
		self.content=[] # содержимое содержания
		self.export_folder_path="" # путь к папке для экспорта
		self.typesOfClass={
			"base":NewDataBase,
			"folder":NewFolder,
			"file":NewFile,
			"segment":NewSegment,
			"section":NewSection
		} # связка тип обекта указанного класса с ключом. Сразу прописываем нужные типы
	def currentFile(self):
		# получаем идентификатор текущего файла
		return self.curfile
	def setCurFile(self,id_):
		# устанавливаем текущий файл. Выбираем его айди
		self.curfile=id_

	def proveAdd(self):
		# присутствует ли в базе добавочная секция
		return (True if len(self.addition)!=0 else False)
	def getAdd(self):
		# получаем из базы добавочную секцию
		return self.addition[:1]
	def addAdd(self,string_list):
		# добавляем в базу добавочную секцию
		self.addition.extend(string_list)
	def delAdd(self):
		# удаляем из базы добавочную секцию
		self.addition=[]

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

	def addAnchor(self,anchor):
		# добавляем якорь к файлу
		if self.curfile!="":
			self.anchors_dict[anchor]=self.curfile
		else:
			print("Ошибка! Текущий Файл не определён. Якорь <<anchor>> не добавлен")

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

	def addClassType(self,kw,type_):
		self.typesOfClass[kw]=type_
	def getClassType(kw):
		return (self.typesOfClass[kw] if kw in self.typesOfClass else None)
	def proveClassType(kw):
		return (True if kw in self.typesOfClass else False)

	def setContentFile(self,path):
		# устанавливает путь к файлу с содержанием
		self.content_file_path=path
	def getContentFile(self,path):
		# получает путь к файлу с содержанием
		return self.content_file_path
	def addContent(self,string_list):
		# разметку HTML файла оглавления помещаем в базу
		self.content_HTML=string_list[:]
	def getContent(self):
		# получаем оглавление в виде HTML разметки
		return self.content_HTML

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
		for file in self.files:
			file.buildThis(base)
		for folder in self.folders:
			folder.convert2HTML(base)

class NewFile():
	"""
	Каждый файл представляет собой контейнер для секций.
	"""
	def __init__(self,path,base):
		self.path=path # путь к файлу является его уникальным идентификатором
		# получаем список строк, это и есть файл
		with open(path,'r',encoding='utf-8') as file:
			self.source=file.readlines()
		self.segments=[] # сегменты, составляющие файл
		self.HTML=[] # список строк готового HTML-файла
		if self.getFileName()=='00.txt-light':
			# если это файл заголовка, этот заголовок будет добавляться ко всем последующим файлам
			base.addAdd(self.source)
		else:
			# если это не файл заголовка
			base.addFile(path) # добавляем файл в базу
			if base.proveAdd():
				self.source=base.getAdd()+self.source
			self.segments.append(NewSegment(self.source,'from_file',base))
			self.convert2HTML(base)
			# если путь к текущему файлу совпадает с путём к содержанию
			if base.getContentFile()==path:
				# добавляем содержание в базу
				base.addContent(self.HTML)
	def getFileName(self):
		# получаем имя файла, отсекая путь
		return os.path.split(self.path)[1]
	def convert2HTML(self,base):
		# конвертируем сегменты файла в HTML
		for segment in self.segments:
			segment.convert2HTML(base)
			self.HTML.extend(segment.getHTML(base))
	def getHTML(self,base):
		# возвращает полное содержимое файла
		new_string_list=[]
		header_list=base.getHeader()
		footer_list=base.getFooter()
		new_string_list=header_list+self.HTML+footer_list
		return new_string_list
	def buildThis(self,base):
		# собираем готовый HTML-файл
		pass

class NewSegment():
	"""
	Сегмент - это объект, заменяющий Файлы и Квазифайлы предыдущей версии программы.
	Сегмент разбивается на секции, а сами секции в свою очередь могут состоять из сегментов.
	Фактически - сегмент это виртуальный контейнер, промежуточный элемент между файлом и секцией.
	"""
	# взять тело функции split из квазифайла и построчно сравнить с телом функции в нормальном файле. Вместо назначения айдишников файлу у нас теперь просто якоря привязанные к текущему файлу.
	def __init__(self,source_list,type_,base):
		# только тип "из файла" заставляет очищать от комментариев
		self.source=(clearStringList(source_list) if type_=='from_file' else source_list)
		self.sections=[] # секции, составляющие сегмент
		self.HTML=[] # строки с конвертированием уже в HTML
		self.segmentSplit(base) # разбиваем на блоки
	def addSection(self,section):
		# функция добавляет секцию к списку секций
		# если в секции есть хоть какое-то содержимое
		if section.getLen()!=0:
			self.sections.append(section)
	def getLen(self):
		# возвращает число секций в сегменте
		return len(self.sections)
	def convert2HTML(self,base):
		# конвертирует все секции сегмента в HTML
		# и добавляем готовые строки в атрибут HTML сегмента
		for section in self.sections:
			section.convert2HTML(base)
			self.HTML.extend(section.getHTML(base))
	def getHTML(self,base):
		# возвращает HTML-содержимое сегмента
		return self.HTML
	def segmentSplit(self,base):
		# данный метод разбивает сегмент на секции
		section=NewSection() # создаём новую пустую секцию
		block_mode='' # выставляем режимы добора в секции
		manage_mode={	
			"head_list":('h1','h2','h3','h4','h5','h6'), # все типы строки для заголовков
			"h1-h6":('','quote-list','ul_ol-list','head-block'), # блоки, которые можно закрывать строкой заголовка
			"SoH-open":('','quote-list','ul_ol-list','head-block'), # блоки, которые можно закрывать через SOH
			"SoH-close":('section_of_head','quote-list','head-block'), # блоки, которые можно закрывать через SOH
			"id":('head-block','quote-list'), # блоки, которые можно закрывать строкой с айди
			"ul_ol":('','quote-list','head-block'),
			"code":('','code-block','head-block','quote-list'),
			"quote-block":('','quote-block','head-block','quote-list'),
			"quote-string":('','head-block'),
			"empty":('head-block','quote-list','ul_ol-list'),
			"other":('head-block','quote-list')
		} # здесь храним инфу для управления
		# перебираем строки, разбивая на секции
		for string in self.source:
			if typeString(string) in manage_mode["head_list"]:
				# строка является заголовком
				if block_mode in manage_mode["h1-h6"]:
					# если сейчас работает один из режимов, которые прерываются обнаружением строки-заголовка
					self.addSection(section) # добавляем к списку предыдущую секцию
					section=NewSection() # создаём новую секцию
					section.changeType(typeString(string)) # изменяем тип секции
					section.addString(getTitle(string)) # добавляем в секцию строку
					block_mode='head-block' # включаем режим работы блока
				else:
					# для всех остальных блоков строка заголовка - обычная строка
					section.addString(string)
			elif typeString(string)=='section_of_head-open':
				# если тип строки "открывающая Секции Заголовков"
				if block_mode in manage_mode["SoH-open"]:
					# если сейчас работает один из режимов, которые можно прервать
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # создаём новую секцию
					section.changeType('section_of_head') # изменяем тип вновь созданной секции
					block_mode="section_of_head" # переключаемся в режим добора строк в секцию заголовков
				else:
					# для всех остальных режимов, строка добавляется в секцию как есть
					section.addString(string)
			elif typeString(string)=='section_of_head-close':
				# если тип строки "закрывающая Секции Заголовков"
				if block_mode in manage_mode["SoH-close"]:
					# если сейчас работает один из режимов, которые можно прервать
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # создаём новую секцию
					block_mode='' # выключаем режим добора
				else:
					# для всех остальных режимов, строка добавляется в секцию как есть
					section.addString(string)
			elif typeString(string)=='id':
				# тип строки идентификатор
				base.addAnchor(getID(string)) # добавляем якорь в базу
				if block_mode=='head-block':
					# если работает режим заголовка
					section.changeID(getID(string)) # изменяем идентификатор секции
					self.addSection(section) # добавляем к списку предыдущую секцию
					section=NewSection() # создаём новую секцию
					block_mode=''
				elif block_mode in manage_mode["id"]:
					# если работает режим секции, который можно прервать
					self.addSection(section) # добавляем к списку предыдущую секцию
					section=NewSection() # создаём новую секцию
					section.addString(string) # добавляем строку в секцию, как обычную строку
					block_mode=''
				else:
					# во всех остальных случаях добавляем как обычную строку
					section.addString(string)
			elif typeString(string) in ('ul','ol'):
				# если данная строка является строкой маркированного или нумерованного списка
				if block_mode in manage_mode["ul_ol"]:
					# если включен режим, который данная строка способна выключить
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # создаём новую секцию
					section.changeType(typeString(string)) # изменяем тип вновь созданной секции
					section.addString(string)
					block_mode="ul_ol-list" # переключаемся в режим добора строк в секцию списка
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
			elif typeString(string)=='code':
				# метки кода переключают режим. В данном случае включаем режим добора строк в секцию кода
				if block_mode=='code-block':
					# если работает режим добора в секцию кода
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # создаём новую секцию
					block_mode='' # выключаем режим добора в секцию кода
				elif block_mode in manage_mode["code"]:
					# если работает режим, который можно прервать переключением в режим кода
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # создаём новую секцию
					section.changeType('code-block')
					section.addString(string) # начальная строка добавляется в блок, чтобы определять тип кода
					block_mode="code-block" # включаем режим добора в секцию кода
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
			elif typeString(string)=='quote':
				# строка открывает блок цитаты
				if block_mode=='quote-block':
					# если работает режим добора в блок цитаты, выключаем
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection()
					block_mode=""
				elif block_mode in manage_mode["quote-block"]:
					# если работает режим, который можно прервать по текущей строке
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection()
					section.changeType('quote-block')
					block_mode="quote-block"
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
			elif typeString(string)=='quote-string':
				# тип строки - строка цитаты
				if block_mode=="quote-list":
					# режим уже включен, добавляем строку в блок
					section.addString(clearQuoteString(string))
				elif block_mode in manage_mode["quote-string"]:
					# если работает режим, который можно прервать данной строко
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection()
					section.changeType('quote-block')
					section.addString(clearQuoteString(string))
					block_mode="quote-list"
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
			elif typeString(string)=='empty':
				# пустая строка (может содержать пробелы)
				if block_mode in manage_mode['empty']:
					# если включен режим, который данная строка прерывает
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # генерим новую секцию
					block_mode='' # выключаем режим
				elif block_mode=='':
					# если набираются параграфы, пустые строки между ними игнорируются
					pass
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
			else:
				# любой иной тип строки
				if block_mode in manage_mode["other"]:
					# все строки прерывают режим добора строк в заголовок или режим списка строк цитаты
					self.addSection(section) # добавляем к списку секций предыдущую секцию
					section=NewSection() # генерим новую секцию
					block_mode='' # прерываем секцию
				else:
					# в любом другом режиме строки добавляются как есть
					section.addString(string)
		if section.getLen()!=0:
			self.addSection(section)


class NewSection():
	"""
	Секция - это объект для хранения однотипных строк или сегментов (как правило одного).
	HTML-разметка вычисляется исходя из секций. Секция всегда генерируется в пустом виде,
	и лишь потом наполняется содержимым
	"""
	def __init__(self):
		self.type="" # тип секции
		self.id="" # id секции
		self.source=[] # список строк секции или сегментов
		self.HTML=[] # html форма секции
	def getLen(self):
		# возвращает условную длину секции
		return len(self.source)
	def changeType(self,string):
		# изменяет тип секции на указанный
		self.type=string
	def changeID(self,string):
		# изменяет идентификатор секции.
		# Этот идентификатор потом может служить якорем
		self.id=string
	def getType(self):
		# возвращает значение атрибута type
		return self.type
	def getID(self):
		# возвращает значение атрибута ID
		return self.id
	def addString(self,string):
		# добавляет строку в исходник секции
		self.source.append(string)
	def getHTML(self,base):
		# возвращает список преобразованных в HTML строк
		return self.HTML
	def convert2HTML(self,base):
		# конвертирование секции в HTML и добавление в атрибут HTML
		pass