# Q. print following pattern:

'''
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I 

'''
for i in range(1,6):
    for s in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,2*i):
        print(chr(64 + j),end=' ')
    print()