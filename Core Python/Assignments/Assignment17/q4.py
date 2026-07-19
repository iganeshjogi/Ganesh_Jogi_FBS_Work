'''
4. Create a class College which has collection of students.
    Add the following methods :
    a. Parameteried constructor for number of students.
    b. AddStudent
    c. GetStudent
    d. RemoveStudent
    e. Override __str__ Method '''


from q1 import Student

class College:

    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print("Student Added Successfully.")
        else:
            print("College is Full.")

    def getStudent(self, index):
        if 0 <= index < len(self.students):
            return self.students[index]
        else:
            return "Invalid Student Index."

    def removeStudent(self, index):
        if 0 <= index < len(self.students):
            removedStudent = self.students.pop(index)
            print(f"{removedStudent.name} Removed Successfully.")
        else:
            print("Invalid Student Index.")

    def __str__(self):
        result = f"College Capacity : {self.capacity}\n"
        result += "Students Details\n"
        result += "-" * 40 + "\n"

        if len(self.students) == 0:
            result += "No Students Available."
        else:
            for student in self.students:
                result += str(student)
                result += "\n" + "-" * 40 + "\n"

        return result


# ------------------ Testing ------------------

c1 = College(3)

s1 = Student(101, "Ganesh", 22, 90.2)
s2 = Student(102, "Rahul", 21, 85.5)
s3 = Student(103, "Vishal", 23, 78.4)

c1.addStudent(s1)
c1.addStudent(s2)
c1.addStudent(s3)

print(c1)

print("Student at Index 1")
print(c1.getStudent(1))

c1.removeStudent(1)

print("\nAfter Removing Student\n")
print(c1)