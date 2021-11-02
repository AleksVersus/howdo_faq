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
		self.type=type_ # тип сегмента
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
		if self.type in ('h1','h2','h3','h4','h5','h6'):
			# имеем дело с заголовком
			lev=int(self.type[1:])
			if lev<6: lev+=1
			new_string_list=[]
			for string in self.source:
				new_string_list.append(self.convertString(string,'string',base))
			if self.id=='':
				self.id=randomString(4)
			self.HTML.append(f'<a id="{self.id}"></a><h{lev}>')
			self.HTML.extend(new_string_list)
			self.HTML.append(f'</h{lev}>\n')
		elif self.type=="code-block":
			# имеем дело с блоком кода
			self.HTML.extend(convertCodeBlock(self.source))
		elif self.type in ('ul','ol'):
			# имеем дело со списком
			self.HTML.extend(convertListBlock(self.source,base))
		elif self.type=="section_of_head":
			# имеем дело с секцией заголовков
			self.HTML.extend(convertSOHBlock(self.source,base))
		elif self.type=="quote-block":
			self.HTML.append('<blockquote>\n')
			segment=NewSegment(self.source,'quote-block',base)
			segment.convert2HTML(base)
			self.HTML.extend(segment.getHTML(base))
			self.HTML.append('\n</blockquote>\n')
		else:
			# имеем дело с параграфом. Каждая строка - отдельный параграф
			for string in self.source:
				self.HTML.append('<p>\n'+self.convertString(string,'string',base)+'\n</p>\n')
	def convertString(self,string,type_,base):
		# конвертируем строку в неразмеченную. Внёс функцию сюда, потому что
		# строка может конвертироваться только при преобразовании секции
		roof_string=NewString(string,type_,base)
		return roof_string.getHTML(base)
def convertString(string,type_,base):
		# конвертируем строку в неразмеченную. Внёс функцию сюда, потому что
		# строка может конвертироваться только при преобразовании секции
		roof_string=NewString(string,type_,base)
		return roof_string.getHTML(base)
