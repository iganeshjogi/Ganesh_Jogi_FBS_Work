# Q. print following pattern:
'''

* * * * * 
*       * 
*       * 
*       * 
*       * 
* * * * * 

'''

for i in range(1,7):
    for j in range(1,6):
        if i == 1 or i == 6 or j == 1 or j == 5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()