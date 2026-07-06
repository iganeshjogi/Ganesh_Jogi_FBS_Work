def selctionsort(li):
    len(li)
    for i in range(0, len(li) - 1):
        min_ind = i
        for j in range (i + 1, len(li)):
            if (li[j] < li[min_ind]):
                min_ind = j
        li[i], li[min_ind] = li[min_ind], li[i]
        print(li)

li = [60, 50, 40, 30, 20, 10]
print(li)
selctionsort(li)

print('After sorting', li)