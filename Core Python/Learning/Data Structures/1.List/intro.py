#1. structure: []
li = [10, 20, 30, 40]

#2. Type of data : Hetrogeneous
# li = [10, 3.14, 'Ganesh']

#3. sequence: Ordered

#4. changable: Mutable
print(id(li))
li.append(50)
print(li)
print(id(li))

#5. Duplication allowed
# li = [10, 20, 20, 30]
# print(li)

#6. Default sorting: Not sorted
# li = [50,40,10,80]
# print(li)