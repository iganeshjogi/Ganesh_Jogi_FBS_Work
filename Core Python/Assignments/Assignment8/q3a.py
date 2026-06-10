# 3. Write a program to find sum of following series using functions :

# a. 1+ 2 + 3 + 4+..... + n

def series_sum (n):
    sum = 0
    for i in range (1,n+1):
        sum += i
    return sum
    
    
n = int(input('Enter the last number for series: '))

sumseries = series_sum(n)

print(f'The sum of series till {n} is {sumseries}.')

