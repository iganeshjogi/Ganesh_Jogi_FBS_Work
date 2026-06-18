# 3. Python Program to Sort the List According to the Second Element in Sublist.

li = [ [15, 8], [22, 3], [10, 12], [35, 1], [18, 6] ]

size = len(li)
for i in range(size-1):
    for j in range(size-1-i):
        if li[j][1] > li[j+1][1]:
            li[j],li[j+1] = li[j+1],li[j]
print(li)