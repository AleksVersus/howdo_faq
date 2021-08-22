import sys, os, re, json
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
		return 'subtitle'
	elif re.match(r'^\s*<section_of_head>\s*$',string_)!=None:
		return 'section_of_head-open'
	elif re.match(r'^\s*</section_of_head>\s*$',string_)!=None:
		return 'section_of_head-close'
	elif re.match(r'^\[:.*?\]$',string_)!=None:
		return 'id'
	else:
		return 'other'

def getTitle(string_):
	return re.findall(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$',string_)[0][1]

def getID(string_):
	return re.findall(r'(\[:)(.+?)(\])',string_)[0][1]

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

def getStringList(files_list):
	string_list=[] # локальная переменная
	mode={"comment":False,"code":False}
	# используем список файлов, чтобы генерировать секции
	for file in files_list:
		# открываем каждый файл последовательно
		with open(file,'r',encoding='utf-8') as this_file:
			string_list.extend(this_file.readlines())
	# после того, как мы выбрали строки из файлов, перебираем их
	# чтобы удалить комментарии везде, кроме блоков кода
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
			# любая не пустая строка добавляется в новый список
			if re.match(r'^\s+?$',string_)!=None:
				# если строка состоит из одних пробелов, это пустая строка
				string_=""
			if string_!="" and string_!=None:
				new_string_list.append(string_) 
	return new_string_list

def ampersandReplace(string_):
	# замена амперсандов в строках
	while True:
		if re.search(r'\&(?!\w+;)',string_)!=None:
			string_=re.sub(r'\&(?!\w+;)','&amp;',string_)
		else:
			break
	return string_
class NewString():
	def __init__(self,string_,**args_):
		self.type="" # по типу определяем, что это за строка (например <title>)
		self.string_body=[] # список объектов
		if args_['start']==True:
			# заголовок рассматривается только если строка приходит первый раз
			title=re.match(r'^\s*(<title>)(.*?)(</title>)\s*$',string_) # заголовок ли?
		else:
			title=None
		hyperlink=re.match(r'^\[[^\]]+\]\([^\)]*\)$',string_) # есть ли гиперссылки
		if title!=None:
			# если это строка заголовок
			self.type='title'
			string_=re.match(r'^\s*(<title>)(.*?)(</title>)\s*$',string_)[0][1]
			string_body.append(NewString(string_))
		elif hyperlink!=None:
			# если строка является гиперссылкой
def convertString(string_):
	title_string=[]
	varname=NewString(string_,start=True)
	link_list=re.findall(r'\[[^\]]+\]\([^\)]*\)',title)
	for link in link_list:
		symbol=title.find(link)
		title_string.append(title[0:symbol])
		title_string.append(title[symbol:symbol+len(link)])
		title=title[symbol+len(link):]
	title=""
	for i in title_string:
		title+=f"{i}\n"
	return title
	
def convertationFB2(body_list):
	# данная функция конвертирует перворазбитый список строк в готовый документ fb2
	new_string_list=[] # выходной список строк
	mode={} # словарь режимов
	for string_ in body_list:
		body=re.match(r'^\s*</?body(\s+[^>]*?)?>\s*$',string_)
		section=re.match(r'^\s*</?section(\s+[^>]*?)?>\s*$',string_)
		title=re.match(r'^\s*<title>.*?</title>\s*$',string_)
		if body!=None:
			new_string_list.append(string_)
		elif section!=None:
			new_string_list.append(string_)
		elif title!=None:
			new_string_list.append(convertString(string_))
	return new_string_list

if __name__=="__main__":
	print(convertTitle("<title>[название ссылки](#link_01_01)Есть просто символ &. Есть в слове &ghjk. А есть &nbsp; [https://www.youtube.com/watch?v=uaEfDzBXFSw&](https://www.youtube.com/watch?v=uaEfDzBXFSw&list=PLcAHO4WsUl2R70UDclnyevDSuBJGDH9F6&index=1&t=25s) ещё часть строки</title>"))