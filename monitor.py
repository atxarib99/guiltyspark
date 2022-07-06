from abc import ABC, abstractmethod
import time

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


