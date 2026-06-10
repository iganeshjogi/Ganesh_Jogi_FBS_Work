# 10. Write a program to check if entered year is a leap year or not.

def leapyearchk(n):
    if (n % 400 == 0)  or (n % 4 == 0 and n % 100 != 0):
        return True
    return False

n =  int(input('Enter the year: '))
res = leapyearchk(n)

if res:
    print(f'{n} is a leap year.')
else:
    print(f'{n} is not a leap year.')