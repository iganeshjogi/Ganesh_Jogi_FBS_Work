# Prime numbers between 1 to n:

n = int(input('Enter the number: '))

for num in range (1, n):
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print (num, end = ' ')