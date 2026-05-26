#6. WAP to check if a given number is prime number or not.

n = int(input('Enter the number: '))

i = 2
prime = 1
while i < n:
    if n % i == 0:
        prime = 0
    i += 1

if prime == 1:
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
