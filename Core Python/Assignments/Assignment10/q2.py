# 2. Write a program to find maximum and minimum element in a list.

# For Minimum Element

def minimumOfList (li):
    size = len(li)
    mini = li[0]
    for i in range(size):
        if li[i] < mini:
            mini = li[i]
    return mini

li = [70,10,80,40,30]

print('Minimum Number:',minimumOfList(li))

# For Maximum Element

def maximumOfList(li):
    size = len(li)
    maxi = li[0]
    for i in range(size):
        if li[i] > maxi:
            maxi = li[i]
    return maxi

li = [70,10,80,40,30]

print('Maximum Number:',maximumOfList(li))