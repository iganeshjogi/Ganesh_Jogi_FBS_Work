# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

def listDuplicate(li):
    new_li = []
    for i in li:
        new_li.append(i)
    return new_li

li = [10, 20, 30, 40, 50]

res = listDuplicate(li)
print(res)