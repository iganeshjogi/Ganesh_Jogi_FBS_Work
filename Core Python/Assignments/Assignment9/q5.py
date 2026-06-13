# 5. Write a program to find factorial using recursion.

def factorialchk(n):
    if n == 0 or n == 1:
        return 1
    return n * factorialchk(n-1)

n = int(input('Enter the number: '))

print(f'The Factorial of {n} is {factorialchk(n)}.')