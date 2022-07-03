from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.len = 6
        self.breadth = 7

    def printarea(self):
        return self.len * self.breadth

rect1 = rectangle()
print(rect1.printarea())