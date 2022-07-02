from abc import ABC, abstractmethod

class Monitor(ABC):

    @abstractmethod
    def get(self):
        pass

    def buildNamedOutput(data, names):
        if len(data) != len(names):
            return 'ERROR: buildNamedOutput(): length of data and names are not the same'
        toreturn = "{"
        for i in range(len(data)):
            toreturn += names[i] + ':' + str(data[i])
            if i < len(data) -1:
                toreturn += ','
        toreturn += '}'
        #encapsulating the return in a list prevents daemon from splitting string into another tuple
        return [toreturn]
