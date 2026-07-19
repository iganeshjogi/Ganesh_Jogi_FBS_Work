'''
2. Create a derived class from Student as EnggStudent with :

a. Data members as :
    i. Branch
    ii. InternalMarks

b. Add the following methods :
    i. Parameterized constructor
    ii. Display
    iii. Accept
    iv. override Method CalculateRank
    v. Override __str__ Method '''

from q1 import Student

class EnggStudent(Student):
    
    def __init__(self, studentId=0, name='', age=0, percentage=0, branch='', internalMarks=0.0):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def display(self):
        super().display()

    def accept(self):
        super().accept()
        self.branch        = input('Enter Branch: ')
        self.internalMarks = float(input('Enter Internal Marks: '))

    def calculateRank(self):
        if self.percentage >= 75:
            print("Excellent Rank")
        elif self.percentage >= 60:
            print("Good Rank")
        else:
            print("Average Rank")

    def __str__(self):
        return super().__str__() + f"""Branch        : {self.branch}          
        Internal Marks: {self.internalMarks}          
        """
    
e1 = EnggStudent(101, 'Ganesh', 22, 90.20, 'Electrical', 40)
e1.display()
e1.calculateRank()