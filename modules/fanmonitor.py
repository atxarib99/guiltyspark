from monitor import Monitor

import subprocess
import json

class MonitorImpl(Monitor):

    name = 'tempmonitor'

    def get(self):
        cmd = ['osx-cpu-temp', '-f']

        warning_threshold = 75
        critical_threshold = 85

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, error = process.communicate()
        output = str(output)
        outputs = output.split('\\n')
        fan1_per = outputs[1][outputs[1].index('(')+1:outputs[1].index(')')]  
        fan2_per = outputs[2][outputs[2].index('(')+1:outputs[2].index(')')]
        fan1_rpm = outputs[1][outputs[1].index('at')+3:]
        fan1_rpm = fan1_rpm[0:fan1_rpm.index('(')]
        fan1_rpm = fan1_rpm[0:fan1_rpm.index(' ')]

        fan2_rpm = outputs[2][outputs[2].index('at')+3:]
        fan2_rpm = fan2_rpm[0:fan2_rpm.index('(')]
        fan2_rpm = fan2_rpm[0:fan2_rpm.index(' ')]

        return fan1_per,fan2_per,fan1_rpm,fan2_rpm
