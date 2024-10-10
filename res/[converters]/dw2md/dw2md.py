from tothconv import SchemeDw2md

def main():
	scheme_path = '..\\..\\..\\[source]\\wiki.qsp.org.dokuwiki\\scheme.json'

	scheme = SchemeDw2md(scheme_path)
	scheme.convert_to_md()

if __name__ == '__main__':
	main()