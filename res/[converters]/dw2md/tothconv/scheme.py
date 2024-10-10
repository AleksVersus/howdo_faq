import os
import json
import pypandoc
import re
from .foo import (wf, safe_mk_fold)

class SchemeDw2md:
	"""Scheme"""
	def __init__(self, scheme_path:str='scheme.json') -> None:
		scheme_path = os.path.abspath(scheme_path)
		os.chdir(os.path.split(scheme_path)[0])
		with open(scheme_path, 'r', encoding='utf-8') as fp:
			self.scheme_json = json.load(fp)
		self.mb = {}
		self.mb['wiki_source'] = []
		self.mb['output_path'] = []
		self.mb['sidebar_position'] = []
		self.mb['wikipath'] = []
		self.mb['type'] = []
		for el in self.scheme_json:
			self.mb['wiki_source'].append(el)
			self.mb['output_path'].append(self.scheme_json[el]['path'])
			self.mb['sidebar_position'].append(self.scheme_json[el]['sidebar_position'])
			self.mb['wikipath'].append(self.scheme_json[el]['wikipath'])
			if 'type' in self.scheme_json[el]:
				self.mb['type'].append(self.scheme_json[el]['type'])
			else:
				self.mb['type'].append('page')
		self.folder_output_md = None

	def get_prop(self, el:str, prop:str) -> str:
		# path; sidebar_position; wikipath;
		return self.scheme_json[el][prop]

	def get_el_by_prop(self, prop:str, value:str) -> dict:
		if not value in self.mb[prop]:
			return None
		i = self.mb[prop].index(value)
		output_dict = {
			'wiki_source': self.mb['wiki_source'][i],
			'output_path': self.mb['output_path'][i],
			'sidebar_position': self.mb['sidebar_position'][i],
			'wikipath': self.mb['wikipath'][i],
			'type': self.mb['type'][i]
		}
		return output_dict

	def get_el(self, i:int) -> dict:
		return {
			'wiki_source': self.mb['wiki_source'][i],
			'output_path': self.mb['output_path'][i],
			'sidebar_position': self.mb['sidebar_position'][i],
			'wikipath': self.mb['wikipath'][i],
			'type': self.mb['type'][i]
		}
		
	def scheme(self) -> dict:
		return self.scheme_json

	def convert_to_md(self) -> None:
		for i, _ in enumerate(self.mb['wiki_source']):
			el = self.get_el(i)
			if el['type'] == 'page':
				self.pypan_file_to_md(el)

	def pypan_file_to_md(self, el:dict) -> None:
		# prepare path
		path = el['wiki_source']
		fullpath = os.path.abspath(path)
		# load dokuwiki text
		with open(fullpath, 'r', encoding='utf-8') as fp:
			input_text = fp.read()
		# prepare text
		input_text = self.dw_prefiltration(input_text, el)
		output_text = pypandoc.convert_text(
			input_text,
			to='markdown',
			format='dokuwiki',
			# filters = ['f_code_instr.py'],
			extra_args=['--wrap=none'])
		output_text = self.md_postfiltration(output_text, el)
		sidebar_position = el['sidebar_position']
		if sidebar_position is not None:
			output_text = f'---\nsidebar_position: {sidebar_position}\n---\n{output_text}'
		output_path = os.path.abspath(el['output_path'])
		wf(output_text, output_path)

	def dw_prefiltration(self, text:str, el:dict) -> str:
		""" Выполняется до прогона через pandoc """
		text = text.replace('<sxh qsp>', '<code qsp>')
		text = text.replace('<sxh>', '<code plain>')
		text = text.replace('</sxh>', '</code>')
		# text = text.replace('\t*', '  *')
		# text = text.replace('*  ', '* ')
		text = text.replace('\t', '  ')
		# wf(text, 'pf.dokuwiki')
		return text

	def md_postfiltration(self, text:str, el:dict) -> str:
		""" Выполняется после прогона через pandoc """
		curpath = os.path.split(os.path.abspath(el['output_path']))[0]
		# исправляем ссылки
		link_patterns = re.findall(r'\[([^]]+?)\]\((.*?)\)', text)
		for link in link_patterns:
			if link[1][0] == '/':
				wikipath = link[1][1:].replace('/', ':')
				if '?&#' in wikipath:
					i = wikipath.find('?&#')
					hashtag = '#' + wikipath[i+3:]
					wikipath = wikipath[0:i]
				else:
					hashtag = ''
				link_el = self.get_el_by_prop('wikipath', wikipath)
				if link_el['type'] == 'empty': print(f'Warning! Link to not exists page!!! {link} {wikipath}')
				try:
					linkpath = os.path.abspath(link_el['output_path'])
				except TypeError as e:
					print(link, wikipath, hashtag, link_el)
					raise e				
				relpath = os.path.relpath(linkpath, curpath).replace('\\','/')
				p, e = os.path.splitext(relpath)
				relpath = (p if e == '.md' else relpath)
				text = text.replace(f'[{link[0]}]({link[1]})', f'[{link[0]}]({relpath}{hashtag})')
		text = re.sub(r'\[(.*?)\]\{\.underline\}', r'<u>\1</u>', text, flags=re.MULTILINE)
		text = text.replace('-   ', '* ')
		text = text.replace(r'\\\n', r'\n')
		text = text.replace('\r\n', '\n')
		text = text.replace(r'\"', '"')
		text = text.replace('---', '—')
		text = re.sub(r'`([^`]+?)`\{\.(\w+)\}', r'\n    ``` \2\n\1\n```\n', text)
		# TODO: convertation in list item codesblock
		return text

	def convert_to_dw(self, output_folder:str='.') -> None:
		self.folder_output_md = os.path.abspath(output_folder)
		for i, _ in enumerate(self.mb['wiki_source']):
			el = self.get_el(i)
			if el['type'] == 'page':
				self.pypan_file_to_dw(el)

	def pypan_file_to_dw(self, el:dict) -> None:
		# prepare path
		path = el['output_path']
		fullpath = os.path.abspath(path)
		# load dokuwiki text
		with open(fullpath, 'r', encoding='utf-8') as fp:
			input_text = fp.read()
		# prepare text
		input_text = self.md_prefiltration(input_text, el)
		output_text = pypandoc.convert_text(
			input_text,
			to='dokuwiki',
			format='markdown',
			# filters = ['f_code_instr.py'],
			extra_args=['--wrap=none'])
		output_text = self.dw_postfiltration(output_text, el)
		output_path = os.path.join(self.folder_output_md, el['wiki_source'])
		output_folder = os.path.split(output_path)[0]
		safe_mk_fold(output_folder)
		wf(output_text, output_path)

	def md_prefiltration(self, text:str, el:dict) -> str:
		""" Выполняется до прогона через pandoc """
		# в какой папке лежит текущий файл
		curpath = os.path.split(el['output_path'])[0]
		# исправляем ссылки
		link_patterns = re.findall(r'\[([^]]+?)\]\((.*?)\)', text)
		for link in link_patterns:
			if link[1][0:4] != 'http':
				# ссылка не ссылается на внешний ресурс, значит ссылается на внутренний
				# пытаемся получить, что это за ссылка относительно текущей папки
				# здесь будет лежать относительный путь 
				curlink = os.path.normpath(os.path.join(curpath, link[1]))
				if os.path.splitext(curlink)[1] == '':
					curlink += '.md'
				link_el = self.get_el_by_prop('output_path', curlink)
				try:
					wikipath = link_el['wikipath']
				except TypeError as e:
					print(link, wikipath, link_el)
					raise e				
				text = text.replace(f'[{link[0]}]({link[1]})', f'[{link[0]}]({wikipath})')
		return text

	def dw_postfiltration(self, text:str, el:dict) -> str:
		""" Выполняется после прогона через pandoc """
		text = text.replace('<code qsp>', '<sxh qsp>')
		text = text.replace('<code html>', '<sxh html>')
		text = text.replace('<code plain>', '<sxh>')
		text = text.replace('<code>', '<sxh>')
		text = text.replace('</code>', '</sxh>')
		text = text.replace(r'\\\n', r'\n')
		text = text.replace('\r\n', '\n')
		return text

if __name__ == '__main__':
	...