import sys, os, re, json
import random

def randomString(length):
	letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
	letters+='ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю'
	result = ''.join(random.choice(letters) for i in range(length))
	return result

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

def remComment(string_):
	mode_=False
	start_string=''
	end_string=''
	start_comment=re.match(r'.*?/\*.*',string_)
	if start_comment!=None:
		start_string,comm,string_=re.findall(r'(.*?)(/\*)(.*)',string_)[0]
		mode_=True
	end_comment=re.match(r'.*?\*/.*',string_)
	if end_comment!=None:
		string_,comm,end_string=re.findall(r'(.*?)(\*/)(.*)',string_)[0]
		mode_=False
	return mode_,start_string+end_string

def clearStringList(string_list):
	# удаляем комментарии везде, кроме блоков кода
	mode={"comment":False,"code":False}
	new_string_list=[]
	for string_ in string_list:
		comment=re.match(r'(.*?/\*.*)|(.*?\*/.*)',string_)
		code=re.match(r'^\s*?```\w*\s*$',string_)
		if mode["comment"]==True and comment==None:
			pass # строки комментария не добавляются в новый список
		elif mode["code"]==True and code==None:
			# строки в блоках кода добавляются без изменений
			new_string_list.append(string_) 
		elif comment!=None and mode["code"]==False:
			# если строка содержит комментарий, а режим кода выключен
			# изменяем режим и получаем строку без комментария
			mode["comment"],string_=remComment(string_)
			if re.match(r'^\s+?$',string_)!=None:
				# если строка состоит из одних пробелов, это пустая строка
				string_=""
			if string_!="" and string_!=None:
				new_string_list.append(string_) 
		elif code!=None and mode["comment"]==False:
			# если строка содержит границу блока кода, но не включён режим комментария
			if mode["code"]==False:
				mode["code"]=True
			else:
				mode["code"]=False
			# строка при этом добавляется в выходной список
			if re.match(r'^\s+?$',string_)!=None:
				# если строка состоит из одних пробелов, это пустая строка
				string_=""
			if string_!="" and string_!=None:
				new_string_list.append(string_) 
		else:
			if string_!=None:
				new_string_list.append(string_) 
	return new_string_list
