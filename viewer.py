'''
This file serves as the communicator to the recent 30 temps. It will show them using asciiplot to the user. The daemon will need not be interrupted for this.
'''

from asciiplot import asciiize
import os
import sys

args = sys.argv

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

def show_temp():
    with open(os.path.expanduser('~') + '/.guiltyspark/' + str(sys.argv[1]) + '.dat', 'r') as f:
        data = []
        for line in f.readlines():
            datapoint = line
            try:
                datapoint = datapoint.strip('(').strip(')').split(',')
            except:
                datapoint = [datapoint]
            
            if data == []:
                for i in range(len(datapoint)):
                    data.append([])
            index = 0
            for i in range(len(datapoint)):
                #handle %
                try:
                    data[i].append(float(datapoint[i]))
                except:
                    #try stripping '%' and try again
                    try:
                        data[i].append(float(datapoint[i].strip('%')))
                    except:
                        data[i].append(0)
            #temps.append(float(line))
        #domain = [i+1 for i in range(0, len(data[0]))]
        if len(sys.argv) > 2:
            try:
                lastval = int(sys.argv[2])
                print(lastval)
                for i in range(len(data)):
                    data[i] = data[i][-1*lastval:]
            except:
                print('couldnt parse args')
        for x in data:
            #check if data has 0 spread.
            if hasspread(x):
                print(asciiize(x, x_ticks=list(range(1,len(data[0]))), height=rows//len(data)-1, inter_points_margin=2))
            else:
                print('data has no spread')

def hasspread(data):
    diff = 0
    lastval = 0
    for x in data:
        if x - lastval != 0:
            return True
    return False


show_temp()
