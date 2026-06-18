# 8. Print 1 to 100 in snakes and ladder pattern.

start = 1
end = 10

for i in range(1,11):

    if i % 2 != 0:
        for i in range(start,end+1):
            print(i,end=' ')

    else:
        for i in range(end,start - 1,-1):
            print(i,end=' ')

    print()

    start += 10
    end += 10