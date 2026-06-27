# # 1. Print numbers from 1 to 10
# for i in range(1,11,1):
#     print(i, end = ', ')

# # 2. Print numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i, end = ', ' )

# # 3. Print even numbers from 1 to n
# n = int(input('Enter the number: '))
# for i in range(2,n+1,2):
#     print(i, end = ', ')

## 4. Print odd numbers from 1 to n
# n = int(input('Enter the number: '))
# for i in range(1,n+1,2):
#     print(i, end = ', ')

##5. Print multiplication table of a number
# n = int(input('Enter thr number: '))
# for i in range(n, n*10+1,n):
#     print(i)
# another method(Traditional)
# n = int(input('Enter thr number: '))
# for i in range(1,11):
#     print(n, 'x', i, '=', i*n)

# # 6. Find sum from 1 to n
# n = int(input('Enter thr number: '))
# sum = 0
# for i in range (1,n+1,1):
#     sum = sum + i
# print(sum)

# # # 7. Find factorial of a number
# n = int(input('Enter the number: '))
# fact = 1
# for i in range(1,n+1,1):
#     fact = fact*i
# print(fact)

# #8. Find sum of even numbers from 1 to n
# n = int(input('Enter the number: '))
# sum = 0
# for i in range (2,n+1,2):
#     sum = sum + i
# print(sum)

# # 9. Find sum of odd numbers from 1 to n
# n = int(input('Enter the number: '))
# sum = 0
# for i in range(1,n+1,2):
#     sum += i
# print(sum)

# 10. Count digits in a number
# n = int(input('Enter the number: '))
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)
# we can't done this by for loop

# #11. Check prime number
# n = int(input('Enter the number: '))
# prime = 0
# for i in range(2,n,1):
#     if n % i == 0:
#         prime = 1

# if prime == 1:
#     print('Not prime')
# else:
#     print('Prime')

# #12. Print prime numbers from 1 to n
# n = int(input('Enter the number: '))
# for i in range(2,n+1):
#     prime = 1
#     for j in range(2,i):
#         if i % j == 0:
#             prime = 0
        
#     if prime == 1:
#         print(i, end = ' ')

# #13. Print numbers from 1 to 20 but skip 5 using 'continue'
# for i in range(1,21,1):
#     if i == 5:
#         continue
#     print(i, end= ' ')

# #14. Print numbers from 1 to 20 and stop at 10 using `break`
# for i in range (1,21,1):
#     if i == 10:
#         break
#     print(i, end= ', ')

# #15. Print Fibonacci series upto n terms
# n = int(input('Enter the number: '))
# a = -1
# b = 1 
# for i in range (1,n+1,1):
#     c = a + b
#     a = b
#     b = c
#     print(c,end= ', ')