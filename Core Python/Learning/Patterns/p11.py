# * $ * $ * 
# $ * $ * $ 
# * $ * $ * 
# $ * $ * $ 
# * $ * $ * 

# for i in range(1,6):
#     for j in range(1,6):
#         if(i % 2 != 0 and j % 2 != 0):
#             print('*', end = ' ')
#         else:
#             print('$', end = ' ')
#     print()

## Another method

for i in range(1,6):
    for j in range(1,6):
        if((i + j) % 2 ==0):
            print('*', end = ' ')
        else:
            print('$', end = ' ')
    print()