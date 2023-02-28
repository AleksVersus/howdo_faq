import sys, os, re, json
import random

"""
	Здесь мы создаём систему узлов, которую в дальнейшем можно обрабатывать в различном виде.
	По сути мы повторяем опыт beautifulsoup только без удобной html разметки в исходнике

"""

# этот класс нужен для тестов. Из финальной версии его можно убрать
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
		self.root_node = None

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
		self.root_folder = NewFolder(self.source_folder)
		self.root_node = self.root_folder.return_node()
		# self.root_folder.convert_to_html()


class NewFolder():
	"""
		NewFolder - object includes other folders and files.
	"""
	def __init__(self, folder_path):
		self.path = folder_path # folders id
		self.files = [] # includes files
		self.folders = [] # includes folders
		files_list, folders_list = self.dir_list(self.path)
		for folder in folders_list:
			self.folders.append(NewFolder(folder))
		for file in files_list:
			self.files.append(NewFile(file))

	def dir_list(self, folder_path):
		files_list = []
		folders_list = []
		paths_list = os.listdir(folder_path)
		for path in paths_list:
			if os.path.isfile(folder_path+"\\"+path) and os.path.splitext(path)[1]=='.txt-light':
				files_list.append(folder_path+"\\"+path)
			elif os.path.isdir(folder_path+"\\"+path):
				folders_list.append(folder_path+"\\"+path)
		return files_list, folders_list

	def print_includes(self, counter=1):
		"""Function for control files-sctructure"""
		text='\t'*counter + self.path+'\n'
		for folder in self.folders:
			text+=folder.print_includes(counter=counter+1)
		for file in self.files:
			text+="\t"*(counter+1)+file.path+'\n'
		return text

	def return_node(self):
		if len(self.files)>0 or len(self.folders)>0:
			node = NewNode(node_type='folder')
			for file in self.files:
				file_node = file.return_node()
				if file_node is not None:
					node.add_node(file_node)
			for folder in self.folders:
				folder_node = folder.return_node()
				if folder_node is not None:
					node.add_node(folder_node)
			if node.get_nodes_count()!=0:
				return node
			else:
				return None
		else:
			return None

class NewFile():
	"""
		NewFile - objects, contains file's contents
	"""
	def __init__(self, file_path):
		self.path = file_path
		with open(self.path, 'r', encoding='utf-8') as file:
			self.source_lines = file.readlines()

	def get_file_name(self, mode='short'):
		if mode in ('full', ''):
			return os.path.split(self.path)[1]
		elif mode in ('short'):
			return os.path.splitext(os.path.split(self.path)[1])[0]

	def return_node(self):
		node = None
		if self.get_file_name()=='00.txt-light':
			node = NewNode(node_type='head')
		else:
			node = NewNode(node_type='file')
		node.add_source(self.source_lines)
		node.source_to_nodes()

