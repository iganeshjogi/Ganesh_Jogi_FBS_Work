# 8. Write a program find reverse of a number

def revnumber(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return rev

n = int(input('Enter the number: '))
res = revnumber(n)
print(f'The reveresed number of a {n} is {res}.')