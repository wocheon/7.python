#!/usr/bin/env python

import os 

#PATH = os.getcwd() 
#file_name = '/mkdirtest'
#print(PATH)
#print(file_name)
#os.mkdir(PATH + file_name)

# makedirs ( use python3 )
PATH = os.getcwd()
file_nm = '/mkdirtest/a/b/c'
print(PATH)
print(file_nm)
#os.makedirs(PATH + file_nm, exist_ok = False)
os.makedirs(PATH + file_nm, exist_ok=True)