class NewNode():
	"""
		NewNode - it is objects for convertation.
		types:
		folder - узел папки
		file - узел файла
		head - узел заголовка
	"""
	def __init__(self, node_type='file'):
		self.node_type = node_type
		self.includes_nodes = []
		self.source_lines = []
		self.attributes = {}

	def add_node(self, node):
		self.includes_nodes.append(node)

	def add_source(self, source_lines):
		if type(source_lines)==list:
			self.source_lines.extend(source_lines)
		elif type(source_lines)==str:
			self.source_lines.append(source_lines)

	def get_nodes_count(self):
		return len(self.includes_nodes)

	def source_to_nodes(self):
		if self.node_type == 'folder':
			# folder-nodes have not sources
			pass
		elif self.node_type == 'file':
			self.segment_stn()
		elif self.node_type == 'head':
			self.head_stn()

	def create_node(self, string_lines, node_type='segment'):
		if len(string_lines)>0:
			node = NewNode(node_type='segment')
			node.add_source(string_lines)
			node.source_to_nodes()
			string_lines = []
			self.add_node(node)

	def segment_stn(self):
		# break node on big nodes
		mode = {"code-block-open": False, "section-of-head-open": False}
		string_lines = []
		for line in self.string_lines:
			string_type = self.string_type(line)
			if string_type == 'section-of-head-open' and not mode['code-block-open']:
				self.create_node(string_lines)
				mode['section-of-head-open']=True
			elif string_type == 'section-of-head-close' and mode['section-of-head-open']:
				self.create_node(string_lines)
				mode['section-of-head-open']=False
			elif string_type == 'code' and not mode['section-of-head-open']:
				string_lines.append(line)
				mode['code-block-open'] = not mode['code-block-open']
			else:
				string_lines.append(line)

		if len(string_lines)!=len(self.string_lines):
			self.create_node(string_lines)
		else:
			# if node not broke on segments-nodes, break node in other types nodes
			mode = {
				"head-open": False,
				"code-block-open": False,
				"ul-open": False,
				"ol-open": False,
				"quote-open": False
			}
			string_lines = []
			for line in self.string_lines:
				string_type = self.string_type(line)



	def head_stn(self):
		if len(self.source_lines)==2:
				self.attributes['anchor']=self.extract_anchor(self.source_lines.pop())
		if len(self.source_lines)==1:
			string_line = self.source_lines.pop()
			self.attributes['head-level']=self.get_head_level(string_line)
			node = NewNode(node_type='string')
			string_line = get_head_text(string_line)
			node.add_source(string_line)
			node.source_to_nodes()
			self.add_node(node)
			if not 'anchor' in self.attributes:
				self.attributes['anchor']=self.translit_string(string_line)

	# ------------------------------- static methods ---------------------------

	@staticmethod
	def extract_anchor(string_line):
		return re.match(r'^(\[:)(.+?)(\])$', string_line).group(2)

	@staticmethod
	def get_head_text(string_line):
		return re.match(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$', string_line).group(2)

	@staticmethod
	def get_head_level(string_line):
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

	@staticmethod
	def translit_string(string_line, direct="cyr_to_lat"):
		translator = {
			"cyr" : [	
				" ", "ъ", "ь", "щ", "ё", "ж", "ц", "ч", "ш", "ю", "я",
				"а", "б", "в", "г", "д", "е", "з", 
				"и", "й", "к", "л", "м", "н", "о", 
				"п", "р", "с", "т", "у", "ф", "х", 
				"ы", "э"
			],
			"lat" : [
				"-", "_", "_", "sch", "io", "zh", "ts", "ch", "sh", "iu", "ia",
				"a", "b", "v", "g", "d", "e", "z", 
				"i", "j", "k", "l", "m", "n", "o", 
				"p", "r", "s", "t", "u", "f", "h", 
				"y", "e"
			]
		}
		if direct == "cyr_to_lat":
			i = 0
			for letter in translator['cyr']:
				string_line = string_line.replace(translator['cyr'][i], translator['lat'][i])
				i+=1
			string_line = re.sub(r'[^\w\-\s]', '', string_line)
		return string_line

	@staticmethod
	def string_type(string_line):
		if re.match(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$', string_line)!=None:
			return 'head'
		elif re.match(r'^\s*<section_of_head>\s*$', string_line)!=None:
			return 'section-of-head-open'
		elif re.match(r'^\s*</section_of_head>\s*$', string_line)!=None:
			return 'section-of-head-close'
		elif re.match(r'^\[:.*?\]$', string_line)!=None:
			return 'id'
		elif re.match(r'^\s*?\*\s+', string_line)!=None:
			return 'ul-li'
		elif re.match(r'^\s*?\d+\.\s+', string_line)!=None:
			return 'ol-li'
		elif re.match(r'^\s*```\w*?', string_line)!=None:
			return 'code'
		elif re.match(r'^\s*?>>>\s*?$', string_line)!=None:
			return 'quote'
		elif re.match(r'^\s*?>\s+', string_line)!=None:
			return 'quote-line'
		elif re.match(r'^\s*?$', string_line)!=None:
			return 'empty'
		else:
			return 'other'

def main():
	# названия файлов, из которых берём сборку
	html_json=[
		# "..\\..\\[source]\\готовые статьи\\html.json",
		"..\\..\\[source]\\ответы\\html.json",
		# "..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		TextToHTML(path).convert_to_html()

if __name__=="__main__":
	main()


