import pypandoc
import os
import re
import sys
import json

with open('scheme.json', 'r', encoding='utf-8') as fp:
	scheme = json.load(fp)

def wf(text:str, path:str) -> None:
	fullpath = os.path.abspath(path)
	with open(fullpath, 'w', encoding='utf-8') as fp:
		fp.write(text)

def prefiltration(text:str) -> str:
	""" Выполняется до прогона через pandoc """
	text = text.replace('<sxh qsp>', '<code qsp>')
	text = text.replace('<sxh>', '<code plain>')
	text = text.replace('</sxh>', '</code>')
	# text = text.replace('\t*', '  *')
	# text = text.replace('*  ', '* ')
	text = text.replace('\t', '  ')
	wf(text, 'pf.dokuwiki')
	return text

def postfiltration(text:str, path:str) -> str:
	""" Выполняется после прогона через pandoc """
	relpath = os.path.relpath(scheme[path], '..\\..\\docs\\wiki')
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
	if fold != '':
		text = text.replace('](/', '](../')
	else:
		text = text.replace('](/', '](')
	return text	

def pypan_file(path:str) -> None:
	name = os.path.split(path)[1]
	name, ext = os.path.splitext(name)
	fullpath = os.path.abspath(path)
	with open(fullpath, 'r', encoding='utf-8') as fp:
		input_text = fp.read()
	input_text = prefiltration(input_text)
	output_text = pypandoc.convert_text(
		input_text,
		to='markdown',
		format='dokuwiki',
		# filters = ['f_code_instr.py'],
		extra_args=['--wrap=none'])
	output_text = postfiltration(output_text, path)
	match = re.match(r'\d+_(\d+)_\w+', name)
	if match is not None:
		output_text = f'---\nsidebar_position: {int(match.group(1))}\n---\n' + output_text
	wf(output_text, scheme[path])

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

def convert_by_scheme():
	for path in scheme.keys():
		print('convert', path, 'to', scheme[path])
		pypan_file(path)

def main():
	# pypan_file('help\\01_02_locations.dokuwiki')
	# poop('..\\..\\docs\\howdo\\intro.md')

	convert_by_scheme()

if __name__ == '__main__':
	main()

# print(pypandoc.get_pandoc_formats())