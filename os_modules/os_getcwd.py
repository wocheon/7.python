#!/usr/bin/env python

import os 

#os.environ
print("# os.environ[\'PATH\']")
print(os.environ['PATH'])
print("\n")

#os.getcwd, os.chdir
print("# os.getcwd, os.chdir")
print("pwd : " + os.getcwd())
change_path="/root/python"
os.chdir(change_path)
print("# change pwd")
print("pwd : " + os.getcwd())
