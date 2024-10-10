import os
from tothconv import SchemeDw2md

def main():
	scheme_path = os.path.abspath('..\\..\\..\\[source]\\wiki.qsp.org.dokuwiki\\scheme.json')
	output_folder = os.path.abspath('..\\..\\..\\[source]\\wiki.qsp.org.out')

	scheme = SchemeDw2md(scheme_path)
	scheme.convert_to_dw(output_folder)

if __name__ == '__main__':
	main()