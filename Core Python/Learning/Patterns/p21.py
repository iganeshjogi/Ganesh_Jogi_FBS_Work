#         1 
#       1 2 3 
#     1 2 3 4 1 
#   1 2 3 4 5 1 1 
# 1 2 3 4 5 6 1 1 1 


for i in range(1,6):
    k = 1
    for j in range (1, 6- i):
        print(' ',end=' ')

    for j in range(1,i+1):
        print(j,end=' ')
        k += 1
    
    for j in range(1,i):
        print(k, end = ' ')
        k= 1
    print()