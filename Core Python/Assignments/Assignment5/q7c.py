# Write a program to solve the following series :
# Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input('Enter the number: '))
sum = 0
for i in range (0,n):
    g = 2 ** i
    sum += g
print(sum)