# 5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [70, 10, 80, 40, 30, 10]

key = int(input('Enter the Element to find: '))

def searchListElement(li,key):
    total = 0
    for i in range(len(li)):
        if li[i] == key:
            total += 1

    if total > 0:
        print(f'Element is present and Count is {total}')
    else:
        print('Element not found')
    

searchListElement(li,key)