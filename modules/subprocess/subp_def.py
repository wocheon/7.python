#!/usr/bin/env python
#! do not use file_nm subprocess.py

import sys
import subprocess

#host=sys.argv[1]

cmd=("ls -l")

def subp_def(cmd):
	res = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return res.stdout, res.stderr

std_out1, std_err1=subp_def(cmd)
print(type(std_out1))
#python3 - byte python2 -file

#python3
#print(std_out1.decode())

#python2
print(std_out1.readline())
