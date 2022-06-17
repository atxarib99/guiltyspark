from abc import ABC, abstractmethod

class Monitor(ABC):

    @abstractmethod
    def get(self):
        pass
