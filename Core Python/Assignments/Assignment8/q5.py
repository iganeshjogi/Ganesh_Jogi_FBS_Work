# 5. Sum of all prime numbers between 1 to n

def sumprimes(n):
    total = 0
    for i in range(2, n+1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            total += i
    return total

n = int(input('Enter the last number: '))

res = sumprimes(n)

print(f'The total sum of all prime numbers til {n} is {res}.')