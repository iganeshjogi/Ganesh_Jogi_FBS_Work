'''
    5 4 3 2 1 
    4     1 
    3   1 
    2 1 
    1 
'''

for i in range(1,6):
    for j in range(6 - i,0,-1):
        if i == 1 or j == 1 or j + i ==6:
            print(j,end=' ')
        else:
            print(' ',end =' ')
    print()