class NewString():
	"""
	Прилагательный класс Строка. Чтобы рекурсивно обрабатывать строку, приходится генерировать новый объект
	"""
	def __init__(self,string,type_,base):
		self.source=string # исходная строка
		self.type=type_ # тип строки
		self.strings=[] # если строка бьётся на другие строки, в ней помимо исходника будут содержаться эти строки
		if self.type=='string':
			# корневой тип. Пока есть две вариации такой строки: термины и другие
			termins=re.match(r'^\s*?`.*?`(,\s+`.*?`)*\s*—',string) # начинается ли строка с терминов
			if termins!=None:
				# да строка начинается с терминов, значит выделяем эти термины и остальные части строки в отдельные строки
				termins=re.findall(r'`.+?`',re.match(r'^\s*?`.*?`(,\s+`.*?`)*',termins.group(0)).group(0))
				for term in termins:
					symbol=string.find(term)
					word1=string[0:symbol]
					word2=string[symbol:symbol+len(term)]
					if len(word1)>0:
						self.strings.append(NewString(word1,'',base))
					self.strings.append(NewString(word2[1:-1],'term',base))
					string=string[symbol+len(term):]
				if len(string)>0:
					self.strings.append(NewString(string,'',base))
			else:
				# строка начинается не с терминов, поэтому мы её рассматриваем как строку стандартного узлового типа
				self.strings.append(NewString(string,'',base))
		elif self.type=='term':
			# это строка типа термин, её содержимое рассматривается как строка стандартного узлового типа
			self.strings.append(NewString(string,'',base))
		elif self.type=='href':
			# если тип строки href, дальше она не изменяется
			pass
		elif self.type=='name':
			y_name,y_sub=re.findall(r'`([^`]+)`(\w+)\b',string)[0]
			self.strings.append(NewString(y_name,'authname',base)) # текст ссылки в нулевой ячейке
			self.strings.append(NewString(y_sub,'authsub',base)) # текст ссылки в нулевой ячейке
		elif self.type=='id':
			# теперь, если к нам приходит идентификатор, мы можем
			# этот идентификатор добавить в базу к текущему файлу
			base.addAnchor(string)
		elif self.type=="hyperlink":
			hl_text,hl_href=re.findall(r'^\[(.*?)\]\((.*?)\)$',string)[0]
			self.strings.append(NewString(hl_text,'',base)) # текст ссылки в нулевой ячейке
			if re.match(r'^#',hl_href)!=None:
				hl_href=f'#folder-file#{hl_href}#'
			self.strings.append(NewString(hl_href,'href',base)) # адрес в первой
		else:
			# для всех прочих строк, в том числе и типа monotype
			# описываем регулярки, как отдельные объекты
			id_regex=re.compile(r'\[:[^\]]*?\]')
			link_regex=re.compile(r'\[[^\]]*?\]\(.*?\)')
			name_regex=re.compile(r'`[^`\s]+?`\w+\b')
			mtp_regex=re.compile(r'`[^`]+?`')
			regex_dict={
				"id":[id_regex,lambda word:getID(word)],
				"hyperlink":[link_regex,lambda word:word],
				"name":[name_regex,lambda word:word],
				"monotype":[mtp_regex,lambda word:word[1:-1]]
			}
			fp_count=0 # счётчик найденных вложений
			for key in regex_dict:
				# перебираем все регэкспы в словаре
				find_pattern=regex_dict[key][0].search(string) # находим совпадения
				if find_pattern!=None:
					# совпадения найдены
					fp_count+=1
					words=regex_dict[key][0].findall(string) # извлекаем слова, подходящие под паттерн
					for word in words:
						# вытаскиваем все слова, подходящие под паттерн, остальное как ст.узловые строки
						symbol=string.find(word)
						word1=string[0:symbol]
						word2=string[symbol:symbol+len(word)]
						if word1!="":
							self.strings.append(NewString(word1,'',base))
						self.strings.append(NewString(regex_dict[key][1](word2),key,base))
						string=string[symbol+len(word):]
					if len(string)>0:
						self.strings.append(NewString(string,'',base))
					break # нам не нужно перебирать на все паттерны, потому что строка уже изменилась.
			if fp_count==0:
				# если в строке не обнаружено вложений, она не разбивается
				self.source=replaceAll(self.source)
	def getHTML(self,base):
		if len(self.strings)>0:
			text=""
			if self.type=="hyperlink":
				# имеем дело с гиперссылкой 0 - текст, 1 - линк
				text+=f'<a href="{self.strings[1].getHTML(base)}" style="text-decoration:none;" class="emFOLD">{self.strings[0].getHTML()}</a>'
			elif self.type=="name":
				# имеем дело с именем 0 - имя, 1 - окончание
				text+=f'<strong>{self.strings[0].getHTML(base)}</strong>\'{self.strings[1].getHTML(base)}'
			elif self.type=="term":
				# имеем дело с термином. Может включать в себя другие элементы
				for string in self.strings:
					text+=string.getHTML(base)
				text=f'<strong>{text}</strong>'
			else:
				# любой другой тип строки
				for string in self.strings:
					text+=string.getHTML(base)
			return text # всегда возвращаем только одну строку
		else:
			if self.type=="monotype":
				# моноширинное слово
				return convertMonotype(self.source)
			elif self.type=="term":
				# не разбитый термин
				return f'<strong>{self.source}</strong>'
			elif self.type=='id':
				# идентификатор
				return f'<a id="{self.source}"></a>'
			else:
				# любая другая строка
				return self.source

class NewLiBlock():
	# секция списка!
	def __init__(self,type_,source_list,base):
		self.id=randomString(8)
		self.type=type_
		self.source=source_list
		self.include=[] # список вложенных объектов, это могут быть только пункты
		# получаем минимальный уровень из исходников
		level,count=minLiLevel(self.source)
		if level!=None:
			buffer=[] # буффер для временного размещения строк
			# выполняем цикл, пока не исчерпаем исходник
			while len(self.source)>0:
				# получаем содержимое исходной строки
				t,l,s=self.source.pop(0)
				if l==level:
					# если совпадают уровни
					if len(buffer)!=0:
						# если в буфере что-то есть, отправляем буфер в пункт
						self.include.append(NewLi(buffer,base))
					# сам буфер теперь содержит только указанный исходник
					buffer=[[t,l,s]]
				else:
					# если уровни не совпадают, добавляем в буфер исходник
					buffer.append([t,l,s])
			if len(buffer)!=0:
				self.include.append(NewLi(buffer,base))
	def __str__(self):
		text=f'id:{self.id} type:{self.type} source.len:{len(self.source)}'
		return text
	def getHTML(self,base):
		new_string_list=[]
		# Блоки бывают только двух типов, третьего не дано
		if self.type=='marked':
			new_string_list.append('<ul>\n')
		elif self.type=='numered':
			new_string_list.append('<ol>\n')
		for li_point in self.include:
			new_string_list.extend(li_point.getHTML(base))
		if self.type=='marked':
			new_string_list.append('</ul>\n')
		elif self.type=='numered':
			new_string_list.append('</ol>\n')
		return new_string_list

