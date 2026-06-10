# 3. Write a program to find sum of following series using functions :
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def powerSum(n):
    total_sum = 0
    for i in range (1,n+1):
        power = i ** i
        total_sum += power
    return total_sum

n = int(input('Enter the last number: '))

res = powerSum(n)

print(f'The total sum of series is {res}.')