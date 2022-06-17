from monitor import Monitor

import subprocess
import json

class TempMonitor(Monitor):

    name = 'tempmonitor'

    def get(self):
        cmd = ['sensors', '-j']

        warning_threshold = 75
        critical_threshold = 85

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, error = process.communicate()
        body = json.loads(output)
        return body['k10temp-pci-00c3']['Tctl']['temp1_input']
