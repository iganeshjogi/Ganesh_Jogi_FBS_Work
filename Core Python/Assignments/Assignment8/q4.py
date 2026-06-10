# 4. Sum of all odd numbers between 1 to n

def sumodds(n):
    sum = 0
    for i in range (1, n+1):
        if i % 2 != 0:
            sum += i
    return sum

n = int(input('Enter the last number: '))

res = sumodds(n)

print(f'The sum of all odd numbers til {n} is {res}.')