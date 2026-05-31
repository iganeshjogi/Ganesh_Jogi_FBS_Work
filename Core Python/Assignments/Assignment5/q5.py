#5. Write a program to print prime numbers between 1 to 100.

for i in range(2,100):
    prime = 1
    for j in range(2,i):
        if i % j == 0:
            prime = 0
        
    if prime == 1:   
        print(i,end=' ')