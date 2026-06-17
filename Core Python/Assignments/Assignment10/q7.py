# 7. Write a program to create a new list from existing list which contains cube of each number of list.

def listElementsCube (li):
    new_li = []
    for i in li:
        new_li.append(i**3)
    return new_li

li = [1, 2, 3, 4, 5]

res = listElementsCube(li)
print(res)
