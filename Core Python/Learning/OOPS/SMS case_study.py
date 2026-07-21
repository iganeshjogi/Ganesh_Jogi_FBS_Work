class Student:
    def __init__(self, roll_no, name, age):
        self._roll_no = roll_no
        self._name = name
        self._age = age
        
    def get_roll_no(self):
        return self._roll_no
        
    def get_name(self):
        return self._name
        
    def get_age(self):
        return self._age
        
    def set_roll_no(self, roll_no):
        self._roll_no = roll_no
        
    def set_name(self, name):
        self._name = name
        
    def set_age(self, age):
        self._age = age
        
    def display_details(self):
        return f"Roll No: {self._roll_no}\nName: {self._name}\nAge: {self._age}"


class EngineeringStudent(Student):
    def __init__(self, roll_no, name, age, branch, cgpa):
        super().__init__(roll_no, name, age)
        self._branch = branch
        self._cgpa = cgpa
        
    def get_branch(self):
        return self._branch
        
    def get_cgpa(self):
        return self._cgpa
        
    def set_branch(self, branch):
        self._branch = branch
        
    def set_cgpa(self, cgpa):
        self._cgpa = cgpa
        
    def display_details(self):
        return f"{super().display_details()}\nBranch: {self._branch}\nCGPA: {self._cgpa}"


class MedicalStudent(Student):
    def __init__(self, roll_no, name, age, specialization, hospital):
        super().__init__(roll_no, name, age)
        self._specialization = specialization
        self._hospital = hospital
        
    def get_specialization(self):
        return self._specialization
        
    def get_hospital(self):
        return self._hospital
        
    def set_specialization(self, specialization):
        self._specialization = specialization
        
    def set_hospital(self, hospital):
        self._hospital = hospital
        
    def display_details(self):
        return f"{super().display_details()}\nSpecialization: {self._specialization}\nHospital: {self._hospital}"


class StudentManagement:
    def __init__(self):
        self.students = {}
        
    def add_student(self):
        print("\n1. Engineering Student\n2. Medical Student")
        choice = input("Enter choice: ")
        
        if choice in ['1', '2']:
            roll_no = input("Enter Roll No: ")
            if roll_no in self.students:
                print("Student already exists!")
                return
                
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            
            if choice == '1':
                branch = input("Enter Branch: ")
                cgpa = float(input("Enter CGPA: "))
                obj = EngineeringStudent(roll_no, name, age, branch, cgpa)
            else:
                specialization = input("Enter Specialization: ")
                hospital = input("Enter Hospital: ")
                obj = MedicalStudent(roll_no, name, age, specialization, hospital)
                
            self.students[roll_no] = obj
            print("Student added successfully!")
        else:
            print("Invalid Choice!")
            
    def view_all_students(self):
        if not self.students:
            print("No students found!")
            return
        for student in self.students.values():
            print(student.display_details())
            print("-" * 20)
            
    def search_student(self):
        roll_no = input("Enter Roll No to search: ")
        if roll_no in self.students:
            print(self.students[roll_no].display_details())
        else:
            print("Student not found!")
            
    def update_student(self):
        roll_no = input("Enter Roll No to update: ")
        if roll_no in self.students:
            student = self.students[roll_no]
            student.set_name(input("Enter New Name: "))
            student.set_age(int(input("Enter New Age: ")))
            
            if isinstance(student, EngineeringStudent):
                student.set_branch(input("Enter New Branch: "))
                student.set_cgpa(float(input("Enter New CGPA: ")))
            elif isinstance(student, MedicalStudent):
                student.set_specialization(input("Enter New Specialization: "))
                student.set_hospital(input("Enter New Hospital: "))
            print("Student updated successfully!")
        else:
            print("Student not found!")
            
    def delete_student(self):
        roll_no = input("Enter Roll No to delete: ")
        if roll_no in self.students:
            del self.students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found!")


def login():
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    
    if user_id == 'admin' and password == '123':
        obj = StudentManagement()
        while True:
            print("\n" + "="*10 + " MENU " + "="*10)
            print("1. Add Student\n2. View All Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
            choice = input("Enter choice: ")
            
            if choice == '1':
                obj.add_student()
            elif choice == '2':
                obj.view_all_students()
            elif choice == '3':
                obj.search_student()
            elif choice == '4':
                obj.update_student()
            elif choice == '5':
                obj.delete_student()
            elif choice == '6':
                print("Thank you... Bye!")
                break
            else:
                print("Invalid Choice!")
    else:
        print("Invalid ID or Password!")

login()