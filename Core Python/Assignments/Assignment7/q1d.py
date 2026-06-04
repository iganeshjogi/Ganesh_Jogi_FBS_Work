for i in range(1,6):
    for s in range(1,6-i):
        print(' ',end=' ')
    for j in range(i,2*i):
        print(j,end=' ')
    for k in range(2*i-2,i-1,-1):
        print(k,end=' ')
    print()