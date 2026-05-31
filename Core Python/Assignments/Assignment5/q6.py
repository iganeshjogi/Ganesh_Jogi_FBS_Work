#6. Write a program to print first n prime numbers.

n = int(input('Enter the number:'))
for i in range(2,n+1):
    prime = 1
    for j in range(2,i):
        if i % j == 0:
            prime = 0   
    if prime == 1:
        print(i,end=' ')