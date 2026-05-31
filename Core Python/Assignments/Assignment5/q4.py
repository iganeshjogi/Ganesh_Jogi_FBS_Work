#4. WAP to print Armstrong number within a given range

start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))
for num in range(start,end+1):

    temp = num
    sum = 0
    power = len(str(num))

    while temp > 0:
        d = temp % 10
        sum += d**power
        temp //= 10

    if sum == num:
        print(num)