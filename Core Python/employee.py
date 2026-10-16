class Employee:

    def __init__(self, id, name, salary, dept):
        self.id = id
        self.name = name 
        self.salary = salary
        self.dept = dept

    def toTuple(self):
        return (self.id, self.name, self.salary, self.dept)
    