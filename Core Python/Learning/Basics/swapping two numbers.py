x = 10
y = 50

print(x,y)

#1. By using third variable

temp = x 
x = y
y = temp

print(x,y)

#2. without using variable 

x = x + y
y = x - y
x = x - y
print(x,y)

#3. Moden method
x,y = y,x
print(x,y)