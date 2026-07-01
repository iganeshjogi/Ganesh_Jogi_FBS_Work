### keyword para
# 1. To neglect positional argument
# 2. Assigning value to parameter in function call
# 3. flow from right to left
# 4. keyword name should be same as in function defination

def emp(id,name,salary,dept='IT'):
    data = (f'ID:{id}\nName:{name}\nsalary:{salary}\ndept:{dept}')
    return data

# res = emp(101,'Ganesh',50000,'IT')
res = emp(salary=40000,id=101,dept='IT',name="Ganesh")
print(res)