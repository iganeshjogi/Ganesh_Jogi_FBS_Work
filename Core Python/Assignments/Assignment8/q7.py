# 7. Write a program to find sum of digits of a number.

def numberDigitSum(n):
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        total += d
        temp //= 10
    return total

n = int(input('Enter the number: '))

res = numberDigitSum(n)
print(f'The sum of digits of a number {n} is {res}')
