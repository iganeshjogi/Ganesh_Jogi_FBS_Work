# 9. Write a program to check if entered number is a palindrome or not.

def palindromeChk(n):
    temp = n
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return temp == rev

n = int(input('Enter the number: '))
res = palindromeChk(n)

if res:
    print('Palindrome Number.')
else:
    print('Not palindrome Number.')