class NewLi():
	# пункт списка
	def __init__(self,source_list,base):
		self.id=randomString(8)
		# у пункта нет типа, это просто пункт
		self.source=source_list
		self.include=[] # вложенные объекты: другие списки или строки
		if len(self.source)==1:
			# если мы передали только одну строку в исходнике, значит лишь эта строка и составляет пункт
			self.include.append(self.source.pop(0))
		else:	
			# получаем минимальный уровень из исходников
			level,count=minLiLevel(self.source)
			if level!=None:
				if count==1 and self.source[0][1]==level:
					# минимальный уровень находится только в нулевом исходнике
					self.include.append(self.source.pop(0)) # нулевой исходник становится строкой
				# оставшийся сорц бьётся на блоки/строки
				self.include.extend(splitLiBlocks(self.source,base))
				self.source=[]
			else:
				# если минимальный уровень не найден, разбить на блоки нельзя, генерим сегмент из оставшихся строк
				print(self.source)
				# self.include.extend(self.source)
				# self.source=[]
	def getHTML(self,base_):
		new_string_list=[]
		br_off=True
		new_string_list.append('<li>\n')
		for els in self.include:
			# print(els)
			if type(els)==list:
				# если типом является строка
				t,l,s=els
				if t==None and br_off==False:
					br='<br>'
				else:
					br=''
					br_off=False
				new_string_list.append(br+convertString(s,'string',base_))
			else:
				# если тип элемента - NewLiBlock
				new_string_list.extend(els.getHTML(base_))
				br_off=True
		new_string_list.append('</li>\n')
		return new_string_list
	def __str__(self):
		text=f'id:{self.id} include.len:{len(self.include)}'
		return text

# функции

def dirList(folder_path):
	# из пути к папке получаем её содержимое в виде списка файлов и папок
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

def randomString(length):
	letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
	letters+='ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю'
	result = ''.join(random.choice(letters) for i in range(length))
	return result

def clearStringList(string_list):
	# удаляем комментарии везде, кроме блоков кода
	# фактически функция создаёт новый список строк, оставляя исходный без изменений
	mode={"comment":False,"code":False}
	new_string_list=[]
	for string in string_list:
		comment=re.match(r'(.*?/\*.*)|(.*?\*/.*)',string)
		code=re.match(r'^\s*?```\w*\s*$',string)
		if mode["comment"]==True and comment==None:
			pass # строки комментария не добавляются в новый список
		elif mode["code"]==True and code==None:
			# строки в блоках кода добавляются без изменений
			new_string_list.append(string) 
		elif comment!=None and mode["code"]==False:
			# если строка содержит комментарий, а режим кода выключен
			# изменяем режим и получаем строку без комментария
			mode["comment"],string=remComment(string)
			if re.match(r'^\s+?$',string)!=None:
				# если строка состоит из одних пробелов, это пустая строка
				string=""
			if string!="" and string!=None:
				new_string_list.append(string) 
		elif code!=None and mode["comment"]==False:
			# если строка содержит границу блока кода, но не включён режим комментария
			if mode["code"]==False:
				mode["code"]=True
			else:
				mode["code"]=False
			# строка при этом добавляется в выходной список
			if re.match(r'^\s+?$',string)!=None:
				# если строка состоит из одних пробелов, это пустая строка
				string=""
			if string!="" and string!=None:
				new_string_list.append(string) 
		else:
			if string!=None:
				new_string_list.append(string) 
	return new_string_list

def remComment(string):
	# удаление части комментария (или всего) из строки
	mode_=False
	start_string=''
	end_string=''
	start_comment=re.match(r'.*?/\*.*',string)
	if start_comment!=None:
		start_string,comm,string=re.findall(r'(.*?)(/\*)(.*)',string)[0]
		mode_=True
	end_comment=re.match(r'.*?\*/.*',string)
	if end_comment!=None:
		string,comm,end_string=re.findall(r'(.*?)(\*/)(.*)',string)[0]
		mode_=False
	return mode_,start_string+end_string

def replaceSpace(string):
	string=string.replace('\t','&nbsp;'*4)
	string=string.replace(' ','&nbsp;')
	return string

