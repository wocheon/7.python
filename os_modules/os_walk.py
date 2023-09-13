#!/usr/bin/env python

import os

list=os.walk('/root')
int=1

print ("###os.walk test###")
for curDir, dirs, files in list:
	print(str(int) + ".curDir : " + curDir)

	if len(dirs)>0:
		#print(len(dirs))
		print("---dirs---")

	for d in dirs:
		print(os.path.join(curDir, d))

	if len(dirs)>0:
		#print(len(dirs))
		print("---files---")

	for i in files:
		print("files : " + os.path.join(curDir, i))
	int = int +1
	

