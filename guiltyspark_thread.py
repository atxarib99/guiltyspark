#!/usr/bin/python3.8

'''
This is the daemon that runs in the background pulling sensor temp info and saving it into a file.
'''

import subprocess
import json
import os
import importlib
import time

installPath = '/usr/local/guiltyspark/'
base = os.path.expanduser('~') + '/.guiltyspark/'


def setup():
    #clear log
    try:    
        os.remove(installPath + 'daemon.log')
    except:
        print('log file not found')
    finally:
        f = open(installPath + 'daemon.log', 'w+')
        f.write('start logging, ')
        f.write(str(time.time()))
        f.write('\n')
        f.close()

    #create dir if it doesn't exist
    if not os.path.exists(base):
        os.mkdir(base)


def run():
    setup()
    #TODO: use notify-send to push a notification to the desktop if temp exceeds threshold
    #for each monitor, run the get
    try:
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
                    try:
                        got = monitor.get()
                        try:
                            got = list(got)
                        except TypeError:
                            got = [got]
                        for item in list(got):
                            towrite += str(item)
                            towrite += ','
                        towrite = towrite[0:len(towrite)-1]
                        print(towrite)
                        f.write(towrite)
                        f.write('\n')
                    except Exception as exp:
                        with open(installPath+'daemon.log', 'a+') as log:
                            log.write(str(time.time()))
                            log.write(',')
                            log.write(monitor.name)
                            log.write('issue in get()\n')
                            time.sleep(5)
    except Exception as exp:
        with open(installPath+'daemon.log', 'a+') as log:
            log.write(str(time.time()))
            log.write(',')
            log.write(str(exp))
            log.write('\n')

