import sys, os, re, json
import random
import datetime
from bs4 import BeautifulSoup

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
		self.source_folder = os.path.abspath(self.root_dict["source-folder"])
		self.output_path = os.path.abspath(self.root_dict["output-folder"])

		# HTML-project
		self.project_html = self.root_dict['project-html']
		self.content_file_path = os.path.abspath(self.project_html["head-contents"])
		with open(os.path.abspath(self.project_html["head"]), 'r', encoding='utf-8') as header:
			self.header_html_lines = header.readlines()
		with open(os.path.abspath(self.project_html["foot"]), 'r', encoding='utf-8') as footer:
			self.footer_html_lines = footer.readlines()

		# FB2-project
		self.project_fb2 = self.root_dict['project-fb2']
		self.output_file_name = self.project_fb2["output-file"].replace('%TIME%',self.get_date())
		self.book_info = self.project_fb2["book-info"]
		self.binary = self.project_fb2['binary']

		self.data_base = None
		self.root_folder = None
		self.root_node = None

	def make_output_folder(self):
		if not os.path.exists(self.output_path):
			os.makedirs(self.output_path)

	def create_data_base(self):
		self.data_base=NewDataBase()
		self.data_base.add_header(self.header_html_lines) # top-part html-doc
		self.data_base.add_footer(self.footer_html_lines) # bottom-part html-doc
		self.data_base.add_output_path(self.output_path) # output-folder path
		self.data_base.set_content_file_path(self.content_file_path) # content of files
		self.data_base.add_crosslink(self.project_html["cross-link"]) # crosslinks start

	def convert_to(self):
		self.make_output_folder()
		self.create_data_base()
		self.root_folder = NewFolder(self.source_folder)
		self.root_node = self.root_folder.return_node()

		self.root_node.transport_data_base(self.data_base)
		self.root_node.convert_to_html()

		with open(self.book_info, 'r', encoding='utf-8') as file:
			header_lines = file.readlines()
		header = ''.join([line.replace(r'%TIME%', self.get_date()).replace(r'%DATE%', self.get_date(mode='xml')) for line in header_lines])
		output_fb2 = self.root_node.convert_to_fb2()
		with open(self.binary, 'r', encoding='utf-8') as file:
			footer = file.read()
		with open(f"{self.output_path}\\{self.output_file_name}", 'w', encoding='utf-8') as file:
			file.write(header+output_fb2+footer)

		output = self.root_node.test_convert()
		with open('new.xml', 'w', encoding='utf-8') as file:
			file.write(output)

	def get_date(self, **args):
		when=datetime.datetime.now()
		if not 'mode' in args:
			args['mode']=''
		month = (str(when.month) if len(str(when.month))==2 else f'0{when.month}')
		day = (str(when.day) if len(str(when.day))==2 else f'0{when.day}')
		if args['mode']!='xml':
			time=f"{when.year}.{month}.{day}"
		else:
			time=f"{when.year}-{month}-{day}"
		return time

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
		self.content_html_text = []
		self.output_folder_path = ""
		self.deep_level_head = {'h1':0, 'h2':0}

	def refresh_deep_level(self):
		self.deep_level_head = {'h1':0, 'h2':0}

	def print_data_base(self, mode=''):
		temp_dic = {
			"files-count": self.files_count,
			"current-file-id": self.current_file_id,
			"crosslink": self.crosslink,
			"addition-section": self.addition_section,
			"header": self.header_html_lines,
			"footer": self.footer_html_lines,
			"content-path": self.content_file_path,
			"content-html": self.content_html_text,
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
		return self.addition_section #html_text

	def add_addition(self, html_text):
		self.addition_section = html_text

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
			return self.files_db['files-ids'][self.files_db['files-paths'].index(file_path)]
		else:
			return None

	def get_file_number(self, file_path):
		if file_path in self.files_db['files-paths']:
			return self.files_db['files-paths'].index(file_path)
		else:
			return -1

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
		if anchor in self.anchors_db['anchors']:
			file_id = self.anchors_db['files-ids'][self.anchors_db['anchors'].index(anchor)]
			file_path = self.files_db['files-paths'][self.files_db['files-ids'].index(file_id)]
			full_file_name = os.path.split(file_path)[1]
			file_name = os.path.splitext(full_file_name)[0]
			instr=re.match(r'\d+_(.*)',file_name)
			if instr!=None:
				file_name=instr.group(1)
			return file_name
		else:
			return None

	def get_full_link_to_anchor(self, anchor:str):
		# print(f"[214] {anchor}")
		if anchor in self.anchors_db['anchors']:
			return f"{self.get_crosslink()}{self.get_file_name(anchor)}.html#{anchor}"
		else:
			return f"#{anchor}"

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

	def add_content_html_text(self, html_text):
		self.content_html_text = html_text

	def get_content_html_text(self):
		return self.content_html_text

	def add_crosslink(self, crosslink_html_string):
		self.crosslink = crosslink_html_string

	def get_crosslink(self):
		return self.crosslink

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
				node.attributes['path']=self.path
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
			self.source_lines = NewNode.comments_replace(file.readlines())

	def get_file_name(self, mode='full'):
		if mode in ('full'):
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
		node.attributes['path']=self.path
		return node

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
		self.data_base = None

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
			self.source_lines = [self.replace_specsymbols(line) for line in self.source_lines]
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
		elif self.node_type == 'tag':
			self.string_stn()
		else:
			# pass unknown types of nodes
			print(f"[333] Unknown type of node: {self.node_type}.")

	def create_node(self, string_lines, node_type='segment', attributes=None):
		if len(string_lines)>0:
			node = NewNode(node_type=node_type)
			node.add_source(string_lines)
			node.source_to_nodes()
			if attributes is not None: node.attributes.update(attributes)
			string_lines.clear()
			self.add_node(node)

	def create_simple_string(self, string_line:str):
		if len(string_line)>0:
			self.create_node([string_line], node_type='tag', attributes={'name': 'simple-string'})

	def segment_stn(self):
		# break node on big nodes
		mode = {"code-block-open": False, "section-of-head-open": False}
		string_lines = []
		for line in self.source_lines:
			string_type = self.string_type(line)
			if string_type == 'section-of-head-open' and not mode['code-block-open']:
				self.create_node(string_lines, attributes={'segment-class':'for-soh'})
				mode['section-of-head-open']=True
			elif string_type == 'section-of-head-close' and mode['section-of-head-open']:
				self.create_node(string_lines, attributes={'segment-class':'for-soh'})
				mode['section-of-head-open']=False
			elif string_type == 'code' and not mode['section-of-head-open']:
				string_lines.append(line)
				mode['code-block-open'] = not mode['code-block-open']
			else:
				string_lines.append(line)

		if not len(string_lines) in (len(self.source_lines), 0):
			self.create_node(string_lines, attributes={'segment-class':'for-soh'})
			self.source_lines = []
		else:
			top_head_level = self.top_head_level(self.source_lines)
			if top_head_level<7:
				# break on sections
				mode = {"code-block-open": False, 'head-block-open':False}
				string_lines = []
				for line in self.source_lines:
					string_type = self.string_type(line)
					if all((
						string_type == 'head', # head
						self.get_head_level(line, result_type='num')==top_head_level, # top level
						not mode['code-block-open'] # non code
					)):
						if len(string_lines)>0:
							if not mode['head-block-open']:
								self.create_node(
									string_lines, node_type='segment',
									attributes={'segment-class':'for-head'})
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

		if not len(string_lines) in (len(self.source_lines), 0):
			nt, at = (('head', {}) if mode['head-block-open'] else ('segment', {'segment-class':'for-head'}))
			self.create_node(string_lines, node_type=nt, attributes=at)
			self.source_lines = []
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
			for line in self.source_lines:
				string_type = self.string_type(line)
				# print(f'[285] string_type {string_type} block_mode {block_mode} line {line}')
				if (string_type in ('ul-li','ol-li')):
					if block_mode in manage_mode["ul-ol"]:
						# print('[288] set block_mode')
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode="ul-ol-list"
						string_lines.append(line)
					else:
						# print('[292] append string')
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
					elif block_mode in manage_mode["quote"]:
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
						# print('[335] empty passed')
					else:
						string_lines.append(line)
				else:
					if block_mode in manage_mode["other"]:
						self.create_node(string_lines, node_type=block_to_node[block_mode])
						block_mode=''
					else:
						string_lines.append(line)
			if not len(string_lines) in (len(self.source_lines), 0):
				# print(f'[345] {block_to_node[block_mode]}')
				self.create_node(string_lines, node_type=block_to_node[block_mode])

		if not len(string_lines) in (len(self.source_lines), 0):
			string_lines = self.create_node(string_lines, attributes={'segment-class':'for-blocks'})
		elif len(string_lines)>0:
			# self.source_lines = string_lines and >0
			# Each string is node!
			while len(self.source_lines)>0:
				line = self.source_lines.pop(0)
				self.create_node([line], node_type='string')

	def head_stn(self):
		# print(f'[511] source_lines', self.source_lines)
		if len(self.source_lines)>2:
			self.source_lines = self.source_lines[0:2]
		if len(self.source_lines)==2:
			self.attributes['anchor']=self.extract_anchor(self.source_lines.pop())
		# print(f'[516] source_lines', self.source_lines)
		if len(self.source_lines)==1:
			string_line = self.source_lines.pop()
			self.attributes['head-level']=self.get_head_level(string_line)
			string_line = self.get_head_text(string_line)
			self.create_node([string_line], node_type='string')
			if not 'anchor' in self.attributes:
				self.attributes['anchor']=self.translit_string(string_line)
		# print(f'[524] source_lines', self.source_lines)

	def list_stn(self):
		string_lines = []
		top_list_level = self.top_list_level(self.source_lines)
		mode = {'ul-block-open': False, 'ol-block-open': False, 'code-block-open':False}
		for line in self.source_lines:
			string_type = self.string_type(line)
			string_level = self.get_string_level(line)
			# print(f'[379] t: "{string_type}", l "{string_level}", line: {line}')
			if all((
					string_type in ('ul-li', 'ol-li'),
					string_level == top_list_level,
					not mode['code-block-open']
				)):
				# print('[385] all')
				if self.all_modes_same(mode):
					# print('[387] all all_modes_same')
					if string_type=='ul-li':
						mode['ul-block-open']=True
						self.attributes['list-type']='ul-list'
					if string_type=='ol-li':
						mode['ol-block-open']=True
						self.attributes['list-type']='ol-list'
				self.create_node(string_lines, node_type='segment', attributes={'name':'li'})
				string_lines.append(self.clear_li_string(line))
			elif string_type == 'code':
				string_lines.append(line)
				mode['code-block-open'] = not mode['code-block-open']
			else:
				string_lines.append(line)
		nt = ('list-node' if (mode['ul-block-open'] or mode['ol-block-open']) else 'segment')
		self.create_node(string_lines, node_type='segment', attributes={'name':'li'})

	def code_stn(self):
		# Code-block is prepared node for convertion.
		# Clear the strings from space.
		top_level = 999999
		string_lines = []
		while len(self.source_lines)>0:
			line = self.source_lines.pop(0).replace('\t', ' '*4)
			level = self.get_string_level(line)
			string_type = self.string_type(line)
			# print(f"[414] level {level} string_type {string_type}")
			top_level = (level if (level < top_level and string_type!='empty') else top_level)
			string_lines.append(line)
		# print(r'[417] ^\s{'+str(top_level)+r'}([\s\S]*)')
		regex = re.compile(r'^\s{'+str(top_level)+r'}([\s\S]*)')
		while len(string_lines)>0:
			line = string_lines.pop(0)
			string_type = self.string_type(line)
			if string_type!='empty':
				line = re.match(regex, line).group(1)
			else:
				line = '\n'
			self.source_lines.append(line)
		self.attributes['code-left-level']=top_level
		# print(self.source_lines)

	def string_stn(self):
		if len(self.source_lines)>0:
			line = self.source_lines.pop(0)
			source_line = line
			while len(line)>0:
				scope_type, scope, line = self.find_separate_scope(line)
				# print(f"[435] scope_type {scope_type}, scope {scope}, line {line}")
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
					# print(f"[454] scope_type {scope_type}, prev_line {prev_line}, scope {scope}, line {line}")
					if scope_type is None:
						# simple-string
						if line == source_line:
							if self.node_type!='string':
								self.node_type='tag'
								self.attributes={'name': 'simple-string'}
							self.source_lines.append(line)
						else:
							self.create_node(
								[line],
								node_type='tag',
								attributes={'name': 'simple-string'}
							)
						line=''
					elif scope_type=='hyperlink':
						self.create_simple_string(prev_line)
						text, href = self.extract_href(scope)
						self.create_node(
							[text],
							node_type='tag',
							attributes={'name': 'hyperlink', 'href': href}
						)
					elif scope_type in ('tt-quote', 'back-apostroph'):
						self.create_simple_string(prev_line)
						scope = self.extract_tt_quote(scope, scope_type)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'tt'}
						)
					elif scope_type=='bold-italic':
						self.create_simple_string(prev_line)
						scope = self.extract_bold_italic(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'bold-italic'}
						)
					elif scope_type=='bold':
						self.create_simple_string(prev_line)
						scope = self.extract_bold(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'bold'}
						)
					elif scope_type=='italic':
						self.create_simple_string(prev_line)
						scope = self.extract_italic(scope)
						self.create_node(
							[scope],
							node_type='tag',
							attributes={'name': 'italic'}
						)
					else:
						# simple-string
						# print(f"[504] line:{line}, source:{source_lines}")
						self.node_type='tag'
						self.attributes={'name': 'simple-string'}
						self.source_lines.append(line)
						line=''
		else:
			print(f"[490] String is not exists.")

	def test_convert(self):
		text = ""
		attributes = ""
		for key in self.attributes:
			attributes += f' {key}="{self.attributes[key]}"'
		if self.node_type == 'folder':
			arround_tags = (f'<folder{attributes}>\n', '</folder>\n')
		elif self.node_type == 'file':
			arround_tags = (f'<file{attributes}>\n', '</file>\n')
		elif self.node_type == 'segment':
			arround_tags = (f'<segment{attributes}>\n', '</segment>\n')
		elif self.node_type == 'quote':
			arround_tags = (f'<quote{attributes}>\n', '</quote>\n')
		elif self.node_type == 'head':
			arround_tags = (f'<header{attributes}>\n', '</header>\n')
		elif self.node_type == 'list-node':
			arround_tags = (f'<list{attributes}>\n', '</list>\n')
		elif self.node_type == 'code':
			arround_tags = (f'<code{attributes}>\n', '</code>\n')
		elif self.node_type == 'string':
			arround_tags = (f'<p{attributes}>\n', '</p>\n')
		elif self.node_type == 'tag':
			arround_tags = (f'<tag{attributes}>\n', '</tag>\n')
		else:
			arround_tags = (f'<unknown class="{self.node_type}"{attributes}>\n', '</unknown>\n')
		if len(self.includes_nodes)>0:
			for node in self.includes_nodes:
				# if self.node_type == 'head': print(f"[700] ", print(node.source_lines, node.includes_nodes))
				text+=node.test_convert()
		elif len(self.source_lines)>0:
			text += '<br/>'.join(self.source_lines)
		text = f"{arround_tags[0]}{text}{arround_tags[1]}"
		return text

	def get_file_name_from_number(self, file_number):
		file_name = self.data_base.files_db['files-paths'][file_number]
		file_name = self.clear_file_name(file_name)
		return file_name

	def clear_file_name(self, file_name):
		file_name = os.path.splitext(os.path.split(file_name)[1])[0]
		instr = re.match(r'\d+_(.*)', file_name)
		if instr is not None: file_name = instr.group(1)
		return file_name

	def get_turn_pages_html(self):
		file_number = self.data_base.get_file_number(self.attributes['path'])
		prev_ = file_number-1
		next_ = file_number+1
		crosslink = self.data_base.get_crosslink()
		if prev_>-1:
			prev_name = self.get_file_name_from_number(prev_)
			prev_link = f'<a href="{crosslink}{prev_name}.html" class="avs-pages-button__link">&lt; Назад, к странице {prev_+1}</a>'
			prev_btn = f'<div class="avs-pages-button__left-combine"><div class="avs-pages-button">{prev_link}</div></div>'
		else:
			prev_btn = '<div class="empty">&nbsp;</div>'
		if next_<len(self.data_base.files_db['files-paths']):
			next_name = self.get_file_name_from_number(next_)
			next_link = f'<a href="{crosslink}{next_name}.html" class="avs-pages-button__link">Вперёд, к странице {next_+1} &gt;</a>'
			next_btn = f'<div class="avs-pages-button__right-combine"><div class="avs-pages-button">{next_link}</div></div>'
		else:
			next_btn = '<div class="empty">&nbsp;</div>'
		text = '<div class="avs-pages-button__wrapper">'
		text += f'{prev_btn}{next_btn}'
		text += '</div>\n'
		return text

	def convert_to_html(self, parent=None, deep_level=0):
		text = ""
		if self.node_type == 'folder':
			self.data_base.refresh_deep_level()
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					node.convert_to_html(parent=self, deep_level=deep_level+1)

		elif self.node_type == 'file':
			central_text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					central_text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			if self.attributes['path']==self.data_base.get_content_file_path():
				self.data_base.add_content_html_text(central_text)
			turn_pages = self.get_turn_pages_html()
			header = ''.join(self.data_base.get_header())
			instr = re.match(r'<header-header></header-header>', header)
			if instr is not None:
				header = header.replace(instr.group(0), self.data_base.get_content_html_text())
			footer = ''.join(self.data_base.get_footer())
			instr = re.match(r'<header-header></header-header>', footer)
			if instr is not None:
				footer = footer.replace(instr.group(0), self.data_base.get_content_html_text())
			output_text = header + turn_pages + central_text + turn_pages + footer
			output_path = f"{self.data_base.get_output_path()}\\{self.clear_file_name(self.attributes['path'])}.html"
			with open(output_path, 'w', encoding='utf-8') as file:
				file.write(output_text)
				# print(f"'[776] File {output_path} was been exist from {self.attributes['path']}'")

		elif self.node_type == 'segment':
			text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			if parent.node_type=='list-node':
				text = f'<li>{text}</li>\n'

		elif self.node_type == 'quote':
			text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			text = f'<blockquote class="avs-article-blockquote">\n{text}</blockquote>\n'

		elif self.node_type == 'head':
			text=""
			anchor = (f' id="{self.attributes["anchor"]}"' if 'anchor' in self.attributes else '')
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			elif len(self.source_lines)>0:
				text += '<br/>'.join(self.source_lines)
			if parent.node_type=='folder':
				self.data_base.add_addition(f'<h2{anchor} class="avs-article-h2">{text}</h2>')
			else:
				last_key = list(self.data_base.deep_level_head.keys())[-1]
				last_head_level = int(re.match(r'h(\d+)', last_key).group(1))
				if self.data_base.deep_level_head[last_key]<deep_level or last_key=='h2':
					last_head_level+=1
					if last_head_level>6: last_head_level=6
					self.data_base.deep_level_head[f"h{last_head_level}"]=deep_level
					text = f'<h{last_head_level}{anchor} class="avs-article-h{last_head_level}">{text}</h{last_head_level}>'
				else:
					text = f'<{last_key}{anchor} class="avs-article-{last_key}">{text}</{last_key}>'

		elif self.node_type == 'list-node':
			text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			if self.attributes['list-type']=='ol-list':
				text = f'<ol>\n{text}</ol>\n'
			elif self.attributes['list-type']=='ul-list':
				text = f'<ul>\n{text}</ul>\n'

		elif self.node_type == 'code':
			code_type = (self.attributes['code-type'] if 'code-type' in self.attributes else None)
			text = ""
			source_lines = self.source_lines
			if code_type == 'qsp':
				text = self.stilization_qsp_code(''.join(source_lines))
			elif code_type == 'css':
				text = self.stilization_css_code(''.join(source_lines))
			elif code_type == 'html':
				text = self.stilization_html_code(''.join(source_lines))
			else:
				text = '<br/>'.join([self.replace_spaces(line) for line in source_lines])
			text = f'<div class="Monokai-Code">\n{text}</div>\n'

		elif self.node_type == 'string':
			text=""
			not_p=False
			if parent.node_type=='segment':
				name = (parent.attributes['name'] if 'name' in parent.attributes else '')
				not_p = (True if name=='li' else False)
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			elif len(self.source_lines)>0:
				text += '<br/>'.join(self.source_lines)
			if not parent.node_type in ('head') and not not_p:
				text = f'<p>\n{text}</p>\n'

		elif self.node_type == 'tag':
			text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			elif len(self.source_lines)>0:
				text += '<br/>'.join(self.source_lines)
			if self.attributes['name']=='tt':
				text = f'<code>{text}</code>'
			elif self.attributes['name']=='hyperlink':
				href = (self.attributes['href'] if 'href' in self.attributes else '#')
				if '#' in href:
					if href.index('#')==0:
						href = self.data_base.get_full_link_to_anchor(href[1:])
				text = f'<a href="{href}" style="text-decoration:none;" class="avs-page-external-link">{text}</a>'
			elif self.attributes['name']=='anchor':
				text = f'<a id="{self.attributes["anchor"]}" name="{self.attributes["anchor"]}"></a>'
			elif self.attributes['name']=='hr':
				text = '<hr class="em-hr" />'
			elif self.attributes['name']=='image':
				text = '<div class="avs-articles-image__wrapper">'
				text += f'<img src="{self.attributes["src"]}" alt="AleksVersus-GAM-RUS" class="avs-articles-image">'
				text += '</div>'
			elif self.attributes['name']=='bold-italic':
				text = f'<strong><em>{text}</em></strong>'
			elif self.attributes['name']=='bold':
				text = f'<strong>{text}</strong>'
			elif self.attributes['name']=='italic':
				text = f'<em>{text}</em>'
			elif self.attributes['name']=='simple-string':
				text = text

		else:
			text=""
			if len(self.includes_nodes)>0:
				for node in self.includes_nodes:
					text+=node.convert_to_html(parent=self, deep_level=deep_level+1)
			elif len(self.source_lines)>0:
				text += '<br/>'.join(self.source_lines)
		return text

	def transport_data_base(self, data_base):
		self.data_base = data_base
		if self.node_type == 'folder':
			pass
		elif self.node_type == 'file':
			self.data_base.append_file(self.attributes['path'])
		elif self.node_type == 'segment':
			pass
		elif self.node_type == 'quote':
			pass
		elif self.node_type == 'head':
			pass
		elif self.node_type == 'list-node':
			pass
		elif self.node_type == 'code':
			pass
		elif self.node_type == 'string':
			pass
		elif self.node_type == 'tag':
			pass
		else:
			pass
		if 'anchor' in self.attributes:
			self.data_base.add_anchor(self.attributes['anchor'])
		if len(self.includes_nodes)>0:
			for node in self.includes_nodes:
				node.transport_data_base(self.data_base)

	def convert_to_fb2(self, parent=None, deep_level=0):
		soup = BeautifulSoup(self.test_convert(), 'lxml')

		for t in soup.find_all('code'):
			for child in t.contents:
				if child.name==None:
					child.string = self.replace_spaces(str(child))
					child.wrap(soup.new_tag('code')).wrap(soup.new_tag('p'))
			for br in t.find_all('br'):
				br.unwrap()
			t.unwrap()

		for quote in soup.find_all('quote'):
			quote.name = 'cite'

		for list_olul in soup.find_all('list'):
			if list_olul['list-type']=='ol-list':
				count=0
				for segment in list_olul.find_all('segment', {'name':'li'}):
					segment.p.insert(0, f"{count+1}. ")
					segment.unwrap()
					count+=1
			if list_olul['list-type']=='ul-list':
				for segment in list_olul.find_all('segment', {'name':'li'}):
					segment.p.insert(0, f"* ")
					segment.unwrap()
			list_olul.unwrap()


		for t in soup.find_all('tag'):
			if t['name']=='hyperlink':
				t.name = 'a'
				t['l:href']=t['href']
				del t['name']
				del t['href']
			elif t['name']=='tt':
				t.name = 'code'
				del t['name']
			elif t['name']=='hr':
				t.string = '---'
				t.name = 'p'
				del t['name']
			elif t['name']=='simple-string':
				t.unwrap()
			elif t['name']=='bold':
				t.name = 'strong'
				del t['name']
			elif t['name']=='italic':
				t.name = 'emphasis'
				del t['name']
			elif t['name']=='bold-italic':
				t.name = 'emphasis'
				t.wrap(soup.new_tag('strong'))
				del t['name']
			elif t['name']=='image':
				t.name = 'p'
				t.string = 'Изображение: '
				new_tag = soup.new_tag('a')
				new_tag['l:href'] = t["src"]
				new_tag.string = t["src"]
				t.append(new_tag)
				del t['name']
				del t['src']

		for file in soup.find_all('file'):
			title = file.header
			file['id']=title['anchor']
			del file['path']
			main_segment = file.segment
			main_segment['type']='files-segment'
			self.fb2_retape_segment(main_segment)
			main_segment.unwrap()
			title.name = 'title'
			del title['anchor']
			file.name = 'section'

		for folder in soup.find_all('folder'):
			if folder.header is not None:
				folder['id'] = folder.header['anchor']
				folder.header.name = 'title'
			del folder['path']
			folder.name = 'section'

		text = str(soup)

		output_text = ""
		while len(text)>0:
			match_in = re.search(r'(<code>)([\s\S]*?)(</code>)', text)
			if match_in is not None:
				scope = match_in.group(0)
				q = text.index(scope)
				prev_line = text[0:q]
				post_line = text[q+len(scope):]
				output_text += prev_line
				output_text += f'<code>{match_in.group(2).strip()}</code>'
				text = post_line
			else:
				output_text += text
				text = ''
		text = output_text

		output_text = ""
		while len(text)>0:
			match_in = re.search(r'(</p>)([\s\n\t]*)(<p>)', text)
			if match_in is not None:
				scope = match_in.group(0)
				q = text.index(scope)
				prev_line = text[0:q]
				post_line = text[q+len(scope):]
				output_text += prev_line
				output_text += f'</p>\n<p>'
				text = post_line
			else:
				output_text += text
				text = ''
		text = output_text

		output_text = ""
		while len(text)>0:
			match_in = re.search(r'(<p>)([\s\S]*?)(</p>)', text)
			if match_in is not None:
				scope = match_in.group(0)
				q = text.index(scope)
				prev_line = text[0:q]
				post_line = text[q+len(scope):]
				output_text += prev_line
				output_text += f'<p>{match_in.group(2).strip()}</p>'
				text = post_line
			else:
				output_text += text
				text = ''
		text = output_text

		output_text = ""
		while len(text)>0:
			match_in = re.search(r'(>)([\s\n\t]*[\.\;\,\:\)\(]+)', text)
			if match_in is not None:
				scope = match_in.group(0)
				q = text.index(scope)
				prev_line = text[0:q]
				post_line = text[q+len(scope):]
				output_text += prev_line
				output_text += f'>{match_in.group(2).strip()}'
				text = post_line
			else:
				output_text += text
				text = ''
		text = output_text

		output_text = ""
		while len(text)>0:
			match_in = re.search(r'<(\w+) .*?>([\s\n\t]*?)</\1>', text)
			if match_in is not None:
				scope = match_in.group(0)
				q = text.index(scope)
				prev_line = text[0:q]
				post_line = text[q+len(scope):]
				output_text += prev_line
				output_text += f''
				text = post_line
			else:
				output_text += text
				text = ''
		text = output_text
		text = text.replace('<html>','').replace('</html>','')
		text = text.replace('<body>','').replace('</body>','')
		return text

	def fb2_retape_segment(self, main_segment):
		for segment in main_segment.find_all('segment', {'segment-class': 'for-head'}):
			t = segment.find_previous_sibling()
			if t is not None and t.name=='header':
				t.name='title'
				segment['id']=t['anchor']
				del t['anchor']
				del t['head-level']
				segment.insert(0, t)
				self.fb2_retape_segment(segment)
			segment.name = 'section'
			for s in segment.find_all('segment'):
				s.unwrap()
			del segment['segment-class']

	# ------------------------------- static methods ---------------------------

	@staticmethod
	def comments_replace(string_lines:list, mode=''):
		input_text = '\r'.join(string_lines)
		output_text = ""
		while len(input_text)>0:
			scope_type, prev_text, scope_regexp_obj, post_text = NewNode.find_overlap_main(input_text, mode=mode)
			if scope_type=='comment':
				output_text += prev_text
				input_text = post_text
			elif scope_type in ("string", "code"):
				output_text += prev_text + scope_regexp_obj.group(0)
				input_text = post_text
			else:
				output_text += input_text
				input_text = ''
		return output_text.split('\r')

	@staticmethod
	def find_overlap_main(string_line:str, mode=''):
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'comment',
				'string',
				'code'
			],
			"scope-regexp":
			[
				re.search(r'\/\*[\s\S]*?\*\/', string_line, flags=re.MULTILINE),
				re.search(r'((?<!")"(?!")|(?<!\')\'(?!\'))[\s\S]*?\1', string_line, flags=re.MULTILINE),
				re.search(r'(```\w*)[\S\s]*?(```)', string_line, flags=re.MULTILINE)
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def stilization_qsp_code(code_text:str):
		# convert code_text to css
		output_text = ""
		while len(code_text)>0:
			scope_type, prev_text, scope_regexp_obj, post_text = NewNode.find_overlap_qsp_scope(code_text)
			if scope_type=='comment':
				output_text += prev_text
				andamp = scope_regexp_obj.group(1)
				excmark = scope_regexp_obj.group(2)
				comment = scope_regexp_obj.group(3)
				output_text += f'<span class="Monokai-Operator">{andamp}</span>'
				output_text += f'<span class="Monokai-Comment">{excmark}{comment}</span>'
				code_text = post_text
			elif scope_type=='string':
				output_text += prev_text
				quot_opn = scope_regexp_obj.group(1)
				quot_cls = scope_regexp_obj.group(3)
				text = scope_regexp_obj.group(2)
				output_text += f'<span class="Monokai-String">{quot_opn}{text}{quot_cls}</span>'
				code_text = post_text
			elif scope_type=='markup':
				output_text += prev_text
				output_text += f'<span class="Monokai-Markup">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='location-start':
				output_text += prev_text
				output_text += f'<span class="Monokai-StartLoc">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='location-end':
				output_text += prev_text
				output_text += f'<span class="Monokai-EndLoc">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='operacion':
				output_text += prev_text
				output_text += f'<span class="Monokai-Operator">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='operator':
				output_text += prev_text
				output_text += f'<span class="Monokai-Operator">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='koperator':
				output_text += prev_text
				output_text += f'<span class="Monokai-Koperator">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='function':
				output_text += prev_text
				output_text += f'<span class="Monokai-Func">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='varname':
				output_text += prev_text
				output_text += f'<span class="Monokai-SysVar">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='hidefunc':
				output_text += prev_text
				output_text += f'<span class="Monokai-UnFunc">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='number':
				output_text += prev_text
				output_text += f'<span class="Monokai-Numeric">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type in ('var', 'spaces'):
				output_text += prev_text
				output_text += f'{scope_regexp_obj.group(0)}'
				code_text = post_text
			else:
				output_text += code_text
				code_text = ''
		return NewNode.replace_spaces(output_text).replace('\n','<br/>\n')

	@staticmethod
	def find_overlap_qsp_scope(string_line:str):
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'comment',
				'string',
				'markup',
				'location-start',
				'operacion',
				'operator',
				'koperator',
				'function',
				'varname',
				'hidefunc',
				'number',
				'location-end',
				'var'
			],
			"scope-regexp":
			[
				NewNode.search_comment(string_line),
				re.search(r'("|\')([\s\S]*?)(\1)', string_line, flags=re.MULTILINE),
				re.search(r'(^\s*)(:[^\s\'\"\{\}\&][^\s\'\"\{\}\&]*?)(?=\s*($|\&amp;))', string_line, flags=re.MULTILINE),
				re.search(r'^\s*#.*?$', string_line, flags=re.MULTILINE),
				re.search(
					r'\-\=|\+\=|\*\=|\/\=|&lt;\=|&gt;\=|\-|\=|\+|\*|\/|\[|\]|\{|\}|\(|\)|\:|\&amp;|,|&lt;|&gt;',
					string_line, flags=re.MULTILINE),
				re.search(r'(?i:(\bexec|\bset|\blet|\blocal|\bview|\binclib|\bfreelib|\baddqst|\bopenqst|\bopengame|\bsavegame|\bkillqst|\bcmdclr|\bcmdclear|\ball|\bclose|\bexit|\bplay|\bsettimer|\bmenu|\bunsel|\bunselect|\bjump|\bcopyarr|\bdelact|\bwait|\bkillall|\bdynamic|\bkillvar|\bdelobj|\baddobj|\bkillobj|\bcls|\bcla|\bgs|\bxgt|\bgt|\bgoto|\bgosub|\bxgoto|\brefint|\bshowobjs|\bshowstat|\bshowacts|\bshowinput|\bmsg|(?<!\w)\*?(pl?|nl|clr|clear)))\b', string_line, flags=re.MULTILINE),
				re.search(r'\b(?i:(act|if|elseif|else|loop|while|step|end))\b', string_line, flags=re.MULTILINE),
				re.search(r'(?i:(\bobj|\bisplay|\blen|\brgb|\bmsecscount|\bno|\band|\bmod|\bcountobj|\binstr|\bisnum|\bval|\bloc|\bor|\bra?nd|\barrsize|\barrpos|\barrcomp|\bstrcomp|\bstrpos|(?<!\w)\$?(input|user_text|usrtxt|desc|maintxt|stattxt|qspver|curloc|selobj|selact|curacts|mid|(u|l)case|trim|replace|getobj|str|strfind|iif|dyneval|func|max|min|arritem)))\b', string_line, flags=re.MULTILINE),
				re.search(r'(?i:(\bnosave|\bdisablescroll|\bdisablesubex|\bdebug|\busehtml|\b(b|f|l)color|\bfsize|(?<!\w)\$?(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)))\b', string_line, flags=re.MULTILINE),
				re.search(r'@[\w\.]+\b', string_line, flags=re.MULTILINE),
				re.search(r'\b\d+\b', string_line, flags=re.MULTILINE),
				re.search(r'(^\s*)(\-)(.*?$)', string_line, flags=re.MULTILINE),
				re.search(r'\b[A-Za-zА-Яа-я_0-9][\w\.]*?\b', string_line, flags=re.MULTILINE)
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def search_comment(string_line:str):
		temp_line = string_line
		comment = ""
		mode = {"comment-open": False}
		while len(temp_line)>0:
			comment_start = re.search(r'(^\s*|\&amp;\s*)(!)', temp_line, flags=re.MULTILINE)
			if comment_start is not None and not mode["comment-open"]:
				scope = comment_start.group(0)
				comment += scope
				q = temp_line.index(scope)
				temp_line = temp_line[q+len(scope):]
				mode["comment-open"]=True
			elif mode["comment-open"]:
				scope_type, prev_line, scope_regexp_obj, post_line = NewNode.find_overlap_comments_scope(temp_line)
				if scope_type in ('single-string', 'single-quotes', 'single-apostrophes', 'single-scobe'):
					scope = scope_regexp_obj.group(0)
					comment += prev_line + scope
					mode["comment-open"]=False
					break # comment is enough
				elif scope_type in ('quotes', 'apostrophes', 'scobe'):
					comment += scope_regexp_obj.group(0)
					temp_line = post_line
				else:
					#error
					print('[240] Error')
					return None
			else:
				# comment is not found
				return None
		if comment != "":
			return re.search(r'(^\s*|\&amp;\s*)(!)([\s\S]*)', comment, flags=re.MULTILINE)

	@staticmethod
	def find_overlap_comments_scope(string_line:str):
		# Get string. Return scope_type, prev_line, scope_regexp_obj, post_line
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'single-quotes',
				'single-apostrophes',
				'single-scobe',
				'single-string',
				'quotes',
				'apostrophes',
				'scobe'
			],
			"scope-regexp":
			[
				re.search(r'^[^"\n]*?"[^"]*?"[^\'"\{\n]*?$', string_line, flags=re.MULTILINE),
				re.search(r'^[^\'\n]*?\'[^\']*?\'[^\'"\{\n]*?$', string_line, flags=re.MULTILINE),
				re.search(r'^[^\{\n]*?\{[^\}]*?\}[^\'"\{\n]*?$', string_line, flags=re.MULTILINE),
				re.search(r'(^[^"\'\{]*?$)', string_line, flags=re.MULTILINE),
				re.search(r'^[^"\n]*?"[^"]*?"[^"\n]*?', string_line, flags=re.MULTILINE),
				re.search(r'^[^\'\n]*?\'[^\']*?\'[^\'\n]*?', string_line, flags=re.MULTILINE),
				re.search(r'^[^\{]*?\{[^\}]*?\}[^\{\n]*?', string_line, flags=re.MULTILINE),
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def stilization_html_code(code_text:str):
		# convert code_text to html
		output_text = ""
		while len(code_text)>0:
			scope_type, prev_text, scope_regexp_obj, post_text = NewNode.find_overlap_html_scope(code_text)
			if scope_type=='tag':
				output_text += prev_text
				open_bracket = scope_regexp_obj.group(1)
				close_bracket = scope_regexp_obj.group(4)
				tag_name = scope_regexp_obj.group(2)
				attributes_string = NewNode.stilization_html_attributes(scope_regexp_obj.group(3))
				output_text += f'{open_bracket}<span class="Monokai-TagName">{tag_name}</span>'
				output_text += f'{attributes_string}{close_bracket}'
				code_text = post_text
			elif scope_type=='comment-block':
				output_text += prev_text
				output_text += f'<span class="Monokai-Comment">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			else:
				output_text += code_text
				code_text = ''
		return NewNode.replace_spaces(output_text).replace('\n','<br/>\n')

	@staticmethod
	def find_overlap_html_scope(string_line:str):
		# Get string. Return scope_type, scope, other_string
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'comment-block',
				'tag'
			],
			"scope-regexp":
			[
				re.search(r'\&lt;!--[\s\S]*?--\&gt;', string_line),
				re.search(r'(\&lt;\/?)(\s*[A-Za-zА-Яа-я]\w*)(\s+[\s\S]+?(?=\/?\&gt;))?(\/?\&gt;)', string_line),
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def stilization_html_attributes(string_line:str):
		output_text=""
		string_line = (string_line if type(string_line)==str else '')
		while len(string_line)>0:
			match_in_string = re.search(r'(\w+)(\s*=\s*)("|\')(.*?)(\3)', string_line)
			match_in_number = re.search(r'(\w+)(\s*=\s*)([^"\'\s]*)', string_line)
			if match_in_string is not None:
				instr = string_line.index(match_in_string.group(0))
				prev_text = string_line[:instr]
				post_text = string_line[instr+len(match_in_string.group(0)):]
				output_text+=prev_text
				output_text+= f'<span class="Monokai-Markup">{match_in_string.group(1)}</span>='
				output_text+=f'<span class="Monokai-String">"{match_in_string.group(4)}"</span>'
				string_line = post_text
			elif match_in_number is not None:
				instr = string_line.index(match_in_number.group(0))
				prev_text = string_line[:instr]
				post_text = string_line[instr+len(match_in_number.group(0)):]
				output_text+=prev_text
				output_text+= f'<span class="Monokai-Markup">{match_in_number.group(1)}</span>='
				output_text+=f'<span class="Monokai-Numeric">{match_in_number.group(3)}</span>'
				string_line = post_text
			else:
				output_text += string_line
				string_line=''
		return output_text

	@staticmethod
	def stilization_css_code(code_text:str):
		# convert code_text to css
		output_text = ""
		count=0
		while len(code_text)>0 and count<999:
			scope_type, prev_text, scope_regexp_obj, post_text = NewNode.find_overlap_css_scope(code_text)
			if scope_type=='selectors':
				output_text += prev_text
				selectors_string = NewNode.stilization_css_selectors(scope_regexp_obj.group(0))
				output_text += f'{selectors_string}'
				code_text = post_text
			elif scope_type=='comment-block':
				output_text += prev_text
				output_text += f'<span class="Monokai-Comment">{scope_regexp_obj.group(0)}</span>'
				code_text = post_text
			elif scope_type=='property-line':
				output_text += prev_text
				property_name = scope_regexp_obj.group(1)
				property_value = scope_regexp_obj.group(4)
				property_end = scope_regexp_obj.group(6)
				output_text += f'<span class="Monokai-Construct">{property_name}</span>: '
				output_text += f'<span class="Monokai-String">"{property_value}"</span>'
				output_text += property_end
				code_text = post_text
			elif scope_type=='property-number':
				output_text += prev_text
				property_name = scope_regexp_obj.group(1)
				property_value = scope_regexp_obj.group(3)
				property_end = scope_regexp_obj.group(4)
				output_text += f'<span class="Monokai-Construct">{property_name}</span>: '
				output_text += f'<span class="Monokai-Numeric">{property_value}</span>'
				output_text += property_end
				code_text = post_text
			elif scope_type=='property-url':
				output_text += prev_text
				property_name = scope_regexp_obj.group(1)
				property_value = scope_regexp_obj.group(4)
				property_end = scope_regexp_obj.group(7)
				output_text += f'<span class="Monokai-Construct">{property_name}</span>: '
				output_text += f'<span class="Monokai-Command">url(<span class="Monokai-String">{property_value}</span>)</span>'
				output_text += property_end
				code_text = post_text
			else:
				output_text += code_text
				code_text = ''
			count+=1
		return NewNode.replace_spaces(output_text).replace('\n','<br/>\n')

	@staticmethod
	def find_overlap_css_scope(string_line:str):
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'comment-block',
				'selectors',
				"property-line",
				"property-number",
				"property-url"
			],
			"scope-regexp":
			[
				re.search(r'\/\*[\s\S]*?\*\/', string_line),
				re.search(r'(\s*)([^\{\}\/]+)(?=\{)', string_line),
				re.search(r'([\w\-]+)(\s*:\s*)("|\')([\s\S]*?)(\3)(\s*;|\s*\})', string_line, flags=re.MULTILINE),
				re.search(r'([\w\-]+)(\s*:\s*)([\S\s]*?)(;|\})', string_line, flags=re.MULTILINE),
				re.search(r'([\w\-]+)(\s*:\s*)(url)(\()([\s\S]*?)(\))(\s*;|\s*\})', string_line, flags=re.MULTILINE),
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

	@staticmethod
	def stilization_css_selectors(string_line:str):
		output_text = ""
		count=0
		while len(string_line)>0 and count<999:
			scope_type, prev_text, scope_regexp_obj, post_text = NewNode.find_overlap_css_selectors_scope(string_line)
			if scope_type in ('tag', 'rule', 'pointer'):
				output_text += prev_text
				output_text += f'<span class="Monokai-TagName">{scope_regexp_obj.group(0)}</span>'
				string_line = post_text
			elif scope_type in ('id', 'class'):
				output_text += prev_text
				output_text += f'<span class="Monokai-Markup">{scope_regexp_obj.group(0)}</span>'
				string_line = post_text
			elif scope_type in ('pseudo-class', '90zxfr'):
				output_text += prev_text
				output_text += f'{scope_regexp_obj.group(0)}'
				string_line = post_text
			else:
				output_text += string_line
				string_line = ''
			count+=1
		return output_text

	@staticmethod
	def find_overlap_css_selectors_scope(string_line:str):
		# Get string. Return scope_type, prev_line, scope_regexp_obj, post_line
		maximal = len(string_line)+1
		mini_data_base = {
			"scope-name": [
				'tag',
				'rule',
				'id',
				"class",
				"pseudo-class",
				"pointer"
			],
			"scope-regexp":
			[
				re.search(r'(?<!(\.|#))(\b\w+\b)', string_line),
				re.search(r'(@\w+\b)', string_line),
				re.search(r'(#[\w\-]+)', string_line),
				re.search(r'(\.[\w\-]+)', string_line),
				re.search(r'(\:[\w\-]+)', string_line),
				re.search(r'(\&gt;|\+)', string_line)
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
			scope_regexp_obj = mini_data_base['scope-regexp'][i]
			scope = scope_regexp_obj.group(0)
			q = string_line.index(scope)
			prev_line = string_line[0:q]
			post_line = string_line[q+len(scope):]
			return scope_type, prev_line, scope_regexp_obj, post_line
		else:
			return None, '', '', string_line

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
				# 'back-apostroph',
				'bold-italic',
				'bold',
				'italic',
				'hyperlink'
			],
			"scope-regexp":
			[
				re.search(r'(\'\')((?<!\s).*?(?!\s))(\1)', string_line),
				# re.search(r'(`)(.*?)(\1)', string_line),
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
		elif re.match(r'^\s*?&gt;&gt;&gt;\s*?$', string_line)!=None:
			return 'quote'
		elif re.match(r'^\s*?&gt;\s+', string_line)!=None:
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
			if NewNode.string_type(line)=='head' and not mode['code-block-open']:
				level = NewNode.get_head_level(line, result_type='num')
				top_level = (level if level < top_level else top_level)
			elif NewNode.string_type(line)=='code':
				mode['code-block-open'] = not mode['code-block-open'] 
		return top_level

	@staticmethod
	def clear_quote_string(string_line:str):
		return re.match(r'^(\s*&gt;\s*)(.+?)$', string_line).group(2)

	@staticmethod
	def get_string_level(string_line:str):
		leveling=re.match(r'^(\s+)\S', string_line)
		return (0 if (leveling is None) else len(leveling.group(1)))

	@staticmethod
	def top_list_level(string_lines:list):
		top_level=999999
		for line in string_lines:
			if NewNode.string_type(line) in ('ol-li', 'ul-li'):
				level = NewNode.get_string_level(line)
				top_level = (level if level<top_level else top_level)
		return top_level

	@staticmethod
	def clear_li_string(string_line:str):
		return re.match(r'^(\s*(\*|\d+\.)\s+)(.+?)$', string_line).group(3)

	@staticmethod
	def get_code_type(string_line:str):
		match_in = re.match(r'^\s*```(\w+)\s*$', string_line)
		return (match_in.group(1) if match_in is not None else None)

	@staticmethod
	def replace_specsymbols(string_line:str):
		# replace ampersand in string
		while True:
			if re.search(r'\&(?!\S+?;)',string_line)!=None:
				string_line = re.sub(r'\&(?!\S+?;)','&amp;', string_line)
			else:
				break
		string_line = string_line.replace('<','&lt;')
		string_line = string_line.replace('>','&gt;')
		return string_line

	@staticmethod
	def replace_spaces(html_text:str):
		# replace spaces on &nbsp; without tags
		output_text = ""
		while len(html_text)>0:
			tag = re.search(r'<.*?>', html_text)
			if tag is not None:
				q = html_text.index(tag.group(0))
				prev_text = html_text[:q]
				post_text = html_text[q+len(tag.group(0)):]
				output_text += prev_text.replace(' ', '&nbsp;')+tag.group(0)
				html_text = post_text
			else:
				output_text += html_text.replace(' ', '&nbsp;')
				html_text = ''
		return output_text

def main():
	# названия файлов, из которых берём сборку
	html_json=[
		# "..\\..\\[source]\\example\\html.json",
		"..\\..\\[source]\\готовые статьи\\build-project.json",
		# "..\\..\\[source]\\ответы\\html.json",
		# "..\\..\\[source]\\вики-qsp\\html.json"
	]
	for path in html_json:
		TextToHTML(path).convert_to()

if __name__=="__main__":
	main()


