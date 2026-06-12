# Q. print following pattern:
'''
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 
  
'''
for i in range(1,6):
    for s in range(6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(i-1,0,-1):
        print(k,end=' ')
    print()