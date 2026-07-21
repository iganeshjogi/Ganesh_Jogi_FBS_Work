class A:
    def get(self):
        print('Get method of class A.')

class B:
    def display(self):
        print('Display method of B.')

    def get(self):
        print('Get method of class B.')

class C(A, B):
    def show(self):
        print('Show method of class C.')


c1 = C()
c1.get()