# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.

def secondlargeEleOfList(li):
    size = len(li)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li[-2]

li = [ 50, 20, 90, 40, 10, 30, 100]
res = (secondlargeEleOfList(li))
print(f'The Second Largest element of a list is {res}.')