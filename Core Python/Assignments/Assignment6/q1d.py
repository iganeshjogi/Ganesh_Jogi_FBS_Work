# Q. print following pattern:
'''
A 
A B 
A B C 
A B C D 
A B C D E 

'''

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()