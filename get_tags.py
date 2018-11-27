#!/usr/bin/env python3

import os, re

mdfiles = [os.path.join(root, name)
	for root, dirs, files in os.walk(os.getcwd())
	for name in files
	if name.endswith(('.md'))]

tags = []

for i in range(len(mdfiles)):
	with open(mdfiles[i]) as f:
		for l, line in enumerate(f):
			if re.search(r"\[(\w+)\]", line):
				tags.append(line.strip())

t = open('tags.txt', 'w')
t.close()

tags = list(set(tags))

for i in range(len(tags)):
	temp = str(tags[i])
	t = open('tags.txt', 'a')
	t.write(temp)
	t.write('\n')
	t.close()