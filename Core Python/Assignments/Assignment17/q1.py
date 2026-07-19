'''
1. Create a class Student with following

a. data members :
    i. StudentId
    ii. Name
    iii. Age
    iv. Percentage

b. Add the following methods :
    i. Parameterized constructor
    ii. Display
    iii. Accept
    iv. Method CalculateRank
    v. Override __str__ Method '''


class Student:
    
    def __init__(self, studentId=0, name='', age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def display(self):
        print(self)
        
    def accept(self):
        self.studentId  = int(input("Enter Student ID: "))
        self.name       = input("Enter Name: ")
        self.age        = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def calculateRank(self):
        print("Rank calculation not implemented.")

    def __str__(self):
        return(f"""
        ID            : {self.studentId}  
        Name          : {self.name}
        Age           : {self.age}          
        Percentage    : {self.percentage}          
        """)