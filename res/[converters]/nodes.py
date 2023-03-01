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
		elif self.node_type == 'segment':
			self.segment_stn()
		elif self.node_type == 'quote':
			self.segment_stn()
		elif self.node_type == 'head':
			self.head_stn()
		elif self.node_type == 'list-node':
			self.list_stn()
		elif self.node_type == 'code':
			self.code_stn()
		elif self.node_type == 'string':
			self.string_stn()

	def create_node(self, string_lines, node_type='segment', attributes=None):
		if len(string_lines)>0:
			node = NewNode(node_type=node_type)
			node.add_source(string_lines)
			node.source_to_nodes()
			if attributes in not None: node.attributes.update(attributes)
			string_lines = []
			self.add_node(node)

	def creat_simple_string(self, string_line:str):
		if len(string_line)>0:
			self.create_node([string_line], node_type='tag', attributes={'name': 'simple-string'})

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

		if not len(string_lines) in (len(self.string_lines), 0):
			self.create_node(string_lines)
		else:
			top_head_level = self.top_head_level(string_lines)
			if top_head_level<7:
				# break on sections
				mode = {"code-block-open": False, 'head-block-open':False}
				string_lines = []
				for line in self.string_lines:
					string_type = self.string_type(line)
					if all((
						string_type == 'head', # head
						self.get_head_level(line, result_type='num')==top_head_level, # top level
						not mode['code-block-open'] # non code
					)):
						if len(string_lines)>0:
							if not mode['head-block-open']:
								self.create_node(string_lines, node_type='segment')
							else:
								self.create_node(string_lines, node_type='head')
						string_lines.append(line)
						mode['head-block-open']=True
					elif string_type == 'id' and mode['head-block-open']:
						string_lines.append(line)
						self.create_node(string_lines, node_type='head')
						mode['head-block-open']=False
					elif string_type == 'code':
						string_lines.append(line)
						mode['code-block-open'] = not mode['code-block-open']
					elif mode['head-block-open']:
						self.create_node(string_lines, node_type='head')
						string_lines.append(line)
						mode['head-block-open']=False
					else:
						string_lines.append(line)

		if not len(string_lines) in (len(self.string_lines), 0):
			self.create_node(string_lines)
		else:
			# If node not broke on segments-nodes, break node in other types nodes.
			# Manage information:
			block_mode='' # mode of addition in blocks
			manage_mode={

				# "string-type": ("which block-types it is may close.") 
				"head":('','quote-list','ul-ol-list','head-block'),
				"id": ('head-block','quote-list'),
				"ul-ol":('','quote-list','head-block'),
				"code":('','code-block','head-block','quote-list'),
				"quote":('','quote-block','head-block','quote-list'),
				"quote-line":('','head-block'),
				"empty":('head-block','quote-list','ul-ol-list'),
				"other":('head-block','quote-list')
			}
			block_to_node = {
				'': 'segment',
				'head-block': 'head',
				'quote-list': 'quote',
				'quote-block': 'quote',
				'ul-ol-list': 'list-node',
				'code-block': 'code'
			}
			mode = {'code-block-open': False, 'code-type': None}
			string_lines = []
			for line in self.string_lines:
				string_type = self.string_type(line)
				if (string_type in ('ul-li','ol-li')):
					if block_mode in manage_mode["ul_ol"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode="ul-ol-list"
					else:
						string_lines.append(line)
				elif string_type=='code':
					if block_mode=='code-block':
						self.create_node(
							string_lines,
							node_type=block_to_node[block_mode],
							attributes={'code-type': mode['code-type']}
						)
						block_mode=''
						mode['code-type'] = None
					elif block_mode in manage_mode["code"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode = "code-block"
						mode['code-type'] = self.get_code_type(line)
					else:
						string_lines.append(line)
					mode['code-block-open'] = not mode['code-block-open']
				elif string_type=='quote':
					if block_mode=='quote-block':
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode=''
					elif block_mode in manage_mode["quote-block"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode="quote-block"
					else:
						string_lines.append(line)
				elif string_type=='quote-line':
					if block_mode=="quote-list":
						string_lines.append(self.clear_quote_string(line))
					elif block_mode in manage_mode["quote-line"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						string_lines.append(self.clear_quote_string(line))
						block_mode="quote-list"
					else:
						string_lines.append(line)
				elif string_type=='empty':
					if block_mode in manage_mode['empty'] and not mode['code-block-open']:
						# empty line don't abort code-block in other blocks
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode=''
					elif block_mode=='':
						pass
					else:
						string_lines.append(line)
				else:
					if block_mode in manage_mode["other"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode=''
					else:
						string_lines.append(line)

		if not len(string_lines) in (len(self.string_lines), 0):
			self.create_node(string_lines)
		elif len(string_lines)>0:
			# self.string_lines = string_lines and >0
			# Each string is node!
			while len(self.string_lines)>0:
				line = self.string_lines.pop(0)
				self.create_node([line], node_type='string')

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

	def list_stn(self):
		string_lines = []
		top_list_level = self.top_list_level(self.string_lines)
		mode = {'ul-block-open': False, 'ol-block-open': False, 'code-block-open':False}
		for line in self.string_lines:
			string_type = self.string_type(line)
			string_level = self.get_string_level(line)
			if all((
					string_type in ('ul-li', 'ol-li'),
					string_level == top_list_level,
					not mode['code-block-open']
				)):
				if self.all_modes_same(mode):
					if string_type=='ul-li':
						mode['ul-block-open']=True
						self.attributes['list-type']='ul-list'
					if string_type=='ol-li':
						mode['ol-block-open']=True
						self.attributes['list-type']='ol-list'
				self.create_node(string_lines)
				string_lines.append(self.clear_li_string(line))
			elif string_type == 'code':
				string_lines.append(line)
				mode['code-block-open'] = not mode['code-block-open']
			else:
				string_lines.append(line)
		self.create_node(string_lines)

	def code_stn(self):
		# Code-block is prepared node for convertion.
		# Clear the strings from space.
		top_level = 999999
		string_lines = []
		while len(self.string_lines)>0:
			line = self.string_lines.pop(0).replace('\t', ' '*4)
			level = self.get_string_level(line)
			top_level = (level if level<top_level else top_level)
			string_lines.append(line)
		regex = re.compile(r'^\s{'+str(top_level)+r'}([\s\S]*)')
		while len(string_lines)>0:
			line = re.match(regex, string_lines.pop(0)).group(1)
			self.string_lines.append(line)

	def string_stn(self):
		if len(self.string_lines)>0:
			line = self.string_lines.pop(0)
			while len(line)>0:
				scope_type, scope, line = find_separate_scope(line)
				if scope_type=='anchor':
					self.node_type='tag'
					self.attributes={
						'name': 'anchor',
						'anchor': self.extract_anchor(scope)
					}
				elif scope_type=='hr':
					self.node_type='tag'
					self.attributes={'name': 'hr'}
				elif scope_type=='image':
					text, href = self.extract_href(scope)
					self.node_type='tag'
					self.attributes={
						'name': 'image',
						'src': href
					}
				else:
					scope_type, prev_line, scope, line = self.find_overlap_scope(line)
					if scope_type is None:
						# simple-string
						self.node_type='tag'
						self.attributes={'name': 'simple-string'}
						self.string_lines.append(line)
						line=''
					elif scope_type=='hyperlink':
						self.creat_simple_string(prev_line)
						text, href = self.extract_href(scope)
						self.create_node(
							[text],
							node_type='tag',
							attributes={'name': 'hyperlink', 'href': href}
						)
					elif scope_type in ('tt-quote', 'back-apostroph'):
						self.creat_simple_string(prev_line)
						scope = self.extract_tt_quote(scope, scope_type)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'tt'}
						)
					elif scope_type=='bold-italic':
						self.creat_simple_string(prev_line)
						scope = self.extract_bold_italic(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'bold-italic'}
						)
					elif scope_type=='bold':
						self.creat_simple_string(prev_line)
						scope = self.extract_bold(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'bold'}
						)
					elif scope_type=='italic':
						self.creat_simple_string(prev_line)
						scope = self.extract_italic(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'italic'}
						)
					else:
						# simple-string
						self.node_type='tag'
						self.attributes={'name': 'simple-string'}
						self.string_lines.append(line)
						line=''
		else:
			print(f"String is not exists.")

	# ------------------------------- static methods ---------------------------

	@staticmethod
	def extract_href(string_line:str):
		match_in = re.match(r'\[(.*?)\]\((.*?)\)', string_line)
		return match_in.group(1), match_in.group(2)

	@staticmethod
	def extract_tt_quote(string_line:str, mode:str):
		if mode=='tt-quote':
			return re.match(r"''(.*?)''", string_line).group(1)
		else:
			return re.match(r"`(.*?)`", string_line).group(1)

	@staticmethod
	def extract_bold_italic(string_line:str):
		return re.match(r"\*\*\*(.*?)\*\*\*", string_line).group(1)

	@staticmethod
	def extract_bold(string_line:str):
		return re.match(r"\*\*(.*?)\*\*", string_line).group(1)

	@staticmethod
	def extract_italic(string_line:str):
		return re.match(r"\*(.*?)\*", string_line).group(1)

	@staticmethod
	def find_separate_scope(string_line:str):
		# Get string. Return scope_type, scope, other_string
		anchor = re.match(r'^\[:.*?\]$', string_line)
		image = re.match(r'^\[%image%\]\(.*?\)$', string_line)
		hr = re.match(r'^\[%hr%\]$', string_line)
		if anchor!=None:
			return 'anchor', string_line, ''
		elif image!=None:
			return 'image', string_line, ''
		elif hr!=None:
			return 'hr', string_line, ''
		else:
			return None, None, string_line

	@staticmethod
	def find_overlap_scope(string_line:str):
		# Get string. Return scope_type, scope, other_string
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'tt-quote',
				'back-apostroph',
				'bold-italic',
				'bold',
				'italic',
				'hyperlink'
			],
			"scope-regexp":
			[
				re.search(r'(\'\')(.*?)(\1)', string_line),
				re.search(r'(`)(.*?)(\1)', string_line),
				re.search(r'(\*\*\*)(.*?)(\1)', string_line),
				re.search(r'(\*\*)(.*?)(\1)', string_line),
				re.search(r'(\*)(.*?)(\1)', string_line),
				re.search(r'\[(.*?)\]\((.*?)\)', string_line)
			],
			"scope-instring":
			[]
		}
		for string_id in mini_data_base['scope-name']:
			i = mini_data_base['scope-name'].index(string_id)
			match_in = mini_data_base['scope-regexp'][i]
			mini_data_base['scope-instring'].append(
				string_line.index(match_in.group(0)) if match_in is not None else maximal)
		minimal = min(mini_data_base['scope-instring'])
		if minimal!=maximal:
			i = mini_data_base['scope-instring'].index(minimal)
			scope_type = mini_data_base['scope-name'][i]
			scope = mini_data_base['scope-regexp'][i].group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def match_in_string(string_line:str):
		match_in = re.search(r'((\'\'|`|\*\*\*|\*\*|\*)(.*?)(\2)|\[.*?\]\(.*?\))', string_line)
		return True	if match_in is not None else False

	@staticmethod
	def extract_anchor(string_line):
		return re.match(r'^(\[:)(.+?)(\])$', string_line).group(2)

	@staticmethod
	def get_head_text(string_line):
		return re.match(r'^(={1,2}|-{1,2}|\+{1,2})(.+?)(\1)$', string_line).group(2)

	@staticmethod
	def get_head_level(string_line:str, result_type='tag'):
		if not result_type in ('tag', 'num'): return None
		if re.match(r'^==.*?==$',string_line)!=None:
			return {'tag':'h1', 'num':1}[result_type]
		elif re.match(r'^=.*?=$',string_line)!=None:
			return {'tag':'h2', 'num':2}[result_type]
		elif re.match(r'^--.*?--$',string_line)!=None:
			return {'tag':'h3', 'num':3}[result_type]
		elif re.match(r'^-.*?-$',string_line)!=None:
			return {'tag':'h4', 'num':4}[result_type]
		elif re.match(r'^\+\+.*?\+\+$',string_line)!=None:
			return {'tag':'h5', 'num':5}[result_type]
		elif re.match(r'^\+.*?\+$',string_line)!=None:
			return {'tag':'h6', 'num':6}[result_type]
		else:
			return None

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
				string_line = string_line.lower().replace(translator['cyr'][i], translator['lat'][i])
				i+=1
			string_line = re.sub(r'[^\w\-\s]', '', string_line)
		return string_line

	@staticmethod
	def string_type(string_line:str):
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

	@staticmethod
	def all_modes_same(mode:dict, all_values=False):
		return all(tuple([value==all_values for value in mode.values()]))

	@staticmethod
	def top_head_level(string_lines:list):
		top_level = 7
		mode = {"code-block-open": False}
		for line in string_lines:
			if self.string_type(line)=='head' and not mode['code-block-open']:
				level = self.get_head_level(line, result_type='num')
				top_level = (level if level < top_level else top_level)
			elif self.string_type(line)=='code':
				mode['code-block-open'] = not mode['code-block-open'] 
		return top_level

	@staticmethod
	def clear_quote_string(string_line:str):
		return re.match(r'^(\s*>\s*)(.+?)$', string_line).group(2)

	@staticmethod
	def get_string_level(string_line:str):
		leveling=re.match(r'^\s+', string_line)
		return (0 if (leveling is None) else len(leveling.group(0)))

	@staticmethod
	def top_list_level(string_lines:list, get_string_level=get_string_level, string_type=string_type):
		top_level=999999
		for line in string_lines:
			if string_type(line) in ('ol-li', 'ul-li'):
				level = get_string_level(line)
				top_level = (level if level<top_level else top_level)
		return top_level

	@staticmethod
	def clear_li_string(string_line:str):
		return re.match(r'^(\s*(\*|\d+\.)\s+)(.+?)$', string_line).group(3)

	@staticmethod
	def get_code_type(string_line:str):
		return re.match(r'^\s*```(\w+)\s*$', string_line).group(1)

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


