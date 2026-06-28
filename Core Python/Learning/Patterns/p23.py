'''

        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

'''


for i in range(1,6):
    k = 1
    for j in range(1,6 - i):
        print(' ',end= ' ')
    
    for j in range(1,i+1):
        print(j,end= ' ')
        k += 1

    k -= 2
    for j in range(1,i):
        print(k,end=' ')
        k -= 1

    print()
