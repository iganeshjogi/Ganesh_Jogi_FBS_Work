# 3. Write a program to reverse a given number using recursive function.

def revNumber(n, digits):
    if n == 0:
        return 0
    return (n % 10) * (10 ** (digits - 1)) + revNumber(n//10, digits - 1)


n = int(input('Enter the Number: '))
digits = int(input('Enter the number of digits: '))

print(f'The reverse of a number {n} is {revNumber(n,digits)}.')