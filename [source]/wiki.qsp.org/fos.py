# Files Operation System
# постоянно приходится писать заново получение структуры файлов и папок, чтобы потом применять к ним какие-либо скритпы
# нужна система, которая сможет получить структуру файлов и папок универсальным способом
# и которая затем сможет применять к ним различные операции в зависимости от требуемых нужд
import sys, os, json
import re
import datetime

def fullZero(string,num_lenght,zero='0',dir_='left'):
	string=str(string)
	if dir_=='left':
		return str(zero)*(num_lenght-len(string))+string
	elif dir_=='right':
		return string+str(zero)*(num_lenght-len(string))
	else:
		return string

def mid(string,start,*fin):
	if start!=None:
		first=int(start)-1
		if first<0: first=0
	else:
		first=0
	if fin[0]!=None:
		last=int(fin[0])
	else:
		last=len(string)
	return string[first:last]

def transliterate(string):
	string=string.lower()
	sword={"а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ё":"io","ж":"zh","з":"z","и":"i","й":"j","к":"k","л":"l","м":"m","н":"n"
	,"о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"h","ц":"ts","ч":"ch","ш":"sh","щ":"sch","ъ":"_","ы":"y","ь":"_",
	"э":"a","ю":"ju","я":"ja"," ":"_"}
	text=""
	for i in string:
		if not i in sword:
			text+=i
		else:
			text+=sword[i]
	return text

def getTimeMark():
	dt = datetime.datetime.now()
	return dt.strftime("%Y_%m_%d_%H_%M_%S_%f")

class NewFolder():
	"""Данный класс позволяет получить папку, как объект, включающий все вложенные в неё файлы и папки"""
	def __init__(self,folder_path):
		self.path=folder_path # folder_path — должен быть абсолютным путём
		self.folders=[] # вложенные папки
		self.files=[] # вложенные файлы
		cmdir=os.listdir(self.path) #
		for i in cmdir:
			pt=f"{self.path}\\{i}"
			if os.path.isdir(pt):
				self.folders.append(NewFolder(pt))
			elif os.path.isfile(pt):
				self.files.append(NewFile(pt))
	def getText(self):
		strings=[self.path+'\n']
		for folder in self.folders:
			strings.extend(folder.getText())
		for file in self.files:
			strings.append(file.getText())
		return strings
	def renameFiles(self,level=None,filt=None,mask="[NT4].[E]",start_counter=None,test=False):
		# print('fold',filt,mask)
		global counter
		if start_counter!=None: counter+=start_counter
		if level==None or level>0:
			if level!=None: level-=1
			for folder in self.folders:
				folder.renameFiles(level=level,filt=filt,mask=mask,test=test)
			for file in self.files:
				file.rename(filt=filt,mask=mask,test=test)
	def foundCount(self,start=False,filt=None):
		# функция отыскивает порядковые номера всех файлов
		numbers_list=[]
		for folder in self.folders:
			numbers_list.extend(folder.foundCount(filt=filt))
		for file in self.files:
			numbers_list.append(file.foundCount(filt=filt))
		if start==False:
			return numbers_list
		else:
			# если в параметре start передан True, значит это первая вызываемая папка
			# она должна вернуть список совпадающих номеров и самый большой номер
			i=0
			double_list=[]
			maxnum=0
			for number in numbers_list:
				if (i+1)!=len(numbers_list):
					# мы имеем дело не с последним элементом списка
					if number in numbers_list[i+1:]:
						# если элемент встречается в списке повторно, добавляем его в список дубликатов
						double_list.append(number)
					if int(number)>maxnum: maxnum=int(number) # если число записанное здесь больше уже найденного максимального
				i+=1
			return [maxnum, double_list]
	def getFilesList(self,level=None,filt=None):
		# print('fold',filt,mask)
		files_list=[]
		if level==None or level>0:
			if level!=None: level-=1
			for folder in self.folders:
				files_list.extend(folder.getFilesList(level=level,filt=filt))
			for file in self.files:
				temp=file.getFilePath(filt=filt)
				if temp!=None: files_list.append(temp)
		return files_list
				

