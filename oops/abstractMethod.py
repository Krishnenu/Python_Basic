from abc import ABC,abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("runnig...")

c1=Laptop()
c1.process()


