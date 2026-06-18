# 7. Python Program to Find the Intersection of Two Lists.

li1 = [10,20,30,40]
li2 = [30,40,50,60]

def listIntersections(li1, li2):
    newli = []
    for i in range(len(li1)):
        if li1[i] in li2:
            newli.append(li1[i])
        
    return newli

res = listIntersections(li1,li2)

print(f'Intersections of Two Lists: {res}')