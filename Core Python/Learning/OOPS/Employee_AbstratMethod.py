from abc import ABC,abstractmethod
class Emp(ABC):
    def __init__ (self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display (self):
        print(f'id = {self.id}\tname = {self.name}\tsal = {self.sal}')

    def SetId(self,id):
        self.id = id

    def GetId(self):
        return self.id
    
    def __del__(self):
        print('End of Emp object')
    
    @abstractmethod
    def calSal():
        pass

class Hr(Emp):
    def __init__(self, id, name, sal, com = 120):
        super().__init__(id, name, sal)
        self.com = com
    
    def setcom(self,com):
        self.com = com

    def getcom(self):
        return self.com
    
    def __str__(self):
        return super().__str__()+'\tCommission = '+str(self.com)
    
    def __del__(self):
        print('End of Hr object')

    def calSal(self):
        print(self.sal + self.com,'Rs')



h1 = Hr(7, 'Harman', 12345, 121)
h1.calSal()