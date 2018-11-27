#!/usr/bin/env python3

import os

mdfiles = [os.path.join(root, name)
	for root, dirs, files in os.walk(os.getcwd())
	for name in files
	if name.endswith(('.md'))]

file_list = []
tag_list = []

def search(tag):
	j = 0
	for i in range(len(mdfiles)):
		with open(mdfiles[i]) as f:
			for l, line in enumerate(f):
				if line.strip() == tag:
					print(str(j) + ' ' + mdfiles[i])
					file_list.append(mdfiles[i])
					j = j + 1

with open ('.tags.txt', 'r') as f:
	for i, line in enumerate(f):
		print(str(i) + ' ' + line)
		tag_list.append(line.strip())

os.system('./.get_tags.py')			

ind = input('Enter the index of the tag you wish to search for: ')
print('\n')

search(tag_list[int(ind)])
print('\n')

yn = input('Would you like to open a file? (y = yes, n = no): ')
print('\n')

if yn == 'y':
	ind2 = input('Enter the index of the file you wish to open: ')
	os.system('xdg-open ' + file_list[int(ind2)])

f.close()	
