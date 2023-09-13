#!/usr/bin/env python

import os 

file_nm="rename_test/test.txt"
dir_nm="rename_test"


if os.path.isfile(file_nm):
	os.remove(file_nm)
	print("#" + file_nm + " :  Deleted")
else:
	print("#" + file_nm + " :  Not Exist")

if os.path.isdir(dir_nm):
	os.rmdir(dir_nm)
	print("#" + dir_nm + " :  Deleted")
else:
	print("#" + dir_nm + " :  Not Exist")

