# 8. Write a program to check whether a number is prime or not using recursion.

def primechk(n,divisor):
    if n == divisor :
        return True
    if n % divisor == 0:
        return False
    return primechk(n,divisor + 1)

n = int(input('Enter the number: '))

if n > 1 and primechk(n, 2):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')