# 4. Write a program to find sum of n numbers using recursion.

def sumofSeries(n):
    if n == 0:
        return 0
    return n + sumofSeries(n-1)

n = int(input('Enter the last number: '))

print(f'The sum of series of numbers from 1 to {n} is {sumofSeries(n)}.')