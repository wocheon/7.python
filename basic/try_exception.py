#!/usr/bin/env python

import subprocess

file_nm="testfile"
cmd="cat testfile"

try:
	f=open(file_nm, "r")
	print(f.read())

except FileNotFoundError:
	print ("File Not exist")
except PermissionError:
	print ("Permission Denyed")
except:
	print ("Error occured")
	

try:
	f=open(file_nm, "r")
	print(f.read())

except Exception as e: 
	print("Exception: " , e)

