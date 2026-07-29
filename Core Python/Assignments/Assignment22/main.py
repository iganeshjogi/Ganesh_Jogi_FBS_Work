import pickle
from emp import Emp
import os


def addRecord():
    eid = int(input('Enter ID: '))
    name = input('Enter NAME: ')
    basic = float(input('Enter BASIC: '))

    emp = Emp(eid, name, basic)

    with open('Core Python/Assignments/Assignment22/EmpData.txt', 'ab') as fp:
        pickle.dump(emp, fp, protocol=pickle.HIGHEST_PROTOCOL)

    print('Employee Added Successfully!')

def displayRecords():
    try:
        with open('Core Python/Assignments/Assignment22/EmpData.txt', 'rb') as fp:
            while True:
                try:
                    records = pickle.load(fp)
                    print(records)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File Not Found!')

def searchRecord():
    searchID = int(input('Enter ID: '))
    found = False
    with open('Core Python/Assignments/Assignment22/EmpData.txt', 'rb') as fp:
        while True:
            try:
                emp = pickle.load(fp)
                if searchID == emp.eid:
                    found = True
                    print(emp)
                    break
            except EOFError:
                break
    if found == False:
        print('ID NOT EXIST!')

def editRecord():
    searchID = int(input('Enter ID: '))
    found = False
    with open('Core Python/Assignments/Assignment22/EmpData.txt', 'rb') as fp,\
        open('Core Python/Assignments/Assignment22/TempData.txt', 'wb') as temp:

        while True:
            try:
                emp = pickle.load(fp)
                if searchID == emp.eid:
                    found = True

                    print("\nEnter New Details")

                    nid = int(input('Enter new ID: '))
                    nName = input('Enter new NAME: ')
                    nBasic = float(input('Enter new BASIC: '))

                    nemp = Emp(nid, nName, nBasic)
                    pickle.dump(nemp, temp, protocol=pickle.HIGHEST_PROTOCOL)

                else:
                    pickle.dump(emp, temp)

            except EOFError:
                break

    if found:
        os.remove("Core Python/Assignments/Assignment22/EmpData.txt")
        os.rename(
            "Core Python/Assignments/Assignment22/TempData.txt",
            "Core Python/Assignments/Assignment22/EmpData.txt"
        )
        print("Record Updated Successfully!")
    else:
        os.remove("Core Python/Assignments/Assignment22/TempData.txt")
        print("ID NOT FOUND!")


def deleteRecord():
    searchID = int(input('Enter ID: '))
    found = False
    with open('Core Python/Assignments/Assignment22/EmpData.txt', 'rb') as fp,\
        open('Core Python/Assignments/Assignment22/TempData.txt', 'wb') as temp:

        while True:
            try:
                emp = pickle.load(fp)
                if searchID == emp.eid:
                    found = True

                else:
                    pickle.dump(emp, temp)

            except EOFError:
                break

    if found:
        os.remove("Core Python/Assignments/Assignment22/EmpData.txt")
        os.rename(
            "Core Python/Assignments/Assignment22/TempData.txt",
            "Core Python/Assignments/Assignment22/EmpData.txt"
        )
        print("Record Deleted Successfully!")
    else:
        os.remove("Core Python/Assignments/Assignment22/TempData.txt")
        print("ID NOT FOUND!")


while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Record")
    print("2. Display All Records")
    print("3. Search Record")
    print("4. Edit Record")
    print("5. Delete Record")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        addRecord()

    elif choice == 2:
        displayRecords()

    elif choice == 3:
        searchRecord()

    elif choice == 4:
        editRecord()

    elif choice == 5:
        deleteRecord()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")