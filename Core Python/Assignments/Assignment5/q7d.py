# Write a program to solve the following series :
# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input('Enter the number: '))
sum = 0
for i in range (1,10+1,1):
    temp = (a * i)/i
    sum += temp
print(sum)