# 11. Write a program to print all numbers which are divisible by m and n in the list.

def listElementDivisiblebymn(li,m,n):
    newli = []
    for i in li:
        if i % m == 0 and i % n == 0:
            newli.append(i)
    return newli


li = [10, 12, 15, 18, 20, 24, 30]
m = int(input('Enter m: '))
n = int(input('Enter n: '))

print(listElementDivisiblebymn(li,m,n))