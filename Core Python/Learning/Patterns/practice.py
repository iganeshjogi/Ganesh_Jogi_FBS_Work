## Category 1: Basic Rectangle Patterns

# *
# *
# *
# *
# *
# for i in range (1,6):
#     print('*',end=' ')
#     print()


# * * * * *
# for i in range(1,6):
#     print('*',end= ' ')


# * * * *
# * * * * 
# * * * *
# * * * * 
# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end=' ')
#     print()


# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# for i in range(1,4):
#     for j in range(1,6):
#         print('1',end=' ')
#     print()


# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# for i in range(1,4):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()


# A B C D E
# A B C D E
# A B C D E
# for i in range (1,4):
#     for j in range(1,6):
#         print(chr(64 + j),end = ' ')
#     print()

## Category 2: Increasing Patterns

# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end= ' ')
#     print()


# A
# A B
# A B C
# A B C D
# A B C D E
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=' ')
#     print()


# A
# B B
# C C C
# D D D D
# E E E E E
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(chr(64 + i),end= ' ')
#     print()


## Category 3: Continuous Patterns

# 1 2 3
# 4 5 6
# 7 8 9
# num = 1
# for i in range(1,4):
#     for j in range(1,4):
#         print(num ,end=' ')
#         num += 1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=' ')
#         num+=1
#     print()

 
# A
# B C
# D E F
# G H I J
# num = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(64+num),end=' ')
#         num+=1
#     print()

## Category 4: Decreasing Patterns

# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,6):
#     for j in range(1,7-i):
#         print('*',end=' ')
#     print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end=' ')
#     print()

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(6-i,end=' ')
#     print()

# E E E E E
# D D D D
# C C C
# B B
# A
# for i in  range(1,6):
#     for j in range(1,7-i):
#         print(chr(70-i),end=' ')
#     print()

## Category 4.5 – Continuous Decreasing Patterns\
# 1 2 3 4 5
# 6 7 8 9
# 10 11 12
# 13 14
# 15
# num = 1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(num,end=' ')
#         num+=1
#     print()


# A B C D E
# F G H I
# J K L
# M N
# O
# num=1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(chr(64 + num),end=' ')
#         num+=1
#     print()


## Category 5: Hollow Patterns

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print('1',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# A A A A A
# A       A
# A       A
# A       A
# A A A A A
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print('A',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# *
# * *
# *   *
# *     *
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         if i == j or j==1 or i == 5:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# * * * * *
# *     *
# *   *
# * *
# *
# for i in range(1,6):
#     for j in range(1,7-i):
#         if i == 1 or j == 1 or j == 6 - i:
#             print('*',end =' ')
#         else:
#             print(' ',end=' ')
#     print()


## Category 6: Right Pyramid


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')

#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')

#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

#         A
#       A B
#     A B C
#   A B C D
# A B C D E
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(chr(64 + j),end=' ')
#     print()

#         A
#       B B
#     C C C
#   D D D D
# E E E E E
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(chr(64 + i),end=' ')
#     print()

#         1
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

## Category – Full Pyramids

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         print('*',end=' ')
#     print()

#         1
#       1 1 1
#     1 1 1 1 1
#   1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# for i in range (1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         print('1',end=' ')
#     print()

#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5
# for i in range(1,6):
#     for s in range (6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         print(i,end=' ')
#     print()

#Category 9 – Number Full Pyramid


#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     for k in range(i-1,0,-1):
#         print(k,end=' ')
#     print()

#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(chr(64+j),end=' ')
#     for k in range(i-1,0,-1):
#         print(chr(64 + k),end=' ')
#     print()


## Category 10 – Inverted Full Pyramid

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# for i in range(1,6):
#     for s in range(1,i):
#         print(' ',end=' ')
#     for j in range(1,12-(2*i)):
#         print('*',end=' ')
#     print()

## Category 11 – Diamond Pattern

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         print('*',end=' ')
#     print()
# for i in range(2,6):
#     for s in range(1,i):
#         print(' ',end=' ')
#     for j in range(1,12-(2*i)):
#         print('*',end=' ')
#     print()

#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j==1 or i==5 or j==2*i-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *
# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j == 1 or j == 2*i - 1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# for i in range(2,6):
#     for s in range(1,i):
#         print(' ',end=' ')
#     for j in range(1,12-(2*i)):
#         if j==1 or j == 12-(2*i) - 1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


## Category 13 – Floyd Triangle


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=' ')
#         num +=1
#     print()


## Category 14 – Butterfly Pattern


# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     for s in range(1,9-2*i):
#         print('_',end=' ')
#     # for j in range(1,i+1):
#     #     print(i,end=' ')
#     print()
# for i in range(1,4):
#     for j in range(1,5-i):
#         print(i,end=' ')
#     for s in range(1,2*i+1):
#         print(' ',end=' ')
#     for j in range(1,5-i):
#         print(i,end=' ')
#     print()


# Category 15 – Sandglass Pattern

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
# for i in range(1,6):
#     for s in range(2,i+1):
#         print(' ',end=' ')
#     for j in range(11-2*i,0,-1):
#         print('*',end=' ')
#     print()
# for i in range(2,6):
#     for s in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         print('*',end=' ')
#     print()


# ## Category 16 – Pascal Triangle

#         1
#       1 1
#     1 2 1
#   1 3 3 1
# 1 4 6 4 1

# n = 5
# for i in range(n):
#     for s in range(n-i-1):
#         print(' ',end=' ')
#     num = 1
#     for j in range(i+1):
#         print(num,end=' ')
#         num = num * (i-j) // (j+1)
#     print()