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
			self.header_strings = header.readlines()
		with open(os.path.abspath(self.root_dict["foot"]), 'r', encoding='utf-8') as footer:
			self.footer_strings = footer.readlines()
		self.data_base = None
		self.root_folder = None

	def make_output_folder(self):
		if not os.path.exists(self.output_path):
			os.makedirs(self.output_path)

	def create_data_base(self):
		self.data_base = NewDataBase()
		self.data_base.addHeader(self.header_strings) # верхняя часть html-документа
		self.data_base.addFooter(self.footer_strings) # нижняя часть html-документа
		self.data_base.addExportPath(self.output_path) # выходная папка
		self.data_base.setContentFile(self.content_file_path) # содержание
		self.data_base.addCrossLink(self.project_dict["cross-link"]) # вид перекрёстных ссылок

	def convert_to_html(self):
		self.make_output_folder()
		self.create_data_base()
		self.root_folder = NewFolder(self.source_folder, self.data_base)
		self.root_folder.convert_to_html(self.data_base)