import pypandoc
import os
import re
import sys
import json

class SchemeDw2md:
	"""Scheme"""
	def __init__(self, scheme_path:str='scheme.json') -> None:
		with open(scheme_path, 'r', encoding='utf-8') as fp:
			self.scheme_json = json.load(fp)
		self.mb = {}
		self.mb['wiki_source'] = []
		self.mb['output_path'] = []
		self.mb['sidebar_position'] = []
		self.mb['wikipath'] = []
		for el in self.scheme_json:
			self.mb['wiki_source'].append(el)
			self.mb['output_path'].append(self.scheme_json[el]['path'])
			self.mb['sidebar_position'].append(self.scheme_json[el]['sidebar_position'])
			self.mb['wikipath'].append(self.scheme_json[el]['wikipath'])

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
			'wikipath': self.mb['wikipath'][i]
		}
		return output_dict

	def get_el(self, i:int) -> dict:
		return {
			'wiki_source': self.mb['wiki_source'][i],
			'output_path': self.mb['output_path'][i],
			'sidebar_position': self.mb['sidebar_position'][i],
			'wikipath': self.mb['wikipath'][i]
		}
		
	def scheme(self) -> dict:
		return self.scheme_json

	def convert_to_md(self) -> None:
		for i, _ in enumerate(self.mb['wiki_source']):
			el = self.get_el(i)
			SchemeDw2md.pypan_file(el)

	@staticmetchod
	def pypan_file(el:dict) -> None:
		# prepare path
		path = el['wiki_source']
		fullpath = os.path.abspath(path)
		# load dokuwiki text
		with open(fullpath, 'r', encoding='utf-8') as fp:
			input_text = fp.read()
		# prepare text
		input_text = SchemeDw2md.prefiltration(input_text, el)
		output_text = pypandoc.convert_text(
			input_text,
			to='markdown',
			format='dokuwiki',
			# filters = ['f_code_instr.py'],
			extra_args=['--wrap=none'])
		output_text = SchemeDw2md.postfiltration(output_text, el)
		sidebar_position = el['sidebar_position']
		if sidebar_position is not None:
			output_text = f'---\nsidebar_position: {sidebar_position}\n---\n{output_text}'
		output_path = os.path.abspath(el['output_path'])
		wf(output_text, output_path)

	@staticmetchod
	def prefiltration(text:str, el:dict) -> str:
		""" Выполняется до прогона через pandoc """
		text = text.replace('<sxh qsp>', '<code qsp>')
		text = text.replace('<sxh>', '<code plain>')
		text = text.replace('</sxh>', '</code>')
		# text = text.replace('\t*', '  *')
		# text = text.replace('*  ', '* ')
		text = text.replace('\t', '  ')
		# wf(text, 'pf.dokuwiki')
		return text

	@staticmetchod
	def postfiltration(text:str, el:dict) -> str:
		""" Выполняется после прогона через pandoc """
		path = el['wiki_source']
		relpath = os.path.relpath(el['output_path'], '..\\..\\docs\\wiki')
		fold = os.path.split(relpath)[0]
		# print(relpath, fold)
		text = re.sub(r'\[(.*?)\]\{\.underline\}', r'<u>\1</u>', text, flags=re.MULTILINE)
		text = text.replace('-   ', '* ')
		text = text.replace(r'\\\n', r'\n')
		text = text.replace('\r\n', '\n')
		text = text.replace(r'\"', '"')
		text = text.replace('---', '—')
		text = re.sub(r'`([^`]+?)`\{\.(\w+)\}', r'\n    ``` \2\n\1\n```\n', text)
		# TODO: convertation in list item codesblock
	
		return text	



def wf(text:str, path:str) -> None:
	fullpath = os.path.abspath(path)
	with open(fullpath, 'w', encoding='utf-8') as fp:
		fp.write(text)

# def poop(path:str) -> None:
# 	path = os.path.abspath(path)
# 	with open(path, 'r', encoding='utf-8') as fp:
# 		input_text = fp.read()
# 	filters = 'f_code_instr.py'
# 	output_text = pypandoc.convert_text(
# 		input_text,
# 		to='dokuwiki',
# 		format='markdown',
# 		extra_args=['--wrap=none', f'--filter={filters}'])
# 	print(output_text)



def main():
	scheme = SchemeDw2md('scheme.json')

if __name__ == '__main__':
	main()

# print(pypandoc.get_pandoc_formats())