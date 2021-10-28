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
			string_=string_[len(word):]
			result+=f'<span class="emNUM">{word}</span>' 
		else:
			result+=string_
			string_=""
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

if __name__=="__main__":
	files_list, folders_list = dirList("D:\\my\\projects\\howdo_faq\\ответы\\80_зарезервированные слова")
	print (files_list, folders_list)