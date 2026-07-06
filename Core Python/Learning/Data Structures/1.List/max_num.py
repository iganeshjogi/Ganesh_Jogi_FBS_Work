li =  [70, 200, 80, 100 ,40, 90,]

max = li[0]

for i in range (0, len(li)):
    if li[i] > max:
        max = (li[i])

print(f'Maximum number: {max}')