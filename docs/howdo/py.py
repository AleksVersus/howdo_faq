import os
import re

curfold = os.path.join(os.getcwd(), 'contents')
listdir = os.listdir(curfold)
for i, fold in enumerate(listdir):
	if os.path.isfile(fold):
		continue
	match = re.match(r'\d+_(.+)', fold)
	if match is not None:
		os.rename(os.path.join(curfold, fold), os.path.join(curfold, match.group(1)))