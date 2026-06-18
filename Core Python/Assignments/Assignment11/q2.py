# 2. Python Program to Merge Two Lists and Sort it

li1 = [80, 20, 10]
li2 = [70, 40, 60]

def Mergetwolists(li1,li2):
    li = []
    for i in li1:
        li.append(i)
    for j in li2:
        li.append(j)

    return li

li = Mergetwolists(li1, li2)
print(f'Merged list: {li}')

def bubblesortlist(li):
    for i in range(len(li) - 1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

print(f'Sorted list: {bubblesortlist(li)}')