# 1. Python Program to Put Even and Odd elements of a List into two Different Lists.

li = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ListEvenOddElementSeparator(li):
    Even_list = []
    odd_list = []
    for i in li:
        if i % 2 == 0:
            Even_list.append(i)
        else:
            odd_list.append(i)
    return(f'Even elements list: {Even_list}\nOdd elements list: {odd_list}')

print(ListEvenOddElementSeparator(li))