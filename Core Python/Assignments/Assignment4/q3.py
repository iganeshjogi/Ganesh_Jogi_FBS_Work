#3. WAP to print sum of series upto n.

n = int(input('Enter the number: '))

i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(f'The sum of series from 1 to {n} is {sum}.')