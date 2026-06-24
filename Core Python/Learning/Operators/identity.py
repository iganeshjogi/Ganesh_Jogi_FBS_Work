x = 10 #Immutable
y = 10
z = 20 
li = [10, 20] #Mutable
li2 = [10, 20]

#1. is

print(x is y)
print(x is z)
print(li is li2)

print(id(x))
print(id(y))
print(id(li))
print(id(li2))

#2. is not
print(li is not li2)