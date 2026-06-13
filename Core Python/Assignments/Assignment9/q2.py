# 2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrongchk(n, p):
    if n == 0:
        return 0
    return (n % 10) ** p + armstrongchk(n // 10,p)


n = int(input('Enter the number:'))
p = len(str(n))

if armstrongchk(n,p) == n:
    print(f'{n} is a Armstrong number.')
else:
    print(f'{n} is not a Armstrong number.')