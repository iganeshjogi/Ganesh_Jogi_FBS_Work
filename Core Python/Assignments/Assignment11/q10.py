# 10. Write a program to print list after removing even numbers.

def removeEvensFromlist(li):
    new_li = []
    for i in li:
        if i % 2 != 0:
            new_li.append(i)
    return new_li

li = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(removeEvensFromlist(li))