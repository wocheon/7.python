#!/usr/bin/env python

import subprocess
import sys


#proc = subprocess.Popen(args=[sys.executable, "stdin_test.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
proc = subprocess.Popen("python stdin_test.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#proc = subprocess.Popen("python stdin_test.py", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

proc.stdin.write('Stdin_Input_Test\n')
proc.stdin.flush()
print(proc.stdout.readline())

sh_proc = subprocess.Popen("sh read_var.sh", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
sh_stdout, sh_stderr=sh_proc.communicate(input="Stdin_Input_test : /bin/bash\n")

print(sh_stdout)
