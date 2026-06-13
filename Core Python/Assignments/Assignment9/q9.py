# 9. Write a program to calculate the m to the power n using recursion.

def basepower(m, n):
    if n == 0:
        return 1
    return m * basepower(m,n-1)

m = int(input('Enter the number: '))
n = int(input('Enter the power: '))

print(basepower(m,n))