def typeString(string):
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
def getTitle(string_):
	return re.findall(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$',string_)[0][1]

def getID(string_):
	return re.findall(r'(\[:)(.+?)(\])',string_)[0][1]

def ampersandReplace(string_):
	# замена амперсандов в строках
	while True:
		if re.search(r'\&(?!\S+?;)',string_)!=None:
			string_=re.sub(r'\&(?!\S+?;)','&amp;',string_)
		else:
			break
	return string_

def anglebrackReplace(string_):
	string_=string_.replace('<','&lt;')
	string_=string_.replace('>','&gt;')
	return string_

def replaceAll(string_):
	string_=ampersandReplace(string_)
	string_=anglebrackReplace(string_)
	return string_

def replaceSpace(string_):
	string_=string_.replace('\t','&nbsp;'*4)
	string_=string_.replace(' ','&nbsp;')
	return string_

def convOPRT(string_):
	oprt=re.search(r'\s*?(?i:(exec|set|let|local|view|inclib|freelib|addqst|openqst|opengame|savegame|killqst|cmdclr|cmdclear|all|close|exit|play|settimer|menu|unsel|unselect|jump|copyarr|delact|wait|killall|dynamic|killvar|delobj|addobj|killobj|cls|cla|gs|xgt|gt|goto|gosub|xgoto|refint|showobjs|showstat|showacts|showinput|msg|act|if|elseif|else|loop|while|step|end|\*?(pl?|nl|clr|clear)))',string_)
	func=re.search(r'\s*?(?i:(obj|isplay|len|rgb|msecscount|no|and|mod|countobj|instr|isnum|val|loc|or|ra?nd|arrsize|arrpos|arrcomp|strcomp|strpos|\$?(input|user_text|usrtxt|desc|maintxt|stattxt|qspver|curloc|selobj|selact|curacts|mid|(u|l)case|trim|replace|getobj|str|strfind|iif|dyneval|func|max|min|arritem)))',string_)
	varname=re.search(r'\s*?(?i:(nosave|disablescroll|disablesubex|debug|usehtml|(b|f|l)color|fsize|\$?(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)))',string_)
	if oprt!=None:
		return f'<span class="emOPRT">{string_}</span>'
	elif func!=None:
		return f'<span class="emFUNC">{string_}</span>'
	elif varname!=None:
		return f'<span class="emVAR">{string_}</span>'
	else:
		return string_

def convKeyWord(string_):
	oprt=re.match(r'\s*?(?i:(exec|set|let|local|view|inclib|freelib|addqst|openqst|opengame|savegame|killqst|cmdclr|cmdclear|all|close|exit|play|settimer|menu|unsel|unselect|jump|copyarr|delact|wait|killall|dynamic|killvar|delobj|addobj|killobj|cls|cla|gs|xgt|gt|goto|gosub|xgoto|refint|showobjs|showstat|showacts|showinput|msg|\*?(pl?|nl|clr|clear)))',string_)
	koprt=re.match(r'\s*?(?i:(act|if|elseif|else|loop|while|step|end))',string_)
	func=re.match(r'\s*?(?i:(obj|isplay|len|rgb|msecscount|no|and|mod|countobj|instr|isnum|val|loc|or|ra?nd|arrsize|arrpos|arrcomp|strcomp|strpos|\$?(input|user_text|usrtxt|desc|maintxt|stattxt|qspver|curloc|selobj|selact|curacts|mid|(u|l)case|trim|replace|getobj|str|strfind|iif|dyneval|func|max|min|arritem)))',string_)
	varname=re.match(r'\s*?(?i:(nosave|disablescroll|disablesubex|debug|usehtml|(b|f|l)color|fsize|\$?(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)))',string_)
	# print (f'{string_}:{oprt},{koprt},{func},{varname}')
	if oprt!=None:
		return f'<span class="Monokai-Operator">{string_}</span>'
	elif koprt!=None:
		return f'<span class="Monokai-Koperator">{string_}</span>'
	elif func!=None:
		return f'<span class="Monokai-Func">{string_}</span>'
	elif varname!=None:
		return f'<span class="Monokai-SysVar">{string_}</span>'
	else:
		return string_

def convertMonotype(string_):
	result=""
	mode={"oprt":False}
	while len(string_)>0:
		if re.match(r'^\s*?(\*|\$)?[a-zA-Z]+',string_)!=None:
			word=re.match(r'^\s*?(\*|\$)?[a-zA-Z]+',string_).group(0)
			string_=string_[len(word):]
			result+=convOPRT(word)
			mode["oprt"]=True
		elif mode["oprt"]==False and re.match(r'^\[.*\]$',string_)!=None:
			word=re.match(r'^\s*?(\*|\$)?[a-zA-Z]+',string_).group(0)
			string_=string_[len(word):]
			result+=f'<span class="emTEXT">{word}</span>'
		elif re.match(r'^(\'|\").*?\1',string_)!=None:
			word=re.match(r'^(\'|\").*?\1',string_).group(0)
			string_=string_[len(word):]
			result+=f'<span class="emTEXT">{word}</span>'
		elif re.match(r'^\[|\]|\(|\)|\{|\}|\&amp;',string_)!=None:
			word=re.match(r'^\[|\]|\(|\)|\{|\}|\&amp;',string_).group(0)
			string_=string_[len(word):]
			result+=f'<span class="emOPRT">{word}</span>'
		elif re.match(r'^\d+',string_)!=None:
			word=re.match(r'^\d+',string_).group(0)
			string_=string_[len(word):]
			result+=f'<span class="emNUM">{word}</span>' 
		else:
			result+=string_
			string_=""
	return f'<span class="em_BLCK">{result}</span>'

class NewString():
	def __init__(self,string_,type_,base_):
		self.source=string_
		self.type=type_
		self.strings=[]
		if self.type=='string':
			termins=re.match(r'^\s*?`.*?`(,\s+`.*?`)*\s*—',string_)
			if termins!=None:
				word1=termins.group(0)
				word2=string_[len(word1):]
				self.strings.append(NewString(word1,'termins',base_))
				self.strings.append(NewString(word2,'',base_))
			else:
				self.strings.append(NewString(string_,'',base_))
		elif self.type=='termins':
			termins=re.findall(r'`.+?`',string_)
			for term in termins:
				symbol=string_.find(term)
				word1=string_[0:symbol]
				word2=string_[symbol:symbol+len(term)]
				if word1!="":
					self.strings.append(NewString(word1,'',base_))
				self.strings.append(NewString(word2[1:-1],'term',base_))
				string_=string_[symbol+len(term):]
			if len(string_)>0:
				self.strings.append(NewString(string_,'',base_))
		elif self.type=='term':
			self.strings.append(NewString(string_,'',base_))
		elif self.type=='hyperlink':
			hl_text,hl_href=re.findall(r'^\[(.*?)\]\((.*?)\)$',string_)[0]
			self.strings.append(NewString(hl_text,'',base_)) # текст ссылки в нулевой ячейке
			if re.match(r'^#',hl_href)!=None:
				hl_href='#folder#'+base_.searchFile(section_id=hl_href[1:],result='file_id')+'.html'+hl_href
			self.strings.append(NewString(hl_href,'href',base_)) # адрес в первой
		elif self.type=='href':
			# если тип строки href, дальше она не изменяется
			pass
		elif self.type=='name':
			y_name,y_sub=re.findall(r'`([^`]+)`(\w+)\b',string_)[0]
			self.strings.append(NewString(y_name,'authname',base_)) # текст ссылки в нулевой ячейке
			self.strings.append(NewString(y_sub,'authsub',base_)) # текст ссылки в нулевой ячейке
		elif self.type=='id':
			pass
		else:
			id_word=re.search(r'\[:[^\]]*?\]',string_)
			link_word=re.search(r'\[[^\]]*?\]\(.*?\)',string_)
			name_word=re.search(r'`[^`\s]+?`\w+\b',string_)
			monotype_word=re.search(r'`[^`]+?`',string_)
			if id_word!=None:
				words=re.findall(r'\[:[^\]]*?\]',string_)
				for word in words:
					symbol=string_.find(word)
					word1=string_[0:symbol]
					word2=string_[symbol:symbol+len(word)]
					if word1!="":
						self.strings.append(NewString(word1,'',base_))
					self.strings.append(NewString(getID(word2),'id',base_))
					string_=string_[symbol+len(word):]
				if len(string_)>0:
					self.strings.append(NewString(string_,'',base_))
			elif link_word!=None:
				words=re.findall(r'\[[^\]]*?\]\(.*?\)',string_)
				for word in words:
					symbol=string_.find(word)
					word1=string_[0:symbol]
					word2=string_[symbol:symbol+len(word)]
					if word1!="":
						self.strings.append(NewString(word1,'',base_))
					self.strings.append(NewString(word2,'hyperlink',base_))
					string_=string_[symbol+len(word):]
				if len(string_)>0:
					self.strings.append(NewString(string_,'',base_))
			elif name_word!=None:
				words=re.findall(r'`[^`\s]+?`\w+\b',string_)
				for word in words:
					symbol=string_.find(word)
					word1=string_[0:symbol]
					word2=string_[symbol:symbol+len(word)]
					if word1!="":
						self.strings.append(NewString(word1,'',base_))
					self.strings.append(NewString(word2,'name',base_))
					string_=string_[symbol+len(word):]
				if len(string_)>0:
					self.strings.append(NewString(string_,'',base_))
			elif monotype_word!=None:
				words=re.findall(r'`[^`]+?`',string_)
				for word in words:
					symbol=string_.find(word)
					word1=string_[0:symbol]
					word2=string_[symbol:symbol+len(word)]
					if word1!="":
						self.strings.append(NewString(word1,'',base_))
					self.strings.append(NewString(word2[1:-1],'monotype',base_))
					string_=string_[symbol+len(word):]
				if len(string_)>0:
					self.strings.append(NewString(string_,'',base_))
			else:
				# если в строке не обнаружено вложений, она не разбивается
				self.source=replaceAll(self.source)	
	def getHTML(self):
		if len(self.strings)>0:
			# print(f"'type:{self.type},len:{len(self.strings)}'")
			text=""
			if self.type=="hyperlink":
				# в нулевой ячейке лежит текст ссылки
				text+=f'<a href="{self.strings[1].getHTML()}" style="text-decoration:none;" class="emFOLD">{self.strings[0].getHTML()}</a>'
			elif self.type=="name":
				# в нулевой ячейке лежит текст ссылки
				text+=f'<strong>{self.strings[0].getHTML()}</strong>\'{self.strings[1].getHTML()}'
			elif self.type=="term":
				for string in self.strings:
					text+=string.getHTML()
				text=f'<strong>{text}</strong>'
			else:
				for string in self.strings:
					text+=string.getHTML()
			return text
		else:
			# print(f"'type:{self.type},src:{self.source}'")
			if self.type=="monotype":
				return convertMonotype(self.source)
			elif self.type=="term":
				return f'<strong>{self.source}</strong>'
			elif self.type=='id':
				return f'<a id="{self.source}"></a>'
			else:
				return self.source

def getLi(string_):
	# конвертируем строку в тип списка уровень пункта и непосредственно строку
	leveling=re.match(r'^(\s*?\*\s|\s*?\d+\.\s)([\s\S]*)',string_)
	if leveling!=None:
		marker=re.match(r'^(\s*?)\*\s',string_)
		number=re.match(r'(\s*?)\d+\.\s',string_)
		if marker!=None:
			type_='marked'
			level_=len(marker.group(1))
		elif number!=None:
			type_='numered'
			level_=len(number.group(1))
		string_=leveling.group(2)
	else:
		type_=None
		level_=-1
	return type_,level_,string_

def getStringLevel(string_):
	level=0
	leveling=re.match(r'^\s+',string_)
	if leveling!=None:
		level=len(leveling.group(0))
	return level

def convertString(string_,type_,base_):
	# конвертируем строку в размченную
	roof_string=NewString(string_,type_,base_)
	return roof_string.getHTML()

def convertCodeBlock(string_list):
	new_string_list=[]
	#print(string_list)
	# конвертируем блок кода в строку
	type_code=re.findall(r'```(\w+)',string_list[0])[0] # получаем тип кода
	text=""
	for i in string_list[1:]:
		text+=i
	result=""
	mode={"comment_open":False,"comment_quotes":False,"comment_brackets":False,"quotes-type":"","brackets-count":0}
	while len(text)>0:
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
			oprt=re.match(r'^(\*|\$)?[a-zA-Z]\w+',text)
			varname=re.match(r'^[a-zA-Zа-яА-я]\w+\b',text)
			operacion=re.match(r'^\=|\+|\*|\/|\[|\]|\{|\}|\(|\)|\:|\&|,|<|>',text)
			numeric=re.match(r'^\d+',text)
			comment_sign=re.match(r'^!',text)
			string_sign=re.match(r'^(\"|\').*?\1',text)
			location_start=re.match(r'^(\s*?#\s?.+)(\n|$)',text)
			location_end=re.match(r'^(-.*?)(\n|$)',text)
			unfunc=re.match(r'^\@[\w\.\#]+\b',text)
			if pref!=None:
				tab=pref.group(0)
				text=text[len(tab):]
				result+=replaceSpace(tab)
			elif oprt!=None:
				word=oprt.group(0)
				text=text[len(word):]
				result+=convKeyWord(word)
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
	return new_string_list

class NewLi():
	# пункт списка
	def __init__(self,source_list):
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
				self.include.extend(splitLiBlocks(self.source))
				self.source=[]
			else:
				# если максимальный уровень не найден, разбить на блоки нельзя
				self.include.extend(self.source)
				self.source=[]
	def getHTML(self,base_):
		new_string_list=[]
		new_string_list.append('<li>\n')
		for els in self.include:
			if type(els)==list:
				# если типом является строка
				t,l,s=els
				if t==None:
					br='<br>'
				else:
					br=''
				new_string_list.append(br+convertString(s,'string',base_))
			else:
				# если тип элемента - NewLiBlock
				new_string_list.extend(els.getHTML(base_))
		new_string_list.append('</li>\n')
		return new_string_list

class NewLiBlock():
	# секция списка!
	def __init__(self,type_,source_list):
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
				print(f'[{self.id}]\t{t},{l},{s[:-1]}')
				if l==level:
					# если совпадают уровни
					print('levels right')
					if len(buffer)!=0:
						# если в буфере что-то есть, отправляем буфер в пункт
						print('create new LI')
						self.include.append(NewLi(buffer))
					# сам буфер теперь содержит только указанный исходник
					print('new buffer')
					buffer=[[t,l,s]]
				else:
					# если уровни не совпадают, добавляем в буфер исходник
					print('add in buffer')
					buffer.append([t,l,s])
	def __str__(self):
		text=f'type:{self.type} source.len:{len(self.source)}'
		return text
	def printAll(self):
		pass
	def getHTML(self,base_):
		new_string_list=[]
		# Блоки бывают только двух типов, третьего не дано
		if self.type=='marked':
			new_string_list.append('<ul>\n')
		elif self.type=='numered':
			new_string_list.append('<ol>\n')
		for li_point in self.include:
			print(type(li_point))
			new_string_list.extend(li_point.getHTML(base_))
		if self.type=='marked':
			new_string_list.append('</ul>\n')
		elif self.type=='numered':
			new_string_list.append('</ol>\n')
		return new_string_list

def minLiLevel(string_array):
	level=None
	count=0
	for t,l,s in string_array:
		if (level==None or level>l) and t!=None:
			level=l
			count+=1 # сколько раз встречается максимальный уровень
	return level,count

def splitLiBlocks(string_array):
	# функция разбивает список исходных строк на одноуровневые блоки
	level,count=minLiLevel(string_array)
	buffer=[]
	tp=None
	blocks=[]
	for t,l,s in string_array:
		# набираем первые блоки
		print([f'type:{t}/{tp} level:{l}/{level} string:{s}'])
		if t!=None:
			# для строк с определённым типом
			if l==level:
				# если уровни совпадают
				if tp!=t and len(buffer)!=0:
					# если типы не совпадают и в буфере что-то есть
					blocks.append(NewLiBlock(tp,buffer)) # создаём блок из буфера
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
					blocks.append(NewLiBlock(tp,buffer))
					buffer=[]
					blocks.append([t,l,s])
			else:
				# если уровень строки равен текущему или больше него, строка попадает в буфер
				buffer.append([t,l,s])
	# последний набранный буфер превращаем в блок
	if len(buffer)!=0:
		t,l,s=buffer[0]
		blocks.append(NewLiBlock(t,buffer))
	return blocks # возвращаем список блоков

def convertListBlock(string_list,base_):
	# конвертируем блок списка в html-список
	# print(string_list)
	string_array=[]
	level=None
	for string in string_list:
		t,l,s=getLi(string)
		string_array.append([t,l,s])
	blocks=splitLiBlocks(string_array)
	new_string_list=[]
	for block in blocks:
		print(block)
		new_string_list.extend(block.getHTML(base_))
	return new_string_list



if __name__=="__main__":
	# string=f'`Обработка локации`, `посещение локации` — под этими терминами[:faq_09_08] понимаются следующие процессы: выполнение кода из поля "Выполнить при\n `&` посещении" указанной <локации>, добавление `mass["35,56"]` в окно основного описания. `goto` `xgoto` Всякое такое. ["Разница между `goto` и `gosub`"](#faq_01_08). Спасибо `Nex`у. `Larson`у.'
	roof_base=NewBD()
	roof_base.addFile('path',section_id='faq_01_08')
	# print(convertString(string,'string',roof_base))
	with open('.\\92_дополнительные тексты\\пример списка.light-txt','r',encoding='utf-8') as file:
		string_list=file.readlines()
	text_list=convertListBlock(string_list,roof_base)
	for i in text_list:
	 	print(i)