import sys, os, re, json
import random

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
	def currentFile(self):
		# получаем идентификатор текущего файла
		return self.curfile
	def proveAdd(self):
		# присутствует ли в базе добавочная секция
		if len(self.addition)!=0:
			return True
		else:
			return False
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
		id_=self.genNewID() # генерируем идентификатор файла
		self.filecount+=1 # увеличиваем счётчик
		self.files_dict[path]=id_ # вносим файл в словарь
		self.curfile=id_ # текущим файлом становится добавленный
	def addAnchor(self,anchor):
		# добавляем якорь к файлу
		if self.curfile!="":
			self.anchors_dict[anchor]=self.curfile
		else:
			print("Ошибка! Текущий Файл не определён. Якорь <<anchor>> не добавлен")
	def getFileID(self,path):
		# получаем айди файла по указанному пути
		return self.files_dict[path]
	def getFilePath(self,id_):
		# получаем путь к файлу по ай-ди
		for key in self.files_dict:
			if self.files_dict[key]==id_:
				return key
				break
	def getFileName(self,anchor):
		# получаем айди файла по содержащемуся в нём якорю
		if anchor in self.anchors_dict:
			return self.anchors_dict[anchor]
		else:
			return ''

