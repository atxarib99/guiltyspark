'''
This file serves as the communicator to the recent 30 temps. It will show them using asciiplot to the user. The daemon will need not be interrupted for this.
'''

from asciiplot import asciiize
import os
import sys

args = sys.argv

def show_temp():
    with open(os.path.expanduser('~') + '/.tempmonitor/temp.dat', 'r') as f:
        temps = []
        for line in f.readlines():
            temps.append(float(line))
        domain = [i for i in range(0, len(temps))]
        if len(sys.argv) > 1:
            try:
                lastval = int(sys.argv[1])
                print(lastval)
                temps = temps[-1*lastval:]
            except:
                print('couldnt parse args')
        print(asciiize(temps, x_ticks=list(range(1,len(temps))), height=25))

show_temp()