def typeString(string):
	# определяем тип строки по содержимому
	if re.match(r'^==.*?==$',string)!=None:
		return 'h1'
	elif re.match(r'^=.*?=$',string)!=None:
		return 'h2'
	elif re.match(r'^--.*?--$',string)!=None:
		return 'h3'
	elif re.match(r'^-.*?-$',string)!=None:
		return 'h4'
	elif re.match(r'^\+\+.*?\+\+$',string)!=None:
		return 'h5'
	elif re.match(r'^\+.*?\+$',string)!=None:
		return 'h6'
	elif re.match(r'^\s*<section_of_head>\s*$',string)!=None:
		return 'section_of_head-open'
	elif re.match(r'^\s*</section_of_head>\s*$',string)!=None:
		return 'section_of_head-close'
	elif re.match(r'^\[:.*?\]$',string)!=None:
		return 'id'
	elif re.match(r'^\s*?\*\s+',string)!=None:
		return 'ul'
	elif re.match(r'^\s*?\d+\.\s+',string)!=None:
		return 'ol'
	elif re.match(r'^```\w*?',string)!=None:
		return 'code'
	elif re.match(r'^\s*?>>>\s*?$',string)!=None:
		return 'quote'
	elif re.match(r'^\s*?>\s+',string)!=None:
		return 'quote-string'
	elif re.match(r'^\s*?$',string)!=None:
		return 'empty'
	else:
		return 'other'

