# 4. Write a program to reverse the list.

li = [70, 10, 80, 40, 30]

# Method 1

def revlist(li):
    size = len(li)
    rev = []
    for i in range(size-1,-1,-1):
        rev.append(li[i])
    return rev

print('Method 1:',revlist(li))

# Method 2

def reverselist(li):
    start = 0
    end = len(li) - 1
    while start < end:
        li[start], li[end] = li[end], li[start]
        start += 1
        end -= 1
    return (li)

print('Method 2:',reverselist(li))