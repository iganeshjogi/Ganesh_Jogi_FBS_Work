#12. Write a program to check if given number is Armstrong number or not.

n  = int(input('Enter the number: '))
power = len(str(n))
temp = n
total = 0
while n > 0:
    d = n % 10
    d_power = d ** power
    total += d_power
    n = n // 10

if temp == total:
    print(f'{temp} is a armstrong number.')
else:
    print(f'{temp} is not a armstrong number.')
