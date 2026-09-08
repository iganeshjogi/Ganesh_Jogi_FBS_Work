# Q. GCD (HCF) of Two Numbers

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

i = num1
while i > 0:
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break
    i = i - 1