'''
1. We want to generate Fibonacci numbers up to a certain limit.
Instead of computing and storing the entire sequence in memory,
create generator to yield Fibonacci numbers one by one,
conserving memory and allowing for easy iteration.'''

def fibonacciseries(n):
    a, b = 0, 1
    for i in range(n):
        yield a    
        a, b = b, a + b
    

g = fibonacciseries(5)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g,'Ended'))