# 7. Write a program to find sum of digits using recursion.

def digitsum(n):
    if n == 0:
        return 0
    return (n % 10) + digitsum(n // 10)

n = int(input('Enter the number'))

print(f'The sum of digits of number {n} is {digitsum(n)}.')