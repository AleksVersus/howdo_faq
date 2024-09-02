import pypandoc
import os


def main():
	print(pypandoc.get_pandoc_version())
	print(pypandoc.get_pandoc_path())
	print(pypandoc.get_pandoc_formats())
	# output = pypandoc.convert_file(os.path.abspath('00_01_start.txt'), to='markdown', format='dokuwiki')
	with open(os.path.abspath('00_01_start.txt'), 'r', encoding='utf-8') as fp:
		text = fp.read()
	output = pypandoc.convert_text(text, to='html', format='dokuwiki')
	with open(os.path.abspath('00_01_start.html'), 'w', encoding='utf-8') as fp:
		fp.write(output)

if __name__ == '__main__':
	main()

# print(pypandoc.get_pandoc_formats())