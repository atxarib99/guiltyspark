#!/usr/bin/python3.8

'''
This is the daemon that runs in the background pulling sensor temp info and saving it into a file.
'''

import subprocess
import json
import os
import importlib

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

#get all monitors in the modules path
for item in os.listdir('./modules'):
    if item[-3:] == '.py':
        print(item)
        monitors.append(importlib.import_module('modules.' + item[0:-3], item[0:-3]).MonitorImpl())

#for each monitor, run the get
while True:
    for monitor in monitors:
        print(monitor.get())
        #continue
        with open(base + monitor.name + '.dat', 'a+') as f:
            towrite = ""
            for item in list(monitor.get()):
                towrite += str(item)
                towrite += ','
            towrite = towrite[0:len(towrite)-1]
            f.write(towrite)
            f.write('\n')
    time.sleep(5)
