# 11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

#step 1. Digits count

def digitcount(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

n = int(input('Enter the number: '))
res = digitcount(n)

#step 2. Armstrong Number check

def armstrongchk(n):
    temp = n
    total = 0
    while n > 0:
        d = n % 10
        d = d ** res 
        total += d
        n //= 10
    return temp == total

res2 = armstrongchk(n) 

if res2:
    print('Armstrong Number.')
else:
    print('Not a Armstrong number.')