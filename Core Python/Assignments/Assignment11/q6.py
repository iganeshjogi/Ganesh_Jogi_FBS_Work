# 6. Python Program to Find the Union of two Lists

li1 = [10,20,30,40]
li2 = [30,40,50,60]

def unionofLists(li1,li2):
    newli = []
    for i in range(len(li1)):
        newli.append(li1[i])
    for j in range(len(li2)):
        if li2[j] not in newli:
            newli.append(li2[j])
    return newli

res = unionofLists(li1,li2)
print(f'Union list: {res}')