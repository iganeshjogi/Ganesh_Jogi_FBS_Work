# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!

def factorial(x):
    if x == 1 or x == 0:
        return 1 
    return x * factorial(x-1)
def factorialSeriesSum(n):

    if factorial(n) == 1:
        return 1
    return factorial(n) + factorialSeriesSum(n-1)


n = int(input('Enter the number of last number of series: '))

print(f'The sum of series of factorials from 1 to {n} is {factorialSeriesSum(n)}.')