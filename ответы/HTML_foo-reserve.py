import sys, os, re, json
import random
from HTML_lib import *


if __name__=="__main__":
	
	db=NewDataBase()
	db.setCurFile('00000000')
	with open('.\\92_дополнительные тексты\\пример SOH.light-txt','r',encoding='utf-8') as file:
		string_list=file.readlines()
	text_list=convertSOHBlock(string_list,db)
	for i in text_list:
	 	print(i)