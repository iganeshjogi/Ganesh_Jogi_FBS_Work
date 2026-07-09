# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

d = {}

def dictionaryNumberSquaresPair(dictionary, nth_Number):

    i = 1
    while i <= nth_Number:
        dictionary[i] = i*i
        i += 1
    return dictionary


n = int(input('Enter the nth Number: '))

res = dictionaryNumberSquaresPair(d, n)

print(res)