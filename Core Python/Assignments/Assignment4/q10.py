#10. WAP to check if given number is Perfect Number.
n = int(input('Enter the number: '))

i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum = sum + i
    i+=1

if n == sum:
    print(f'{n} is a perfect number.')
else:
    print(f'{n} is not a perfect number.') 