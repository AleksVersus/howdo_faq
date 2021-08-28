# Builder fb2-файла 
import sys, os, re, json # импорт необходимых модлулей
import datetime
from HTML_foo import *

class NewBD():
	def __init__(self):
		self.base=[] # база представляет собой всего лишь список записей
		self.filecount=0 # число записей в базе
	def __str__(self):
		return f"{len(self.base)} files in base. First File {self.base[0]}"
	def printBase(self):
		return self.base
	def addFile(self,path_,**args_):
		# добавляем файл в базу 
		file=[path_,self.getLastID(),""] # путь, идентификатор по порядку, идентификатор в структуре ссылок
		if "section_id" in args_:
			file[2]=args_["section_id"]
		self.base.append(file)
		self.filecount+=1
	def getLastID(self):
		lenght=8
		sfc=str(self.filecount)
		lenid=len(sfc)
		return '0'*(lenght-lenid)+sfc
	def searchFile(self,**args_):
		result=None
		for file_path,file_id,section_id in self.base:
			if ("section_id" in args_) and (section_id==args_["section_id"]):
				result=file_path,file_id,section_id
				break
			if ("file_id" in args_) and (file_id==args_["file_id"]):
				result=file_path,file_id,section_id
				break
			if ("file_path" in args_) and (file_path==args_["file_path"]):
				result=file_path,file_id,section_id
				break
		if "result" in args_:
			# если мы хотим получить какой-то определённый результат
			if args_["result"]=="file_path":
				return result[0]
			if args_["result"]=="file_id":
				return result[1]
			if args_["result"]=="section_id":
				return result[2]
			if args_["result"]=="index":
				return self.base.index(result)
		else:
			return result[0]
	def changeID(self,path_,section_id):
		idx=self.searchFile(file_path=path_,result='index')
		self.base[idx][2]=section_id

class NewFile():
	def __init__(self,path_,file_base):
		self.path=path_
		file_base.addFile(path_) # добавляем файлы в базу
		self.body=[]
		with open(path_,'r',encoding='utf-8') as file:
			self.body=file.readlines()
	def __str__(self):
		return f'File Path: {self.path}; lenght of file: {len(self.body)}.'
	def printFile(self):
		return f'"File Path: {self.path}; lenght of file: {len(self.body)}."'
	def getPath(self):
		return self.path
class NewFolder():
	"""docstring for NewFolder"""
	def __init__(self, path_,file_base):
		self.path=path_ # объект папка обладает атрибутом путь
		files_list, folders_list = dirList(path_)
		self.files=[] # атрибут file - это по сути список всех вложенных файлов
		for file in files_list:
			self.files.append(NewFile(file,file_base))
		self.folders=[] # атрибут folders - это по сути список вложенных объектов того же класса
		# перебираем все пути из списка папок и создаём на каждый по новому объекту
		for folder in folders_list:
			self.folders.append(NewFolder(folder,file_base))
	def __str__(self):
		return f'Folder Path: {self.path}; number of files: {len(self.files)}; number of includes: {len(self.folders)}.'
	def printFolder(self):
		return f'Folder Path: {self.path}; number of files: {len(self.files)}; number of includes: {len(self.folders)}.'
	def printFiles(self):
		text=""
		for i in self.files:
			text+=i.printFile()+'\n'
		return text
	def printFolders(self):
		text=""
		for i in self.folders:
			text+=i.printFolder()+"\n"
		return text
	def printAll(self):
		text=""
		for i in self.folders:
			text+=f"'Path:{i.path}'\n"
			text+=i.printAll()+'\n'
			text+="'---'\n"
		for i in self.files:
			text+=i.printFile()+'\n'
		return text
	def popString(self):
		string=self.file.pop(0)
		return typeString(string),string
	def getHTML(self,file_base):
		for file in self.files:
			# по имени файла определяем, берём ли мы из него дополнительный заголовок
			if os.path.split(file.getPath())[1]=='00.txt-light':
				print(file)
		for folder in self.folders:
			folder.getHTML(file_base)

work_dir=os.getcwd()
generate_id=0
# открываем файл проекта для чтения и получаем его структуру в переменную root
with open("html.json","r",encoding="utf-8") as project_file:
	root_dict=json.load(project_file)
project_dict=root_dict["project"] # словарь помещаем в переменную
# формируем название релизного файла
folder_path=os.path.abspath(project_dict["folder"]) # папка, из которой подтягиваем файлы
# создаём базу данных
file_base=NewBD()
# создаём объект папка верхнего уровня
roof_folder=NewFolder(folder_path,file_base)
# теперь разматываем папку и файлы, получая HTML
roof_folder.getHTML(file_base)