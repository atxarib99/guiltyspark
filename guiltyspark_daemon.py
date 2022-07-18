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

installPath = '/usr/local/guiltyspark/'

import time

#TODO: use notify-send to push a notification to the desktop if temp exceeds threshold
#for each monitor, run the get
while True:
    #reload monitors each time?
    #allows for deamon to run endlessly and for monitors to be hotswappable
    #doesnt allow for variables. Monitor will need to be serializable. TODO: create example.
    monitors = []
    #get all monitors in the modules path
    for item in os.listdir(installPath + '/modules'):
        if item[-3:] == '.py':
            print(item)
            monitors.append(importlib.import_module('modules.' + item[0:-3], item[0:-3]).MonitorImpl())

    for monitor in monitors:
        #continue
        with open(base + monitor.name + '.dat', 'a+') as f:
            towrite = ""
            got = monitor.get()
            try:
                got = list(got)
            except TypeError:
                got = [got]
            for item in list(got):
                towrite += str(item)
                towrite += ','
            towrite = towrite[0:len(towrite)-1]
            f.write(towrite)
            f.write('\n')
    time.sleep(5)
