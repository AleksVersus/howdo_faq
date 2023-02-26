# основа конвертирования. Исключительные классы и функции для преобразования в HTML
import sys, os, re, json
import random

class TextToHTML():
	"""
		Class of Converter Object. This Class get project, prepare
		and convert list of source-files in html-files.
	"""
	def __init__(self, html_json_path):
		self.project_file = os.path.abspath(html_json_path)
		with open(self.project_file, "r", encoding="utf-8") as file:
			self.root_dict = json.load(file)
		self.project_dict = self.root_dict['project']
		self.source_folder = os.path.abspath(self.project_dict["source_folder"])
		self.output_path = os.path.abspath(self.project_dict["export_folder"])
		self.content_file_path = os.path.abspath(self.root_dict["head_contents"])
		with open(os.path.abspath(self.root_dict["head"]), 'r', encoding='utf-8') as header:
			self.header_html_lines = header.readlines()
		with open(os.path.abspath(self.root_dict["foot"]), 'r', encoding='utf-8') as footer:
			self.footer_html_lines = footer.readlines()
		self.data_base = None
		self.root_folder = None

	def make_output_folder(self):
		if not os.path.exists(self.output_path):
			os.makedirs(self.output_path)

	# def create_data_base(self):
	# 	self.data_base=NewDataBase()
	# 	self.data_base.add_header(self.header_html_lines) # верхняя часть html-документа
	# 	self.data_base.add_footer(self.footer_html_lines) # нижняя часть html-документа
	# 	self.data_base.add_output_path(self.output_path) # выходная папка
	# 	self.data_base.set_content_file_path(self.content_file_path) # содержание
	# 	self.data_base.add_crosslink_form(self.project_dict["cross-link"]) # вид перекрёстных ссылок

	def convert_to_html(self):
		self.make_output_folder()
		# self.create_data_base()
		self.root_folder = NewFolder(self.source_folder, self.data_base)
		# self.root_folder.convert_to_html()

class NewDataBase():
	"""NewDataBase — object is include descriptions of anchors and sections
	in connect with unique files/sections. Every file have unique path, 
	and every anchor is unique.
	"""
	def __init__(self):
		self.files_count = 0
		self.files_db = {
			# connect files paths and it's ids
			"files-paths": [],
			"files-ids": []
		}
		self.anchors_db = {
			# connect anchors and it's file ids
			"anchors": [],
			"files-ids": []

		}
		self.current_file_id = ""
		self.crosslink = "" # first part for crosslinks
		self.addition_section = []
		self.header_html_lines = []
		self.footer_html_lines = []
		self.content_file_path = ""
		self.content_html_lines = []
		self.output_folder_path = ""

	def print_data_base(self, mode=''):
		temp_dic = {
			"files-count": self.files_count,
			"current-file-id": self.current_file_id,
			"crosslink": self.crosslink,
			"addition-section": self.addition_section,
			"header": self.header_html_lines,
			"footer": self.footer_html_lines,
			"content-path": self.content_file_path,
			"content-html": self.content_html_lines,
			"output-folder": self.output_folder_path,
			"files-db": self.files_db,
			"anchors-db": self.anchors_db
		}
		if mode in ('', 'print'):
			print(temp_dic)
		elif mode in ('json'):
			with open('print_data_base.json', 'w', encoding='utf-8') as file:
				json.dump(temp_dic, file, indent=4)

	def get_current_file(self):
		return self.current_file_id

	def set_current_file(self, file_id):
		self.current_file_id = file_id

	def prove_addition(self):
		return (True if len(self.addition_section)!=0 else False)

	def get_addition(self):
		return self.addition_section[:1]

	def add_addition(self, source_lines):
		self.addition_section.extend(source_lines)

	def del_addition(self):
		self.addition_section=[]

	def get_last_file_id(self):
		if self.files_count==0:
			return None
		else:
			return self.files_db['files-ids'][-1]

	def gen_file_id(self):
		return '0'*(8-len(str(self.files_count)))+str(self.files_count)

	def append_file(self, file_path):
		file_id = self.gen_file_id()
		self.files_count += 1
		self.files_db['files-paths'].append(file_path)
		self.files_db['files-ids'].append(file_id)
		self.current_file_id = file_id
		return self.files_count-1

	def get_file_id(self, file_path):
		if file_path in self.files_db['files-paths']:
			self.files_db['files-ids'][self.files_db['files-paths'].index(file_path)]
		else:
			return None

	def get_file_path(self, file_id):
		if file_id in self.files_db['files-ids']:
			self.files_db['files-paths'][self.files_db['files-ids'].index(file_id)]
		else:
			return None

	def add_anchor(self, anchor):
		if self.current_file_id!="":
			self.anchors_db['anchors'].append(anchor)
			self.anchors_db['files-ids'].append(self.current_file_id)
		else:
			print("Error! Current file is not set. Anchor <<anchor>> not append.")

	def get_file_name(self, anchor):
		if anchor in self.anchors_db:
			file_id = self.anchors_db['files-ids'][self.anchors_db['anchors'].index(anchor)]
			file_path = self.files_db['files-paths'][self.files_db['files-ids'].index(file_id)]
			full_file_name = os.path.split(file_path)[1]
			file_name = os.path.splitext(full_file_name)[0]
			instr=re.match(r'\d+_',file_name)
			if instr!=None:
				file_name=file_name[len(instr.group(0)):]
			return file_name
		else:
			return None

	def add_header(self, html_lines):
		self.header_html_lines = html_lines[:]

	def add_footer(self, html_lines):
		self.footer_html_lines = html_lines[:]

	def get_header(self):
		return self.header_html_lines[:]

	def get_footer(self):
		return self.footer_html_lines[:]

	def add_output_path(self, folder_path):
		self.output_folder_path = folder_path

	def get_output_path(self):
		return self.output_folder_path

	def set_content_file_path(self, content_file_path):
		self.content_file_path = content_file_path

	def get_content_file_path(self):
		return self.content_file_path

	def add_content_lines(self, html_lines):
		self.content_html_lines = html_lines[:]

	def get_content_lines(self):
		return self.content_html_lines

	def add_crosslink_form(self, crosslink_html_string):
		self.crosslink = crosslink_html_string

	def get_cross_link(self):
		return self.crosslink

