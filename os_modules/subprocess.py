#!/usr/bin/env python

import os

os.system("ls -l")
file_nm ="ps_ef.log"

if os.path.isfile(file_nm):
        f = open(file_nm, 'w')
else:
        f = open(file_nm, 'a')

f.write(res)
f.close()

f = open(file_nm, 'r')
while True:
        line = f.readline()
        if not line:
                break
        print(line)
f.close
#
