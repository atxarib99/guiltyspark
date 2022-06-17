#!/usr/bin/python3.8

'''
This is the daemon that runs in the background pulling sensor temp info and saving it into a file.
'''

import subprocess
import json
import os
from tempmonitor import TempMonitor

base = os.path.expanduser('~') + '/.guiltyspark/'
#create dir if it doesn't exist
if not os.path.exists(base):
    os.mkdir(base)
    
#clear old files
try:
    os.remove(base+'temp.dat')
except:
    f = open(base+'temp.dat', 'w+')
    f.close()

import time

#TODO: use notify-send to push a notification to the desktop if temp exceeds threshold
monitors = []
monitors.append(TempMonitor())

while True:
    for monitor in monitors:
        with open(base + monitor.name + '.dat', 'a+') as f:
            f.write(str(monitor.get()))
            f.write('\n')
    time.sleep(5)
