''' abstract strategy interface '''
from abc import ABC, abstractmethod

class Strategy(ABC):
    ''' abstract strategy interface for different algorithms '''
    @abstractmethod
    def execute(self, data):
        pass