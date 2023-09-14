#!/usr/bin/env python
#! do not use file_nm subprocess.py

import subprocess
cmd = "ls -l"
res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
res_out, res_err = res.communicate()
print (res_out.decode('utf-8'))