def getTitle(string):
	# функция получает текст из строки заголовка
	return re.findall(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$',string)[0][1]

def getID(string):
	# извлекает идентификатор (якорь) из строки
	return re.findall(r'(\[:)(.+?)(\])',string)[0][1]

def clearQuoteString(string):
	# очищает строку от метки цитаты
	return re.findall(r'^(\s*>\s*)(.+?)$',string)[0][1]

def ampersandReplace(string):
	# замена амперсандов в строках
	while True:
		if re.search(r'\&(?!\S+?;)',string)!=None:
			string=re.sub(r'\&(?!\S+?;)','&amp;',string)
		else:
			break
	return string

def anglebrackReplace(string):
	string=string.replace('<','&lt;')
	string=string.replace('>','&gt;')
	return string

def replaceAll(string):
	string=ampersandReplace(string)
	string=anglebrackReplace(string)
	return string

def convertMonotype(string):
	# по сути функция преобразует строку, помеченную как моноширинная в 
	# размеченный код, но по упрощённым правилам
	result="" # сюда помещаем результат
	mode={"oprt":False} # встретили ли мы оператор
	# паттерны для удобства
	oprt_regex=re.compile(r'^\s*?(\*|\$)?[a-zA-Z]+') # паттерн правильного оператора, переменной
	sign_regex=re.compile(r'^\[.*\]$') # какой-то тег или другое значение в квадртаных скобках
	text_regex=re.compile(r'^(\'|\").*?\1') # паттерн строкового значения
	dlmt_regex=re.compile(r'^\[|\]|\(|\)|\{|\}|\&amp;') # патерн разделителя типа скобки
	num_regex=re.compile(r'^\d+') # патерн числа
	while len(string)>0:
		# код выполняется, пока длина строки больше нуля
		if oprt_regex.match(string)!=None:
			# строка начинается с оператора или имени переменной
			word=oprt_regex.match(string).group(0)
			string=string[len(word):]
			result+=convertOperator(word)
			mode["oprt"]=True
		elif mode["oprt"]==False and sign_regex.match(string)!=None:
			word=sign_regex.match(string).group(0)
			string=string[len(word):]
			result+=f'<span class="emTEXT">{word}</span>'
		elif text_regex.match(string)!=None:
			word=text_regex.match(string).group(0)
			string=string[len(word):]
			result+=f'<span class="emTEXT">{word}</span>'
		elif dlmt_regex.match(string)!=None:
			word=dlmt_regex.match(string).group(0)
			string=string[len(word):]
			result+=f'<span class="emOPRT">{word}</span>'
		elif num_regex.match(string)!=None:
			word=num_regex.match(string).group(0)
			string=string[len(word):]
			result+=f'<span class="emNUM">{word}</span>' 
		else:
			result+=string
			string=""
	return f'<span class="em_BLCK">{result}</span>'

def convertOperator(string):
	oprt=re.search(r'\s*?(?i:(exec|set|let|local|view|inclib|freelib|addqst|openqst|opengame|savegame|killqst|cmdclr|cmdclear|all|close|exit|play|settimer|menu|unsel|unselect|jump|copyarr|delact|wait|killall|dynamic|killvar|delobj|addobj|killobj|cls|cla|gs|xgt|gt|goto|gosub|xgoto|refint|showobjs|showstat|showacts|showinput|msg|act|if|elseif|else|loop|while|step|end|\*?(pl?|nl|clr|clear)))',string)
	func=re.search(r'\s*?(?i:(obj|isplay|len|rgb|msecscount|no|and|mod|countobj|instr|isnum|val|loc|or|ra?nd|arrsize|arrpos|arrcomp|strcomp|strpos|\$?(input|user_text|usrtxt|desc|maintxt|stattxt|qspver|curloc|selobj|selact|curacts|mid|(u|l)case|trim|replace|getobj|str|strfind|iif|dyneval|func|max|min|arritem)))',string)
	varname=re.search(r'\s*?(?i:(nosave|disablescroll|disablesubex|debug|usehtml|(b|f|l)color|fsize|\$?(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)))',string)
	if oprt!=None:
		return f'<span class="emOPRT">{string}</span>'
	elif func!=None:
		return f'<span class="emFUNC">{string}</span>'
	elif varname!=None:
		return f'<span class="emVAR">{string}</span>'
	else:
		return string

def convertCodeBlock(string_list):
	new_string_list=[]
	#print(string_list)
	# конвертируем блок кода в строку
	codemarker=re.findall(r'```(\w+)',string_list[0])
	if len(codemarker)>0:
		type_code=codemarker[0] # получаем тип кода
	else:
		type_code=""
	if type_code=="qsp":
		new_string_list=convertCodeQSP(string_list[1:])
	elif type_code=="css":
		new_string_list=convertCodeCSS(string_list[1:])
	elif type_code=="html":
		new_string_list=convertCodeHTML(string_list[1:])
	else:
		new_string_list=string_list[1:]
	return new_string_list
	
def convertCodeQSP(string_list):
	text=""
	for i in string_list:
		text+=replaceAll(i)
	result=""
	mode={"comment_open":False,"comment_quotes":False,"comment_brackets":False,"quotes-type":"","brackets-count":0}
	while len(text)>0:
		# print([text])
		# print(f'>>>comment_open:{mode["comment_open"]}')
		if mode["comment_open"]==True:
			# если включен режим извлечения комментария
			if mode["comment_quotes"]==True:
				# получаем весь текст до закрывающего символа
				comment_start=re.match(r'^[\s\S]*?('+mode["quotes-type"]+'|$)',text)
				# поскольку встречен закрывающий смивол, можно закрыть кавычку
				# print(f'>>> 2:{comment_start.group(0)}')
				mode["comment_quotes"]=False
				mode["quotes-type"]=""
				word=comment_start.group(0)
				text=text[len(word):]
				result+=replaceSpace(word)
			elif mode["comment_brackets"]==True:
				# в этом режиме мы можем встретить как открывающий так и закрывающий символ
				comment_start=re.match(r'^[\s\S]*?(\{|\}|\"|\'|$)',text)
				# print(f'>>> 3:{comment_start.group(0)},{comment_start.group(1)}')
				if comment_start.group(1)=="'" or comment_start.group(1)=='"':
					# если попадается кавычка, включаем режим распознавания кавычек.
					mode["comment_quotes"]=True
					mode["quotes-type"]=comment_start.group(1)
					word=comment_start.group(0)
					text=text[len(word):]
					result+=replaceSpace(word)
				elif comment_start.group(1)=="{":
					# если попадается скобка, открываем новую скобку
					mode["comment_brackets"]=True
					word=comment_start.group(0)
					text=text[len(word):]
					result+=replaceSpace(word)
					mode['brackets-count']+=1
				elif comment_start.group(1)=="}":
					word=comment_start.group(0)
					text=text[len(word):]
					result+=replaceSpace(word)
					mode['brackets-count']-=1
					if mode['brackets-count']<1:
						mode["comment_brackets"]=False
			elif mode["comment_quotes"]==False:
				# получаем весь текст до открывающего символа
				comment_start=re.match(r'^[^\'\"\{]*([\'\"\{]|$)',text)
				# print(f'>>> 0:{comment_start.group(0)}')
				if '\n' in comment_start.group(0):
					# если в строке есть переход на новую строку
					# значит можно закрыть комментарий здесь
					word=comment_start.group(0)
					idx=word.index('\n')
					word=word[:word.index('\n')+1]
					# print(f">>>word:{word},index:{idx}")
					text=text[len(word):]
					result+=f'{replaceSpace(word[:-1])}</span>{word[-1:]}'
					mode["comment_open"]=False
				else:
					# если до кавычки/скобки не встретилось перехода на новую строку
					if comment_start.group(1)=="'" or comment_start.group(1)=='"':
						mode["comment_quotes"]=True
						mode["quotes-type"]=comment_start.group(1)
						word=comment_start.group(0)
						text=text[len(word):]
						result+=replaceSpace(word)
					elif comment_start.group(1)=="{":
						mode["comment_brackets"]=True
						word=comment_start.group(0)
						text=text[len(word):]
						result+=replaceSpace(word)
						mode['brackets-count']+=1
		else:
			pref=re.match(r'^\s+',text)
			convention=re.match(r'^(\[команда.*?\]|\[\#.*?\]|\[\$.*?\]|\[аргумент.*?\])',text)
			oprt=re.match(r'^(\*|\$)?[a-zA-Z]\w*',text)
			if oprt!=None:
				oprt=convKeyWord(oprt.group(0),'prove')
			varname=re.match(r'^\$?[a-zA-Zа-яА-я]\w*\b',text)
			operacion=re.match(r'^\-|\=|\+|\*|\/|\[|\]|\{|\}|\(|\)|\:|\&amp;|,|&lt;|&gt;',text)
			numeric=re.match(r'^\d+',text)
			comment_sign=re.match(r'^!',text)
			string_sign=re.match(r'^(\"|\')[\s\S]*?\1',text)
			location_start=re.match(r'^(\s*?#\s?.+)(\n|$)',text)
			location_end=re.match(r'^(--.*?)(\n|$)',text) # конец локации только с двух минусов
			unfunc=re.match(r'^\@[\w\.\#]+\b',text)
			markup=re.match(r'^:[^\s\'\"\{\}\&]+',text)
			if pref!=None:
				tab=pref.group(0)
				text=text[len(tab):]
				result+=replaceSpace(tab)
			elif markup!=None:
				word=markup.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-Markup">{replaceSpace(word)}</span>'
			elif convention!=None:
				word=convention.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-Command">{replaceSpace(word)}</span>'
			elif oprt!=None:
				word=oprt.group(0)
				text=text[len(word):]
				result+=convKeyWord(word,'get')
			elif unfunc!=None:
				word=unfunc.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-UnFunc">{word}</span>'
			elif varname!=None:
				word=varname.group(0)
				text=text[len(word):]
				result+=word
			elif operacion!=None:
				word=operacion.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-Operator">{word}</span>'
			elif numeric!=None:
				word=numeric.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-Numeric">{word}</span>'
			elif string_sign!=None:
				word=string_sign.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-String">{replaceSpace(word)}</span>'
			elif location_start!=None:
				word=location_start.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-StartLoc">{replaceSpace(location_start.group(1))}</span>\n'
			elif location_end!=None:
				word=location_end.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-EndLoc">{replaceSpace(location_end.group(1))}</span>\n'
			elif comment_sign!=None:
				mode["comment_open"]=True
				word=comment_sign.group(0)
				text=text[len(word):]
				result+=f'<span class="Monokai-Comment">{word}'
			else:
				word=replaceSpace(text)
				text=""
				result+=word
	result=result.replace('\n','<br>\n')
	new_string_list=result.split('\n')
	index=0
	while index<len(new_string_list):
		new_string_list[index]+='\n'
		index+=1
	new_string_list.insert(0,'<div class="Monokai-Code">\n')
	new_string_list.append('\n</div>\n')
	return new_string_list

def convKeyWord(string,mode):
	# mode: get - получить форматирование, prove - проверить оператор
	oprt=re.match(r'\s*?(?i:(exec|set|let|local|view|inclib|freelib|addqst|openqst|opengame|savegame|killqst|cmdclr|cmdclear|all|close|exit|play|settimer|menu|unsel|unselect|jump|copyarr|delact|wait|killall|dynamic|killvar|delobj|addobj|killobj|cls|cla|gs|xgt|gt|goto|gosub|xgoto|refint|showobjs|showstat|showacts|showinput|msg|\*?(pl?|nl|clr|clear)))\b',string)
	koprt=re.match(r'\s*?(?i:(act|if|elseif|else|loop|while|step|end))\b',string)
	func=re.match(r'\s*?(?i:(obj|isplay|len|rgb|msecscount|no|and|mod|countobj|instr|isnum|val|loc|or|ra?nd|arrsize|arrpos|arrcomp|strcomp|strpos|\$?(input|user_text|usrtxt|desc|maintxt|stattxt|qspver|curloc|selobj|selact|curacts|mid|(u|l)case|trim|replace|getobj|str|strfind|iif|dyneval|func|max|min|arritem)))\b',string)
	varname=re.match(r'\s*?(?i:(nosave|disablescroll|disablesubex|debug|usehtml|(b|f|l)color|fsize|\$?(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)))\b',string)
	# print (f'{string}:{oprt},{koprt},{func},{varname}')
	if mode=="get":
		if oprt!=None:
			return f'<span class="Monokai-Operator">{string}</span>'
		elif koprt!=None:
			return f'<span class="Monokai-Koperator">{string}</span>'
		elif func!=None:
			return f'<span class="Monokai-Func">{string}</span>'
		elif varname!=None:
			return f'<span class="Monokai-SysVar">{string}</span>'
		else:
			return string
	elif mode=="prove":
		if oprt!=None:
			return oprt
		elif koprt!=None:
			return koprt
		elif func!=None:
			return func
		elif varname!=None:
			return varname
		else:
			return None

def convertCodeCSS(string_list):
	# конвертер CSS-кода
	text=""
	for i in string_list:
		text+=replaceAll(i)
	result=""
	mode={"open_selector":False}
	while len(text)>0:
		pref=re.match(r'^\s+',text)
		comment_block=re.match(r'^\/\*[\s\S]*?\*\/',text)
		if mode["open_selector"]==False:
			selector=re.match(r'^([^\{]+)(\{)',text)
			selector_end=None
			prop=None
		else:
			selector=None
			selector_end=re.match(r'^\}',text)
			prop=re.match(r'^([^\s\:][^\:]+)(:)([^;]*)(;)',text)
		if pref!=None:
			tab=pref.group(0)
			text=text[len(tab):]
			result+=replaceSpace(tab)
		elif comment_block!=None:
			word=comment_block.group(0)
			text=text[len(word):]
			result+=f'<span class="Monokai-Comment">{replaceSpace(word)}</span>'
		elif selector!=None:
			word=selector.group(0)
			text=text[len(word):]
			sel=selector.group(1)
			brack=selector.group(2)
			result+=f'<span class="Monokai-Markup">{replaceSpace(sel)}</span>'
			result+=f'{replaceSpace(brack)}'
			mode["open_selector"]=True
		elif selector_end!=None:
			word=selector_end.group(0)
			text=text[len(word):]
			result+=f'{replaceSpace(word)}'
			mode["open_selector"]=False
		elif prop!=None:
			word=prop.group(0)
			ppty=prop.group(1)
			ddot=prop.group(2)
			volm=prop.group(3)
			coma=prop.group(4)
			text=text[len(word):]
			result+=f'<span class="Monokai-Construct">{replaceSpace(ppty)}</span>'
			result+=f'<span class="Monokai-Command">{replaceSpace(ddot)}</span>'
			result+=f'<span class="Monokai-Numeric">{replaceSpace(volm)}</span>'
			result+=f'<span class="Monokai-Command">{replaceSpace(coma)}</span>'
		else:
			word=replaceSpace(text)
			text=""
			result+=word
	result=result.replace('\n','<br>\n')
	new_string_list=result.split('\n')
	index=0
	while index<len(new_string_list):
		new_string_list[index]+='\n'
		index+=1
	new_string_list.insert(0,'<div class="Monokai-Code">\n')
	new_string_list.append('\n</div>\n')
	return new_string_list

def convertCodeHTML(string_list):
	# конвертер CSS-кода
	text=""
	for i in string_list:
		text+=replaceAll(i)
	result=""
	mode={"open_tag":False}
	while len(text)>0:
		pref=re.match(r'^\s+',text)
		comment_block=re.match(r'^\&lt;!--[\s\S]*?--\&gt;',text)
		if mode["open_tag"]==False:
			ltb=re.match(r'^(\&lt;\/?)(\s*[A-Za-zА-Яа-я]\w*)',text)
			rtb=None
			prop=None
			other=re.match(r'[\s\S]+?((?=\&lt;)|$)',text)
		else:
			ltb=None
			rtb=re.match(r'^\/?\&gt;',text)
			prop=re.match(r'^([\w-]+\s*)(=\s*)(\".*?\"|\'.*?\'|\S+)',text)
			other=None
		if pref!=None:
			tab=pref.group(0)
			text=text[len(tab):]
			result+=replaceSpace(tab)
		elif comment_block!=None:
			word=comment_block.group(0)
			text=text[len(word):]
			result+=f'<span class="Monokai-Comment">{replaceSpace(word)}</span>'
		elif ltb!=None:
			word=ltb.group(0)
			text=text[len(word):]
			lt=ltb.group(1)
			tag_name=ltb.group(2)
			result+=f'{replaceSpace(lt)}'
			result+=f'<span class="Monokai-TagName">{replaceSpace(tag_name)}</span>'
			mode["open_tag"]=True
		elif rtb!=None:
			word=rtb.group(0)
			text=text[len(word):]
			result+=f'{replaceSpace(word)}'
			mode["open_tag"]=False
		elif prop!=None:
			word=prop.group(0)
			ppty=prop.group(1)
			ddot=prop.group(2)
			volm=prop.group(3)
			text=text[len(word):]
			result+=f'<span class="Monokai-Markup">{replaceSpace(ppty)}</span>'
			result+=f'{replaceSpace(ddot)}'
			result+=f'<span class="Monokai-String">{replaceSpace(volm)}</span>'
		elif other!=None:
			word=other.group(0)
			text=text[len(word):]
			result+=f'{replaceSpace(word)}'
		else:
			word=replaceSpace(text)
			text=""
			result+=word
	result=result.replace('\n','<br>\n')
	new_string_list=result.split('\n')
	index=0
	while index<len(new_string_list):
		new_string_list[index]+='\n'
		index+=1
	new_string_list.insert(0,'<div class="Monokai-Code">\n')
	new_string_list.append('\n</div>\n')
	return new_string_list

def convertListBlock(string_list,base):
	# конвертируем блок списка в html-список
	string_array=[] # массив для выборки строк
	for string in string_list:
		# перебираем строки и разбираем их по принципу: тип, уровень, строка
		t,l,s=getLi(string)
		string_array.append([t,l,s])
	blocks=splitLiBlocks(string_array,base) # разбиваем список на блоки
	new_string_list=[]
	for block in blocks:
		# конвертируем блоки в строки HTML
		if type(block)==list:
			print(block)
		else:	
			new_string_list.extend(block.getHTML(base))
	return new_string_list

def getStringLevel(string):
	level=0
	leveling=re.match(r'^\s+',string)
	if leveling!=None:
		level=len(leveling.group(0))
	return level

def minLiLevel(string_array):
	level=None
	count=0
	for t,l,s in string_array:
		if (level==None or level>l) and t!=None:
			level=l
			count+=1 # сколько раз встречается максимальный уровень
	return level,count

def getLi(string):
	# конвертируем строку в тип списка уровень пункта и непосредственно строку
	leveling=re.match(r'^(\s*?\*\s|\s*?\d+\.\s)([\s\S]*)',string)
	if leveling!=None:
		marker=re.match(r'^(\s*?)\*\s',string)
		number=re.match(r'(\s*?)\d+\.\s',string)
		if marker!=None:
			tp='marked'
			level=len(marker.group(1))
		elif number!=None:
			tp='numered'
			level=len(number.group(1))
		string=leveling.group(2)
	else:
		tp=None
		level=-1
	return tp,level,string

def splitLiBlocks(string_array,base):
	# функция разбивает список исходных строк на одноуровневые блоки
	level,count=minLiLevel(string_array)
	buffer=[]
	tp=None
	blocks=[]
	for t,l,s in string_array:
		# набираем первые блоки
		if t!=None:
			# для строк с определённым типом
			if l==level:
				# если уровни совпадают
				if tp!=t and len(buffer)!=0:
					# если типы не совпадают и в буфере что-то есть
					blocks.append(NewLiBlock(tp,buffer,base)) # создаём блок из буфера
					buffer=[[t,l,s]] # буфер теперь содержит лишь текущую строку
					tp=t
				elif tp!=t:
					# если типы не совпадают, но в буфере ничего нет
					tp=t # выставляем новый тип
					buffer.append([t,l,s]) # в буфер добавляем строку
				else:
					# если типы совпадают, просто добавляем строку в буфер
					buffer.append([t,l,s])
			elif l!=level:
				# если уровни не совпадают
				buffer.append([t,l,s])
		else:
			# для строк с неопределённым типом
			if level==None:
				# если уровень получен не был, все строки являются строками с неопределённым типом
				blocks.append([t,l,s])
			elif getStringLevel(s)<level:
				# если уровень такой строки меньше текущего, эта строка так же способствует разделению блока
				if len(buffer)==0:
					# буфер пуст, возвращаем строку
					blocks.append([t,l,s])
				else:
					# буфер не пуст, превращаем буфер в блок, строку возвращаем
					blocks.append(NewLiBlock(tp,buffer,base))
					buffer=[]
					blocks.append([t,l,s])
			else:
				# если уровень строки равен текущему или больше него, строка попадает в буфер
				buffer.append([t,l,s])
	# последний набранный буфер превращаем в блок
	if len(buffer)!=0:
		if tp!=None:
			blocks.append(NewLiBlock(tp,buffer,base))
		else:
			blocks.extend(buffer)
	return blocks # возвращаем список блоков









if __name__=="__main__":
	db=NewDataBase()
	db.setCurFile('00000000')
	string=f'`Обработка локации`, `посещение локации` — под этими терминами[:faq_09_08] понимаются следующие процессы: выполнение кода из поля "Выполнить при\n `&` посещении" указанной <локации>, добавление `mass["35,56"]` в окно основного описания. `goto` `xgoto` Всякое такое. ["Разница между `goto` и `gosub`"](#faq_01_08). Спасибо `Nex`у. `Larson`у.'
	string_obj=NewString(string,'string',db)
	print(string_obj.getHTML())