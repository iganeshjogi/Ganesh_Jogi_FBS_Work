for i in range(1,6):
    for s in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:
            print(j,' ',end=' ')
        else:
            print('   ',end=' ')
    print()