'''
Q2. Create a class Distance with data members as km,m and cm and add following
methods :
    a. Constructor
    b. Destructor
    c. Overload +,- operator'''

class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Distance Object Destroyed")

    def __add__(self, other):
        cm = self.cm + other.cm
        carry_m = cm // 100
        cm = cm % 100

        m = self.m + other.m + carry_m
        carry_km = m // 1000
        m = m % 1000

        km = self.km + other.km + carry_km

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def __sub__(self, other):
        km = self.km
        m = self.m
        cm = self.cm

        cm -= other.cm
        if cm < 0:
            m -= 1
            cm += 100

        m -= other.m
        if m < 0:
            km -= 1
            m += 1000

        km -= other.km

        return Distance(km, m, cm)


d1 = Distance(5, 200, 50)
d2 = Distance(2, 150, 70)

print(d1 + d2)
print(d1 - d2)