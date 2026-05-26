#9. WAP to print all numbers in a range divisible by a given number.

n = int(input('Enter the range: '))
d = int(input('Enter the divisor: '))

i = 1

while i <= n:
    if i % d == 0:
        print(i, end = ', ')
    i += 1