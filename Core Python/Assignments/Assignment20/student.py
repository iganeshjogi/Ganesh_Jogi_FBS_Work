'''
3. Create object of student class (Outside SY & TY package) having roll
number, name, SYMakrs and TYMarks. Add the marks of SY and TY
Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
"C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
of the student in proper format. '''


from SY import SYMarks
from TY import TYMarks

class Student:

    def __init__(self, roll_number, name, syMarks, tyMarks):

        self.roll_number = roll_number
        self.name = name
        self.syMarks = syMarks
        self.tyMarks = tyMarks

    def CalculateGrade(self):
        total = self.syMarks.computer + self.tyMarks.theory
        percentage = (total / 200) * 100

        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'PASS'
        else:
            return 'FAIL'

    def display(self):
        print("Roll Number :", self.roll_number)
        print("Name        :", self.name)
        print("Grade       :", self.CalculateGrade())


sy = SYMarks(40, 40, 40)
ty = TYMarks(40, 40)

s1 = Student(101, 'AMIT', sy, ty)

s1.display()