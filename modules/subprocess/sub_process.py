#!/usr/bin/env python
#! do not use file_nm subprocess.py

import os
import subprocess

cmd = "ls -l"

print("# subprocess.call")
subprocess.call(["echo","calltest"])
subprocess.call("echo calltest2", shell=True)

res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
print ("#res")
print (res)
print ("#res.stdout")
print (res.stdout)
print ("#res.stdout.decode()")
print (res.stdout.decode())

