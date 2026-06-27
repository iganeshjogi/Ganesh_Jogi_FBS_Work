# #1. Print numbers from 1 to n

# n = int(input('Enter the number: '))

# i = 1
# while i <= n:
#     print(i)
#     i += 1

# #2. Print numbers from n to 1

# n = int(input('Enter the number: '))

# i = n
# while i >= 1:
#     print(i)
#     i -= 1

# #3. Print even numbers from 1 to n

# n = int(input('Enter the number: '))

# i = 2
# while i <= n:
#     print(i)
#     i += 2

# #4. Print odd numbers from 1 to n

# n = int(input('Enter the number: '))
# i = 1
# while i <= n:
#     print(i)
#     i += 2

# # 5. Find sum of numbers from 1 to n
# n = int(input('Enter the number: '))

# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
# print(sum)

# # 6. Find multiplication table of a number

# n = int(input('Enter the number: '))
# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1

# # 7. Find factorial of a number
# n = int(input('Enter the number: '))

# i = 1
# fact = 1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(fact)

# # 8. Find square of numbers from 1 to n

# n = int(input('Enter the number: '))

# i = 1
# while i <= n:
#     print(i**2)
#     i += 1

# # 9. Find cube of numbers from 1 to n

# n = int(input('Enter the number: '))

# i = 1
# while i <= n:
#     print(i**3)
#     i += 1

# 10. Count digits in a number

n = int(input('Enter the number: '))

count = 0
while n > 0:
    n = n //10
    count += 1
print(count)

# # 11. Reverse a number

# n = int(input('Enter the number: '))

# rev = 0

# while n > 0:
#     d = n % 10
#     rev = rev * 10 + d
#     n = n // 10
# print(rev)

# # 12. Check palindrome number

# n = int(input('Enter number:'))
# temp = n
# rev = 0

# while n > 0:
#     d = n % 10
#     rev = rev * 10 + d
#     n //= 10   
# if rev == temp:
#     print('The number is palindrome.')
# else:
#     print('The number is not palindrome.')

# # 13. Find sum of digits

# n = int(input('Enter the number: '))
# sum = 0
# while n > 0:
#     d = n % 10
#     sum = sum + d
#     n = n // 10
# print(sum)

# # 14. Find product of digits

# n = int(input('Enter the number: '))

# product = 1
# while n > 0:
#     d = n % 10
#     product = d * product
#     n //= 10
# print(product)

# # 15. Check Armstrong number
# n = int(input('Enter the number:'))
# temp = n
# sum = 0
# while n > 0:
#     d = n % 10
#     sum = sum + d**3
#     n //= 10
# if sum == temp:
#     print('The number is armstrong.')
# else:
#     print('The number is not armstrong.')

## 16. Check prime number

# n = int(input('Enter the number: '))

# i = 2
# prime = 1

# while i < n:

#     if n % i == 0:
#         prime = 0

#     i += 1

# if prime == 1:
#     print('Prime number')

# else:
#     print('Not prime number')

# # 17. Print prime numbers from 1 to n
# n = int(input('Enter the number: '))
# num = 2
# while num <= n:

#     i = 2
#     prime = 1

#     while i < num:

#         if num % i == 0:
#             prime = 0

#         i += 1

#     if prime == 1:
#         print(num)

#     num += 1