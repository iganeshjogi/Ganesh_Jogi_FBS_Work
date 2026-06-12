# Q. print following pattern:
'''
        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 
'''

for i in range(1,6):
    for s in range(1,6-i):
        print(' ',end=' ')
    
    for j in range(1,2*i):
        if j == 1 or j== 2*i - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

for i in range(1,5):
    for s in range(1,i+1):
        print(' ',end=' ')
    
    for j in range(1,10-2*i):
        if j==1 or j == 10-2*i -1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()