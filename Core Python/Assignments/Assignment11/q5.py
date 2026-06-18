# 5. Python Program to Sort a List According to the Length of the Elements within the list.

li = ["apple", "kiwi", "banana", "cat", "elephant"]

def sortlistnyElementLength(li):
    for i in range(len(li)-1):
        for j in range(len(li) - 1 - i):
            if len(li[j]) > len((li[j+1])):
                li[j],li[j+1] = li[j+1],li[j]
    return li

print(sortlistnyElementLength(li))