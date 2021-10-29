import sys, os, re, json
import random




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
				if l==level:
					# если совпадают уровни
					if len(buffer)!=0:
						# если в буфере что-то есть, отправляем буфер в пункт
						self.include.append(NewLi(buffer))
					# сам буфер теперь содержит только указанный исходник
					buffer=[[t,l,s]]
				else:
					# если уровни не совпадают, добавляем в буфер исходник
					buffer.append([t,l,s])
			if len(buffer)!=0:
				self.include.append(NewLi(buffer))
	def __str__(self):
		text=f'id:{self.id} type:{self.type} source.len:{len(self.source)}'
		return text
	def getHTML(self,base_):
		new_string_list=[]
		# Блоки бывают только двух типов, третьего не дано
		if self.type=='marked':
			new_string_list.append('<ul>\n')
		elif self.type=='numered':
			new_string_list.append('<ol>\n')
		for li_point in self.include:
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
		if tp!=None:
			blocks.append(NewLiBlock(tp,buffer))
		else:
			blocks.extend(buffer)
	return blocks # возвращаем список блоков

def convertListBlock(string_list,base_):
	# конвертируем блок списка в html-список
	string_array=[]
	level=None
	for string in string_list:
		t,l,s=getLi(string)
		string_array.append([t,l,s])
	blocks=splitLiBlocks(string_array)
	new_string_list=[]
	for block in blocks:
		if type(block)==list:
			print(block)
		else:	
			new_string_list.extend(block.getHTML(base_))
	return new_string_list

def convertSOHBlock(string_list,base_):
	# конвертируем блок section of head в список
	new_string_list=[]
	quazy_file=NewQuazy(string_list,base_)
	new_string_list=quazy_file.getHTML(base_)
	i=0
	for string in new_string_list:
		metahead=re.match(r'^<(/?)(h\d+)>',string)
		if metahead!=None:
			lev=int(re.search(r'\d+',metahead.group(2)).group(0))+6
			if metahead.group(1)!='/':
				new_string_list[i]=new_string_list[i].replace(metahead.group(0),f'<p class="head_{lev}">')
			else:
				new_string_list[i]=new_string_list[i].replace(metahead.group(0),f'</p>')
		i+=1
	return new_string_list

if __name__=="__main__":
	# string=f'`Обработка локации`, `посещение локации` — под этими терминами[:faq_09_08] понимаются следующие процессы: выполнение кода из поля "Выполнить при\n `&` посещении" указанной <локации>, добавление `mass["35,56"]` в окно основного описания. `goto` `xgoto` Всякое такое. ["Разница между `goto` и `gosub`"](#faq_01_08). Спасибо `Nex`у. `Larson`у.'
	# roof_base=NewBD()
	# roof_base.addFile('path',section_id='faq_01_08')
	# with open('.\\92_дополнительные тексты\\пример SOH.light-txt','r',encoding='utf-8') as file:
	# 	string_list=file.readlines()
	# text_list=convertSOHBlock(string_list[1:-1],roof_base)
	# for i in text_list:
	#  	print(i)
	pass