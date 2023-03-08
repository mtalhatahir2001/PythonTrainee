from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def parameter(self):
        pass

    @abstractmethod
    def area(self):
        pass