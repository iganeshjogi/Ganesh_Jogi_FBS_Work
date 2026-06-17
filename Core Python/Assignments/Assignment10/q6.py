# 6. Write a program to remove duplicates from the list.

li = [10, 20, 30, 40, 10, 20, 50]
def listDuplicateRemove(li):
    new_li = []
    for i in range (len(li)):
        if li[i] not in(new_li):
            new_li.append(li[i])
    return(new_li)

res = listDuplicateRemove(li)
print(res)