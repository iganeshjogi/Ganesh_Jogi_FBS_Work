li = [1, 10, 18, 45, 69]
start = 0
stop = len(li)-1
targate = int(input('Enter the number you want to search: '))
while start <= stop:
    mid = (start + stop) // 2
    if li[mid] == targate:
        print(f'{targate} is found')
        break
    elif li[mid] < targate:
        start = mid + 1
    elif li[mid] > targate:
        stop = mid - 1
else:
    print(f'{targate} is not found')