class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    def __str__(self):
        return f'{self.h}:{self.m}:{self.s}'
    def __add__(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s
        return (f'{h}:{m}:{s}')

t1 = Time(10,10,10)
t2 = Time(11,11,11)

print(t1)
print(t2)
print(t1+t2)