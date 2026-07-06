li = [ 52, 48, 26, 89, 24, 98 ]

print(f'Before swapping: {li}')
n = len(li)

for i in range(n):
    for j in range(n-i-1):
        if li[j] > li[j+1]:
            #swap
            li[j],li[j+1] = li[j+1],li[j]

    print(li) # to see Operration
    
print(f'After swapping: {li}')