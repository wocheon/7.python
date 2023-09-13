#!/usr/bin/env python

import os 

path='/root'

print("---" + path + " file list---")
for i in os.listdir(path):
	print i
