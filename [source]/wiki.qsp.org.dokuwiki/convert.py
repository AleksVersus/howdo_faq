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
	text = text.replace('</sxh>', '</code>')
	text = text.replace('\t*', '  *')
	text = text.replace('*  ', '* ')
	text = text.replace('\t', '  ')
	wf(text, 'pf.dokuwiki')
	return text

def postfiltration(text:str) -> str:
	""" Выполняется после прогона через pandoc """
	text = re.sub(r'\[(.*?)\]\{\.underline\}', r'<u>\1</u>', text)
	text = text.replace('-   ', '* ')
	text = text.replace('\r\n', '\n')
	text = text.replace(r'\"', '"')
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
	output_text = postfiltration(output_text)
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

def main():
	pypan_file('00_01_start.dokuwiki')
	# poop('..\\..\\docs\\howdo\\intro.md')

if __name__ == '__main__':
	main()

# print(pypandoc.get_pandoc_formats())