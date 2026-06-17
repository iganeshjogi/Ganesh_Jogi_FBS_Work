# 10. Write a program to remove all occurrences of a given element in the list.

def RemoveListOccurences(li):
    li1 = []
    for i in li:
        if i != key:
            li1.append(i)
    return li1

li = [ 10, 20, 30, 20, 40, 20, 50]
key = int(input('Enter the element to remove all occurrences from the list: '))
print(RemoveListOccurences(li))