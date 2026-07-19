'''
3. Create a class MedicalStudent inherited from Student with following :

a. Data members as :
    i.  Specialization
    ii. MarksOfInternship

b. Add the following methods :
    i. Parameterized constructor
    ii. Display
    iii. Accept
    iv. override Method CalculateRank
    v. Override __str__ Method '''

from q1 import Student

class MedicalStudent(Student):

    def __init__(self, studentId=0, name='', age=0, percentage=0, specialization='', marksofinternship=0.0):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksofinternship = marksofinternship

    def display(self):
        super().display()

    def accept(self):
        super().accept()
        self.specialization = input('Enter Specialization: ')
        self.marksofinternship = input('Enter Marks of Internship: ')

    def calculateRank(self):
        if self.percentage >= 75:
            print("Excellent Rank")
        elif self.percentage >= 60:
            print("Good Rank")
        else:
            print("Average Rank")

    def __str__(self):
        return super().__str__() + f"""Specialization: {self.specialization}
        Internship marks : {self.marksofinternship}"""

m1 = MedicalStudent(201, 'Vishal', 25, 70, 'Dentist', 90)
m1.display()
m1.calculateRank()