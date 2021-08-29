import sys, os, re, json

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

class NewString():
	def __init__(self,string_,type_,base_):
		self.source=string_
		self.type=type_
		self.strings=[]
		print(f"'type:{self.type},string: {string_}'")
		if self.type=='':
			pass
		elif self.type=='string':
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
def convertString(string_,type_,base_):
	# конвертируем строку в параграф
	roof_string=NewString(string_,type_,base_)


		

if __name__=="__main__":
	string=f'`Обработка локации`, `посещение локации` — под этими терминами понимаются следующие процессы: выполнение кода из поля "Выполнить при посещении" указанной локации, добавление в окно основного описания. `goto` `xgoto` Всякое такое. ["Разница между `goto` и `gosub`"](#faq_01_08). Спасибо `Nex`у. `Larson`у.'
	NewString(string,'string',[1,2,3])