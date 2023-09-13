#!/usr/bin/env python

import os 

file_nm="test.txt"

if os.path.isfile(file_nm):
	f = open(file_nm, 'a')
	f.write("testfile\n")
	f.close()

file_nm= os.path.abspath(file_nm)

print("# file : " + file_nm + "\n" )

print("# os.path.abspath : " + os.path.abspath(file_nm) + "\n")

print("# os.path.exists : " + str(os.path.exists(file_nm)) + "\n")

print("# os.path.basename : " + os.path.basename(file_nm))
print("\t # file_nm.split('/')[-1] : " + file_nm.split('/')[-1] + "\n")

print("# os.path.dirname : " + os.path.dirname(file_nm) + "\n")

dir_nm, base_nm=os.path.split(file_nm)
print("# os.path.split : dir_nm, base_nm=os.path.split(file_nm) ")
print("\t# os.path.split - dir_nm : " + dir_nm  )
print("\t# os.path.split - base_nm : " + base_nm  + "\n")

print("# os.path.isfile - base_nm : " + str(os.path.isfile(base_nm)))
print("# os.path.isdir - dir_nm : " + str(os.path.isdir(dir_nm)) + "\n")

print("# os.path.join(dir_nm,base_nm) : " + os.path.join(dir_nm,base_nm) + "\n")
