def checkprime(n):
    if n > 1:
        for i in range(2, n // 2 + 1 ):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False
    
data = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(checkprime,data))
print(res)