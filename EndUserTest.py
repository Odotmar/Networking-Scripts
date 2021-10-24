#!/usr/bin/env python3

import subprocess
import sys

#Sets location for files
path_for_output = "~/Desktop/Sohonet-Triage.txt"

#Get customer public IP
cust_pub_ip = subprocess.run(["curl ifconfig.me"])
#Get OS Info
cust_os = subprocess.run(["/ etc / os - release | grep PRETTY "])

myoutput = open(path_for_output,'w+')

p = Popen([cust_os,cust_pub_ip], stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True)


with open(path_for_output,"r") as f:
    print(f.read())
