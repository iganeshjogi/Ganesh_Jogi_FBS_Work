class Emp:
    company = 'FBS'
    @staticmethod
    def companyPolicy():
        print('Office time 9 to 5')

    def __init__ (self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def display (self):
        print(f'id = {self.id}\tname = {self.name}\tsal = {self.sal}')

class HR(Emp):
    def __init__(self,id, name, sal, commission):
        super.__init__(id, name, sal)
        self.commission = commission


e1 = Emp(10,'Ganesh', 789)
e1.display()

e2 = Emp(12,'Vishal',15000)
e2.display()

print(Emp.company)
Emp.companyPolicy()
e1.companyPolicy()