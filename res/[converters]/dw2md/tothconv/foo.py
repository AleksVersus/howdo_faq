import os

__all__ = [
	'wf',
	'safe_mk_fold'
]

def safe_mk_fold(new_path:str) -> None:
	""" Safe make dir with making all chain of dir """
	if not os.path.isdir(new_path):
		os.makedirs(new_path)

def wf(text:str, path:str) -> None:
	fullpath = os.path.abspath(path)
	print(fullpath)
	with open(fullpath, 'w', encoding='utf-8') as fp:
		fp.write(text)

