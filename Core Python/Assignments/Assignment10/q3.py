# 3. Write a program to find the second largest element in the list.

def secMaxNumberOfList(li):
    maxi = li[0]
    smax = li[0]
    for i in range(len(li)):
        if li[i] > maxi:
            smax = maxi
            maxi = li[i]
        
        elif li[i] > smax:
            smax = li[i]
    
    print(f'The maximum number:{maxi} \nThe Second maximum number:{smax}')

li = [70,10,80,40,30]
secMaxNumberOfList(li)