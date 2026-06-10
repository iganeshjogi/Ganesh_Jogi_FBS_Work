# 3. Write a program to find sum of following series using functions :
# b. 1!+ 2! + 3! + 4!+..... + n!

def factorial_series(n):
    total_fact = 0
    for i in range (1, n+1):
        fact = 1
        for j in range (1 , i +1):
            fact *= j
        total_fact += fact
    return total_fact

n = int(input('Enter the last number: '))

factsum = factorial_series(n)

print(f'The sum of series of fatorials from 1 to {n} is {factsum}.')