class NewFolder():
	"""
		NewFolder - object includes other folders and files.
	"""
	def __init__(self, folder_path, data_base):
		self.path = folder_path # folders id
		self.files = [] # includes files
		self.folders = [] # includes folders
		self.data_base = data_base
		files_list, folders_list = dir_list(self.path)
		for folder in folders_list:
			self.folders.append(NewFolder(folder, self.data_base))
		self.data_base.del_addition() # удаляем дополнительные заголовки перед перебором файлов <-------------
		for file in files_list:
			self.files.append(NewFile(file, self.data_base))

	# def convert_to_html(self):
	# 	for file in self.files:
	# 		file.buildThis()
	# 	for folder in self.folders:
	# 		folder.convert_to_html()

class NewFile():
	"""
		NewFile - objects, contains file's contents
	"""
	def __init__(self, file_path, data_base):
		self.path = file_path
		self.data_base = data_base
		self.file_number = None
		# with open(self.path, 'r', encoding='utf-8') as file:
		# 	self.source_lines = file.readlines()
		# self.segments = [] # сегменты, составляющие файл
		# self.html_lines = [] # список строк готового HTML-файла
		if self.get_file_name()=='00.txt-light':
			self.base.add_addition(self.source_lines)
		else:
			self.file_number = self.data_base.append_file(self.path)
			if self.data_base.prove_addition():
				self.source_lines = self.data_base.get_addition() + self.source_lines
			self.segments.append(NewSegment(self.source_lines, 'from_file', self.data_base))
			self.convert_to_html()
			if self.data_base.get_content_file_path()==self.path:
				self.data_base.add_content_lines(self.html_lines)

	def get_file_name(self):
		return os.path.split(self.path)[1]

def dir_list(folder_path):
	files_list = []
	folders_list = []
	paths_list = os.listdir(folder_path)
	for path in paths_list:
		if os.path.isfile(folder_path+"\\"+path) and os.path.splitext(path)[1]=='.txt-light':
			files_list.append(folder_path+"\\"+path)
		elif os.path.isdir(folder_path+"\\"+path):
			folders_list.append(folder_path+"\\"+path)
	return files_list, folders_list

def main():
	# названия файлов, из которых берём сборку
	html_json=[
		"..\\..\\[source]\\готовые статьи\\html.json",
		# "..\\..\\[source]\\ответы\\html.json",
		# "..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		TextToHTML(path).convert_to_html()

if __name__=="__main__":
	main()
