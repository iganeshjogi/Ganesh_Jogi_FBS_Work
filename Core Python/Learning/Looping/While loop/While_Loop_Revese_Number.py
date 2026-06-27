# Palindrome checker

n = int(input('Enter the number:'))
temp = n
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
print (rev)

if temp == rev:
    print(f'The number {temp} is palindrome.')
else:
    print(f'The number {temp} is not palindrome.')