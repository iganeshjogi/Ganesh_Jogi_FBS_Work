class student:
    def __init__(self,roll, name, age):
        self.name = name
        self._roll = roll
        self.__age = age

    def __str__(self):
        return f'Name: {self.name}\tRollNo: {self._roll}\tAge: {self.__age}'
    
class AgriStudent(student):
    def display(self):
        print(self.name)
        print(self._roll)
        # print(self.__age) # private Specifier


s1 = AgriStudent(101, 'Vishal', 25)
s1.display()