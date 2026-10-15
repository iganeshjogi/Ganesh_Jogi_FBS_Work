from datastore import Datastore
from employee import Employee

class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while ch != '6':
            print('''Please select option:
            1. Add emp
            2. Upd emp
            3. Del emp
            4. Search emp
            5. Show all emp
            6. Logout
            ''')
            
            ch = input('Enter choice:')
            if(ch == '1'):
                res = self.addEmp()
                print(res)
            elif(ch == '2'):
                res = self.updEmp()
                print(res)
            elif(ch == '3'):
                id = input('Enter ID:') 
                res = self.delEmp(id)              
            elif(ch == '4'):
                id = input('Enter ID:')
                res = self.searchEmp(id)
                print(res)
            elif(ch == '5'):
                res = self.showAllEmp()
                print(res)
            elif(ch == '6'):
                print('Logged out...')
            else:
                print('Invalid choice...')


    def addEmp(self):
        id = input('Enter ID:')
        name = input('Enter NAME:')
        sal = float(input('Enter SALARY:'))
        dept = input('Enter DEPARTMENT:')

        emp = Employee(id, name, sal, dept)
        res = self.ds.addData(emp, 'employee')
        return res

    def showAllEmp(self):
        res = self.ds.showAllData('employee')
        return res
    
    def searchEmp(self, id):
        res = self.ds.getData(id, 'employee')
        return res

    def updEmp(self):
        id = input('Enter ID:')
        res = self.searchEmp(id)
        if(res):
            print('NOTE: Leave field blank if do not want to change...')
            name = input(f'Enter NAME({res[1]}):') or res[1]
            sal = float(input(f'Enter SAL({res[2]}):')) or res[2]
            dept = input(f'Enter DEPT({res[3]}):') or res[3]
            emp = Employee(id, name, sal, dept)
            res = self.ds.updData(emp, 'employee')
            return res
        else:
            return 'ID not exist.'
        
    def delEmp(self,id):
        res = self.ds.delData(id, 'employee')
        return res
    
if(__name__ == '__main__'):
    Admin()