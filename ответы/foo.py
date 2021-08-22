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

class NewString():
	def __init__(self,string_,**args_):
		self.type="" # по типу определяем, что это за строка (например <title>)
		self.string_body=[] # список объектов
		self.last_string="" # если объекты уже нельзя сгенерировать, оставляем строку здесь
		if not 'strtype' in args_:
			args_['strtype']=''
		if args_['strtype']=='title':
			# если это строка заголовок
			self.type='title'
			string_=re.findall(r'^\s*(<title>)(.*?)(</title>)\s*$',string_)[0][1]
			self.string_body.append(NewString(string_))
		elif args_['strtype']=='hyperlink':
			# если строка является гиперссылкой
			self.type="hyperlink"
			hl_text,hl_href=re.findall(r'^\[(.*?)\]\((.*?)\)$',string_)[0]
			self.string_body.append(NewString(hl_text)) # текст ссылки в нулевой ячейке
			self.string_body.append(NewString(hl_href,strtype='href')) # адрес в первой
		elif args_['strtype']=='href':
			self.type='href'
			self.last_string=string_
		elif args_['strtype']=='monotype':
			self.type='monotype'
			self.last_string=string_
		else:
			hyperlink=re.search(r'\[(.*?)\]\((.*?)\)',string_)
			monotype=re.search(r'`[^`]+`',string_)
			if hyperlink!=None:
				# если в тексте пристутсвуют гиперссылки, разбиваем текст на части
				link_list=re.findall(r'\[[^\]]+\]\([^\)]*\)',string_)
				for link in link_list:
					symbol=string_.find(link)
					self.string_body.append(NewString(string_[0:symbol])) # простая строка
					self.string_body.append(NewString(string_[symbol:symbol+len(link)],strtype='hyperlink')) # гиперссылка
					string_=string_[symbol+len(link):]
				if len(string_)>0: self.string_body.append(NewString(string_))
			elif monotype!=None:
				# если в тексте присутствует monotype разметка
				# определяем, можно ли на лету перекрасить эту разметку
				mt_list=re.findall(r'`\w+`\w+\b',string_)
				for i in mt_list:
					y_name,y_sub=re.findall(r'`(\w+?)`(\w+)\b',i)[0]
					string_=string_.replace(i,f"{y_name}'{y_sub}")
				monotype=re.search(r'`[^`]+`',string_)
				if monotype!=None:
					mt_list=re.findall(r'`[^`]+`',string_)
					for i in mt_list:
						symbol=string_.find(i)
						self.string_body.append(NewString(string_[0:symbol])) # простая строка
						self.string_body.append(NewString(string_[symbol:symbol+len(link)],strtype='monotype'))
						string_=string_[symbol+len(link):]
					if len(string_)>0: self.string_body.append(NewString(string_))
			else:
				self.last_string=string_
	def getString(self):
		if len(self.last_string)>0:
			string_=replaceAll(self.last_string)
			if self.type=='title':
				return f'<title>{string_}</title>'
			elif self.type=='href':
				return f'<a href="{self.last_string}">'
			elif self.type=='monotype':
				return f'<strong>{string_}</strong>'
			else:
				return string_
		else:
			if self.type=='title':
				string_="<title>"
				for i in self.string_body:
					string_+=i.getString()
				string_+='</title>'
				return string_
			elif self.type=='hyperlink':
				return f'{self.string_body[1].getString()}{self.string_body[0].getString()}</a>'
			else:
				string_=""
				for i in self.string_body:
					string_+=i.getString()
				return string_

def convertString(string_,**args_):
	if not 'strtype' in args_:
		args_['strtype']=''
	varname=NewString(string_,strtype=args_['strtype'])
	return varname.getString()

	
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
			new_string_list.append(convertString(string_,strtype='title'))
	return new_string_list

if __name__=="__main__":
	string="<title>[название ссылки](#link_01_01)Есть <просто> символ &. Есть в слове &ghjk. А есть &nbsp; [https://www.youtube.com/watch?v=uaEfDzBXFSw&](https://www.youtube.com/watch?v=uaEfDzBXFSw&list=PLcAHO4WsUl2R70UDclnyevDSuBJGDH9F6&index=1&t=25s) ещё часть строки</title>"
	print(string)
	print(convertString(string,strtype='title'))