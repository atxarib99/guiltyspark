from abc import ABC, abstractmethod
import time
import os

class Monitor(ABC):

    @abstractmethod
    def get(self):
        pass

    def buildNamedOutput(data, names, includeTimestamp=False):
        if len(data) != len(names):
            return 'ERROR: buildNamedOutput(): length of data and names are not the same'
        if includeTimestamp:
            data.insert(0, time.time())
            names.insert(0, 'timestamp')
        toreturn = "{"
        for i in range(len(data)):
            toreturn += names[i] + ':' + str(data[i])
            if i < len(data) -1:
                toreturn += ','
        toreturn += '}'
        #encapsulating the return in a list prevents daemon from splitting string into another tuple
        return [toreturn]

    def getData(self):
        with open(os.path.expanduser('~') + '/.guiltyspark/' + str(self.name) + '.dat', 'r') as f:
            data = []
            datanames = []
            for line in f.readlines():
                datapoint = line
                #its a dict, format this data point, and get datanames
                if '{' in datapoint:
                    datapoint = datapoint.strip('{}\n').split(',')
                    newdatapoint = []
                    for point in datapoint:
                        #populate datanames if not already done
                        datanames.append(point.split(':')[0])
                        newdatapoint.append(point.split(':')[1])
                    datapoint = newdatapoint
                #else its a single value
                else:
                    datapoint = [datapoint]
                    datanames.append(self.name)

                if data == []:
                    for i in range(len(datapoint)):
                        data.append([])

                #build data list
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
            return data, datanames
