li = [10, 50, 80, 70, 60, 100]

max = li[0]
smax = 0

for i in range(1,len(li)):
    if (li[i] > max ):
        smax = max
        max = li [i]
    
    elif (li[i] > smax):
        smax = li[i]

print('Maximum',max)
print('Second Maximum',smax)