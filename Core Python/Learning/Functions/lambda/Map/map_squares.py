data = [1,2,3,4,5,6,7,8,9,10]

# sq = lambda n: n * n
# res = list(map(sq,data))

res = list(map(lambda n: n * n,data))
print(res)