#!/usr/bin/env python3

import sys,os 
import subprocess

def sub_run(cmd):
	res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
	return res.stdout.decode()

def execute(cmd):
	out=subprocess.Popen(cmd, shell=True , stdout=subprocess.PIPE)
	res=out.stdout.readline().decode()
	return str(res).strip()

def check_load(load_avg):
	if load_avg>=critic_level:
		res=(f"Critical : Load Average ({load_avg})")
	elif load_avg>=warn_level:
		res=(f"Warnning : Load Average ({load_avg})")
	else:
		res=(f"OK : Load Average ({load_avg})")
	return res

def check_mem(free_m):
	total_m=int(free_m[0])
	avail_m=int(free_m[1])
	mem_res = round(avail_m / total_m * 100 ,2) 

	if mem_res>=mem_critic:
		res=(f"Critical : Memory Usage ({mem_res})")
	elif mem_res >=mem_warn:
		res=(f"Warnning : Memory Usage ({mem_res})")
	else:
		res=(f"OK : Memory Usage ({mem_res})")
	return res


warn_level=1
critic_level=3
mem_warn=80
mem_critic=90


date="date '+%y%m%d'"
timestamp="date '+%Y-%m-%d %H:%M'"
up="cat /proc/loadavg | awk '{print $1}' | awk -F. '{print $1}'"
free="free -m | grep ^Mem | awk '{print $2 \",\" $7}'"
info_1="hostname"
info_2="hostname -i | awk '{print $2}'"
info_3="cat /etc/*release* | grep PRETTY_NAME | awk -F'=' '{print $2}' | sed 's/\"//g'"


load_avg=int(execute(up)) 
free_m=execute(free).split(',')
file_nm=f"{execute(info_1)}_{execute(date)}.log"


if os.path.isfile(file_nm):
	f=open(file_nm, "w")
else:
	f=open(file_nm, "a")

f.write("#Server Info\n")
f.write(f"Timestamp : {execute(timestamp)} \n")
f.write(f"Hostname : {execute(info_1)}\nIP: {execute(info_2)}\nOS: {execute(info_3)}\n")

f.write("\n#load_average\n")
f.write(f"{check_load(load_avg)}\n")

f.write("\n#free\n")
f.write(f"{check_mem(free_m)}\n")

f.write("\n#uptime\n")
f.write(sub_run("uptime"))
	
f.write("\n#mpstat\n")
f.write(sub_run("mpstat -P ALL"))

f.write("\n#vmstat\n")
f.write(sub_run("vmstat"))

f.write("\n#Top 10 Process Sort by CPU Usage\n")
f.write(sub_run("ps -aux --sort -pcpu | head -n 11"))

f.write("\n#Top 10 Process Sort by Memory Usage\n")
f.write(sub_run("ps -aux --sort -rss | head -n 11"))

f.close()

f = open(file_nm, 'r')
while True:
        line = f.read()
        if not line:
                break
        print(line)
f.close
