# Factorial checker

n = int(input('Enter the nuber: '))
fact = 1
i = 1
for i in range (1, n+1):
    fact = fact * i
    i += 1
print(f' The factorial of {n} is {fact}.')