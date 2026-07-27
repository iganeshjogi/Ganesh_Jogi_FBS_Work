def valGen(n):
    for i in range (1, n + 1):
        yield i

res = valGen(10)

# print(res)

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

li = [15246]
print(li[0])

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res,0))