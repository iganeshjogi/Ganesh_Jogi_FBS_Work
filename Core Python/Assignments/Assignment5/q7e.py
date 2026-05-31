# Write a program to solve the following series:
# x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input('Enter the value of x: '))
n = int(input('Enter number of terms: '))

sum = 0

for i in range(1, n+1):

    den = 2 * i - 1

    term = (x * i) / den

    if i % 2 == 0:
        sum -= term
    else:
        sum += term

print(sum)