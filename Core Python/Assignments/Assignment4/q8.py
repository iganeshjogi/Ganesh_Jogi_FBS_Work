#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n = int(input('Enter the number: '))

i = 1
while i <= n:
    if i % 7 == 0 and i % 5 == 0:
        print(i, end = ', ')
    i += 1