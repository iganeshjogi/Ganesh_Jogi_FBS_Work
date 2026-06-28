# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range (5,0,-1):
#     for j in range (i):
#         print('*',end = ' ')
#     print()

## without changing value of i range

for i in range(1,6):
    for j in range(1, 7 - i):
        print('*', end = ' ')
    print()

