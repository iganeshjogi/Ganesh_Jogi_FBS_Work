# 1. Write a program to find sum of all elements of list:

def sumOfListElements (li):
    size = len(li)
    total = 0
    for i in range (size):
        total += li[i]
    return total

li = [10,20,30,40,50,]

print(sumOfListElements(li))