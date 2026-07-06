def bubblesort(li):
    size = len(li)
    for i in range(1,size):
        for j in range (0,size - 1):
            if li[j] > li [j + 1]:
                li[j], li[j+1] = li[j+1], li[j]
            # print(li)

li = [50, 40, 30, 20, 10] 
print(li)
bubblesort(li)
 
print('After sorting', li)