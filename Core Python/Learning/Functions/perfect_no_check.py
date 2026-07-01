# n = int(input('Enter the number:'))
# sum = 0
# for i in range (1,n):
#     if n % i == 0:
#         sum += i
    
# if sum == n:
#     print('Perfect number')
# else:
#     print('Not a Perfect Number')

def checkPerfectNo (n):
    sum = 0
    for i in range(1,n):
        if n % i ==0:
            sum += i
    if sum == n:
        return True
    else:
        return False
    
n = int(input('Enter the number:'))
res = checkPerfectNo(n)
print(res)