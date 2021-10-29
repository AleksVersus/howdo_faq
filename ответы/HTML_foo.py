# вспомогательные функции, стандартные
import os, random, re

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
				result+=f'<span class="Monokai-UnFunc">{replaceSpace(word)}</span>'
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

if __name__=="__main__":
	with open('.\\92_дополнительные тексты\\пример кода.qsps','r',encoding='utf-8') as file:
		string_list=file.readlines()
	text_list=convertCodeQSP(string_list[1:])
	for i in text_list:
	 	print(i)