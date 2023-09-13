#!/usr/bin/env python

import os 

PATH = os.getcwd() 
file_name = '/mkdirtest'
os.mkdir(PATH + file_name)

print ("#" + PATH + file_name + " Created")

if os.path.isfile('mkdirtest/test.txt'):
  f = open('mkdirtest/test.txt', 'w')
else:
  f = open('mkdirtest/test.txt', 'a')

f.write("testfile")
f.close()

change_nm="/rename_test"
os.rename(PATH + file_name, PATH + change_nm)
print ("# renamed : " + PATH + change_nm )


print("--- rename_test file list---")
for i in os.listdir("rename_test"):
        print i

print("# cat rename_test/test.txt")

f = open('rename_test/test.txt', 'r')
while True:
	line = f.readline()
	if not line:
		break
	print(line)
f.close
