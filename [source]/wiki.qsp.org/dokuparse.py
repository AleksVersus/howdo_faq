# Перепарсивание dokuwiki wiki.qsp.org

import sys, os
import re
from bs4 import BeautifulSoup as bs
import fos


def getSoup(file_path):
	with open(file_path,'r',encoding='utf-8') as file:
		text=file.read()
	return bs(text,"html.parser")

def clearText(old_text):
	text_strings=old_text.split('\n')
	prev_is_space=False
	prev_is_li=False
	new_text=[]
	for string in text_strings:
		space=re.search(r'^[\s\n\t]*$',string)
		li=re.match(r'^\s*\*\s+',string)
		if space!=None:
			# текущая строка пуста
			if (not prev_is_space) and (not prev_is_li):
				# предыдущая не пуста и не является частью списка
				new_text.append(string+'\n') # добавляем текущую к списку строк
				prev_is_space=True # помечаем, что уже есть пустая строка
			else:
				# предыдущая тоже пуста или является частью списка
				pass # ничего не делаем
		else:
			# текущая не пуста
			# string=string.replace("'","''")
			new_text.append(string+'\n')
			prev_is_space=False
			if li!=None:
				prev_is_li=True
			else:
				prev_is_li=False
	return new_text

def mkFile(file_path,export_folder,string_list):
	# для начала нам нужно вычислить имя файла и папки
	folder_path,file_ext_name=os.path.split(file_path)
	folder_name=os.path.split(folder_path)[1]
	file_name=os.path.splitext(file_ext_name)[0]
	exit_folder_path=f"{export_folder}\\{folder_name}"
	if not os.path.isdir(exit_folder_path):
		os.mkdir(exit_folder_path)
	with open(f"{exit_folder_path}\\{file_name}.txt-light",'w',encoding='utf-8') as file:
		file.writelines(string_list)


def convertPage(soup):
	dokuwiki_content=soup.find('div',{'id':'dokuwiki__content'})
	if dokuwiki_content!=None:
		pageId=dokuwiki_content.find('div',{'class':'pageId'}).text.replace(':','_')
		page_group=dokuwiki_content.find('div',{'class':'page group'})
		dw_toc=page_group.find('div',{'id':'dw__toc'})
		if dw_toc!=None:
			dw_toc.decompose()
		images=page_group.find_all('img')
		for image in images:
			new_tag=soup.new_tag('a',href=f'{image["src"]}')
			new_tag.string=f"%image%"
			image.insert_after(new_tag)
		h2=page_group.find('h2')
		if h2!=None:
			h2.string=f"=={h2.text}==\n[:{pageId}]\n\n[:{h2['id']}]"
		hrefs=page_group.find_all('a')
		for href in hrefs:
			href.string=f"[{href.text}]({href['href']})"
		h3_s=page_group.find_all('h3')
		for h3 in h3_s:
			h3.string=f"={h3.text}=\n[:{h3['id']}]"
		h4_s=page_group.find_all('h4')
		for h4 in h4_s:
			h4.string=f"--{h4.text}--\n[:{h4['id']}]"
		h5_s=page_group.find_all('h5')
		for h5 in h5_s:
			h5.string=f"-{h5.text}-\n[:{h5['id']}]"
		h6_s=page_group.find_all('h6')
		for h6 in h6_s:
			h6.string=f"++{h6.text}++\n[:{h6['id']}]"
		codes=page_group.find_all('pre',{'class':'brush: qsp'})
		for code in codes:
			code.string=f"\n```qsp\n{code.text}\n```"
		strongs=page_group.find_all('strong')
		for strong in strongs:
			strong.string=f"`{strong.text}`"
		level=10
		while level>0:
			lp=f'level{level}'
			li_prove=page_group.find('li',{'class':lp})
			# print(lp, li_prove)
			if li_prove!=None:
				li_s=page_group.find_all('li',{'class':lp})
				for li in li_s:
					tab='\t'*level+'* '
					li.string=f"{tab}{li.text}"
			level-=1
		# подготавливаем текст
		prep_text=clearText(page_group.text)
		return prep_text
	else:
		return None

def convertFiles(files_paths_list,export_folder):
	if not os.path.isdir(export_folder):
		os.mkdir(export_folder)
	for file_path in files_paths_list:
		soup=getSoup(file_path) # получаем суп
		prep_text_string_list=convertPage(soup) # конвертим суп в текст
		if prep_text_string_list!=None:
			mkFile(file_path,export_folder,prep_text_string_list) # записываем файл

def main():
	current_folder = os.path.abspath(os.getcwd())
	folder = fos.NewFolder(current_folder)
	files_list=folder.getFilesList(filt=r'.*\.html$/re')

	convertFiles(files_list,f'{current_folder}\\[export]')


if __name__=="__main__":
	main()
	