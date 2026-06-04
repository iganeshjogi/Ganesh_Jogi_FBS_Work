for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    for s in range(1,10-2*i):
        print(' ',end=' ')
    for k in range(i,0,-1):
        if k != 5 or i !=5:
            print(k,end=' ')
    print()