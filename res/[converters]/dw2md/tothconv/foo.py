import os

__all__ = [
	'wf'

]

def wf(text:str, path:str) -> None:
	fullpath = os.path.abspath(path)
	with open(fullpath, 'w', encoding='utf-8') as fp:
		fp.write(text)

