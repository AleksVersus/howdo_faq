import sys, os
import re

def convert_to_wiki(import_file, export_folder):
	with open(import_file, 'r', encoding='utf-8') as file:
		string_list = file.readlines()
	string_list = code_blocks(string_list)
	string_list = code_blocks_h(string_list)
	string_list = heading(string_list)
	string_list = hyperref(string_list)
	string_list = bolded(string_list)
	string_list = keywords(string_list)
	# for string in string_list:
	# 	print(string[:-1])
	export_file = os.path.splitext(os.path.split(import_file)[1])[0]+'.export.txt-light'
	with open(f'{export_folder}\\{export_file}','w',encoding='utf-8') as file:
		file.writelines(string_list)
		

def code_blocks(string_list):
	new_string_list = []
	for string in string_list:
		match_open = re.match(r'^\s*```qsp$', string)
		match_close = re.match(r'^\s*```$', string)
		if not match_open is None:
			new_string_list.append('<sxh qsp>\n')
		elif not match_close is None:
			new_string_list.append('</sxh>\n')
		else:
			new_string_list.append(string)
	return new_string_list

def code_blocks_h(string_list):
	new_string_list = []
	for string in string_list:
		match_open = re.match(r'^\s*```\w+$', string)
		match_close = re.match(r'^\s*```$', string)
		if not match_open is None:
			new_string_list.append('<sxh>\n')
		elif not match_close is None:
			new_string_list.append('</sxh>\n')
		else:
			new_string_list.append(string)
	return new_string_list

def heading(string_list):
	new_string_list = []
	for string in string_list:
		head_1 = re.match(r'^(={2})([^=]+?)\1$', string)
		head_2 = re.match(r'^(={1})([^=]+?)\1$', string)
		head_3 = re.match(r'^(-{2})(.+?)\1$', string)
		head_4 = re.match(r'^(-{1})(.+?)\1$', string)
		head_5 = re.match(r'^(\+{2})(.+?)\1$', string)
		head_6 = re.match(r'^(\+{1})(.+?)\1$', string)
		if not head_1 is None:
			new_string_list.append(f'====== {head_1.group(2)} ======\n')
		elif not head_2 is None:
			new_string_list.append(f'===== {head_2.group(2)} =====\n')
		elif not head_3 is None:
			new_string_list.append(f'==== {head_3.group(2)} ====\n')
		elif not head_4 is None:
			new_string_list.append(f'=== {head_4.group(2)} ===\n')
		elif not head_5 is None:
			new_string_list.append(f'== {head_5.group(2)} ==\n')
		elif not head_6 is None:
			new_string_list.append(f'= {head_6.group(2)} =\n')
		else:
			new_string_list.append(string)
	return new_string_list

def hyperref(string_list):
	new_string_list = []
	for string in string_list:
		match_list = re.findall(r'\[([^\]\[]*?)\]\(([^\(\)]*?)\)', string)
		if not match_list is None:
			for match in match_list:
				string = string.replace(f'[{match[0]}]({match[1]})', f'[[{match[1]}|{match[0]}]]')
			new_string_list.append(string)
		else:
			new_string_list.append(string)
	return new_string_list

def bolded(string_list):
	new_string_list = []
	for string in string_list:
		match_list = re.findall(r'`([^`]+?)`', string)
		if not match_list is None:
			for match in match_list:
				string = string.replace(f'`{match}`', f'**{match}**')
			new_string_list.append(string)
		else:
			new_string_list.append(string)
	return new_string_list

def keywords(string_list):
	keywords = re.compile(r'(?i:\*\*(if|elseif|while|end|act|exec|local|view|inclib|addqst|openqst|opengame|savegame|killqst|cmdclr|cmdclear|all|close|exit|play|settimer|menu|unsel|unselect|jump|copyarr|delact|wait|killall|dynamic|killvar|delobj|addobj|killobj|cls|cla|gs|xgt|gt|goto|gosub|xgoto|refint|showobjs|showstat|showacts|showinput|msg|\*pl|\*nl|\*clr|\*clear|\*p|pl|nl|clr|clear|p|nosave|disablescroll|disablesubex|debug|usehtml|bcolor|fcolor|lcolor|fsize|\$counter|\$ongload|\$ongsave|\$onnewloc|\$onactsel|\$onobjsel|\$onobjadd|\$onobjdel|\$usercom|\$fname|\$backimage|\$args|args|result|\$result|obj|isplay|len|rgb|msecscount|no|and|mod|countobj|instr|isnum|val|loc|or|rnd|rand|arrsize|arrpos|arrcomp|strcomp|strpos|\$input|\$user_text|\$usrtxt|\$desc|\$maintxt|\$stattxt|\$qspver|\$curloc|\$selobj|\$selact|\$curacts|\$mid|\$ucase|\$lcase|\$trim|\$replace|\$getobj|\$str|\$strfind|iif|dyneval|func|max|min|\$iif|\$dyneval|\$func|\$max|\$min|set|let)\*\*)')
	new_string_list = []
	for string in string_list:
		match_list = re.findall(keywords, string)
		if not match_list is None:
			for match in match_list:
				string = string.replace(f'**{match}**', f"''**{match.upper()}**''")
			new_string_list.append(string)
		else:
			new_string_list.append(string)
	return new_string_list

if __name__=="__main__":
	import_file='D:\\my\\projects\\howdo_faq\\[source]\\wiki.txt\\07_programming\\03_help_coding.txt-light'
	export_folder='D:\\my\\projects\\howdo_faq\\[source]\\wiki.qsp.org\\[export]'
	convert_to_wiki(import_file, export_folder)