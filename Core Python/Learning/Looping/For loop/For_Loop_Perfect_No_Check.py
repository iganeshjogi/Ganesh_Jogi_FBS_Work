# perfect number checker

n = int(input('Enter the number: '))

temp = 0

for i in range (1, n):
    if  n % i == 0:
        temp += i

if n == temp:
    print(f'{n} is a perfect number.')
else:
    print(f'{n} is a not a perfect number.')