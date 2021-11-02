import sys, os, re, json
import random
from HTML_lib import *


def convertSOHBlock(string_list,base_):
	# конвертируем блок section of head в список
	new_string_list=[]
	quazy_file=NewQuazy(string_list,base_)
	new_string_list=quazy_file.getHTML(base_)
	i=0
	for string in new_string_list:
		metahead=re.match(r'^<(/?)(h\d+)>',string)
		if metahead!=None:
			lev=int(re.search(r'\d+',metahead.group(2)).group(0))+6
			if metahead.group(1)!='/':
				new_string_list[i]=new_string_list[i].replace(metahead.group(0),f'<p class="head_{lev}">')
			else:
				new_string_list[i]=new_string_list[i].replace(metahead.group(0),f'</p>')
		i+=1
	return new_string_list

if __name__=="__main__":
	
	db=NewDataBase()
	db.setCurFile('00000000')
	with open('.\\92_дополнительные тексты\\пример списка.light-txt','r',encoding='utf-8') as file:
		string_list=file.readlines()
	text_list=convertListBlock(string_list,db)
	for i in text_list:
	 	print(i)