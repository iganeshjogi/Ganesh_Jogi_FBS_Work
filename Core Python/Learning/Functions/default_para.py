### Default Parameters / Arguments
#1. To make parameter optional
#2. Assigning value to the parameter in function
#3. If we don't pass the value to the parameter in function call, It will take default value.
    # If we pass the value to the parameter in function call, It will take passed value.
#4.Flow of making default is from right to left.

def empl(id,name,salary,dept='IT'):
    data = (f'ID: {id}\nName: {name}\nSalary: {salary}\nDept: {dept}')
    return data

res = empl(101,'Ganesh', 50000,'Data Analyst')
print(res)