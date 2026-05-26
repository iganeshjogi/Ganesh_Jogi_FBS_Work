#4. WAP to print factorial of a number.

n = int(input('Enter the number: '))

i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1
print(f'The factorial of a number {n} is {fact}.')