class NewFile():
	def __init__(self,file_path):
		self.path=file_path # абсолютный путь к файлу
		self.folder,self.name = os.path.split(self.path) # папка, в которой лежит файл и само имя файла
	def getText(self):
		return self.path+'\n'
	def isRightName(self,filt=None):
		if filt!=None:
			if filt[-3:]=='/re':
				filt=filt[:-3]
				if re.search(filt,self.name)==None: return False
			else:
				if not filt in self.name: return False
		return True
	def rename(self,filt=None,mask="[NT4].[E]",test=False):
		# filt - это фильтр имени файла. Может быть регулярным выражением, тогда последние три символа должны быть ключом /re
		if self.isRightName(filt=filt):
			global counter
			counter_change=False
			name,ext=os.path.splitext(self.name)
			ext=ext[1:]
			run=True
			# print(name,ext,mask)
			while run:
				tick=0
				n=re.search(r'\[N(T?)((\d+)(-(\d+))?)?\]',mask)
				e=re.search(r'\[E\]',mask)
				d=re.search(r'\[D\]',mask)
				c=re.search(r'\[(C+)\]',mask)
				if n!=None:
					name=mid(name,n.group(3),n.group(5))
					if n.group(1)!=None: name=transliterate(name)
					mask=mask.replace(n.group(0),name)
					tick+=1
				if e!=None:
					mask=mask.replace(e.group(0),ext)
					tick+=1
				if d!=None:
					mask=mask.replace(d.group(0),getTimeMark())
					tick+=1
				if c!=None:
					if not counter_change:
						counter+=1
						counter_change=True
					mask=mask.replace(c.group(0),fullZero(counter,len(c.group(1))))
					tick+=1
				# print(mask)
				if tick==0: run=False
			self.name=mask
			old_path=self.path
			self.path=f"{self.folder}\\{self.name}"
			if not test:
				os.rename(old_path, self.path)
	def getFilePath(self,filt=None):
		if self.isRightName(filt=filt):
			return self.path
	def foundCount(self,filt=None):
		if self.isRightName(filt=filt):
			count=re.search(r'_(\d+)$',os.path.splitext(self.name)[0]) # выдёргиваем из имени последнюю часть, т.е. порядковый номер
			if count!=None:
				return count.group(1)
			else:
				return '-1'
		else:
			return '-1'


def main_rename(folder):
	with open('file_1.txt-light','w',encoding='utf-8') as file:
	 	file.writelines(folder.getText())
	folder.renameFiles(filt=r"(^.{3,}\.txt-light$|^[^0]{2}$)/re",mask="[NT]_[CCCC].[E]")
	with open('file_2.txt-light','w',encoding='utf-8') as file:
	 	file.writelines(folder.getText())

if __name__=="__main__":
	counter=-1
	folder = NewFolder("D:\\my\\projects\\howdo_faq\\[source]\\wiki.txt\\help")
	folder.renameFiles(filt=r"(^.{3,}\.txt-light$|^[^0]{2}$)/re",mask="help_[N].[E]")
	# main_rename(folder) # пакетное переименовывание всех файлов
	# print(folder.foundCount(start=True,filt=r"(^.{3,}\.txt-light$|^[^0]{2}$)/re")) # поиск конечного счётчика
	# print(folder.getFilesList(filt=r"(^.{3,}\.txt-light$|^[^0]{2}$)/re"))

	


# описание маски (mask)
# [N] - имя файла без расширения
# [NT] - имя файла без расширения но транслитом (в eng)
# [N4-8] - вырезаем из имени файла с четвёртого по восьмой символ включительно
# [NT4] - вырезаем из имени файла все символы с четвёртого и транслетируем
# [E] - вставляем текущее расширение файла
# [D] - вставляем временную метку в название файла в формате 2022_09_08_15_55_05_635789
# [C] - глобальный счётчик. Указание разрядности идёт через повтор символа C: [CC] [CCCC]
# чтобы счётчик стартовал не с 0, а с другого числа, передаём параметр start_counter в первую папку
# пример замены расширения файла
# filt=r".*\.light\-txt/re", mask="[N].txt-light"
# пример транслитерирования имён файлов
# filt=r".*\.txt-light/re", mask="[NT].txt-light"
# меняем названия всех файлов txt-light кроме 00.txt-light на транслетриованные плюс счётчик
# filt=r"(^.{3,}\.txt-light$|^[^0]{2}$)/re",mask="[NT]_[CCCC].[E]"

# параметры, которые принимает renameFiles() для папки
# level - глубина вложения. Это число показывает, на сколько папок вглубь применять операции. None - на всю глубину вложений
# filt - фильтр файлов по названиям. Можно использовать регулярные выражения, но такие регулярки должны заканчиваться ключом /re
# mask - маска нового имени файла, смотри выше
# start_counter - начало отсчёта для счётчика. Если не указано, счётчик стартует с нуля.
# test - примает значения False или True. Если передан True - переименование файлов осуществляется виртуально, т.е. только в объектах. 
# Чтобы файлы переименовались и физически, необходимо убрать этот параметр, или задать ему значение False