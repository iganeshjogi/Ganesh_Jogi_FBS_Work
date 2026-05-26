#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input('Enter the three digit number: '))
d1 = num // 100
d2 = num // 10
d2 = d2 % 10
d3 = num % 10

if (d1,d2,d3) == (d3,d2,d1):
    print('Number is palindrome.')

else:
    print('Number is not palindrome.')