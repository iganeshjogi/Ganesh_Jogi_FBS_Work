def digit_sep (n):

    if n > 0:
        d = n % 10
        print(d)
        digit_sep(n//10)
        

res= digit_sep(124)
print(res)