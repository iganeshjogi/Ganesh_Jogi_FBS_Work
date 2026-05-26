n = int(input('Enter the number: '))

temp = n
total_sum = 0
while n > 0:
    d = n % 10

    i = 1
    fact = 1
    while i <= d:
        fact = fact * i
        i += 1
    
    total_sum += fact 
    n= n // 10

if total_sum == temp:
    print(f'The {temp} is a strong number.')
else:
    print(f'The {temp} is not a strong number.')