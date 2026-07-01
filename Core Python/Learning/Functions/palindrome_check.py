def palindrome(n):
    if n > 0:
        temp = n
        rev = 0
        while temp > 0:
            d = temp % 10
            rev = (rev*10) + d
            temp = temp // 10
        if rev == n:
            return True
        else:
            return False
    else:
        return False
    
n = int(input('Enter Number: '))
res = palindrome(n)
print(res)