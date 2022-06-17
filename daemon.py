#!/usr/bin/python3.8

'''
This is the daemon that runs in the background pulling sensor temp info and saving it into a file.
'''

import subprocess
import json
import os

cmd = ['sensors', '-j']

warning_threshold = 75
critical_threshold = 85

def get_temps():
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    body = json.loads(output)
    return body['k10temp-pci-00c3']['Tctl']['temp1_input']

#create dir if it doesn't exist
if not os.path.exists(os.path.expanduser('~') + '/.tempmonitor/'):
    os.mkdir(os.path.expanduser('~') + '/.tempmonitor/')
    
#clear old files
try:
    os.remove(os.path.expanduser('~') + '/.tempmonitor/temp.dat')
except:
    f = open(os.path.expanduser('~') + '/.tempmonitor/temp.dat', 'w+')
    f.close()


import time

#TODO: use notify-send to push a notification to the desktop if temp exceeds threshold
while True:
    temp = get_temps()
    with open(os.path.expanduser('~') + '/.tempmonitor/temp.dat', 'a+') as f:
        f.write(str(temp))
        f.write('\n')
    time.sleep(5)

