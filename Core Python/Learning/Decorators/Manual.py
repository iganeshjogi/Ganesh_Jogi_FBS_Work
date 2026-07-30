def myDecorator(fun):
    print('This is start of decoration.')
    fun()
    print('This is end of decoration.')

def greet():
    print('Good Evening!')

myDecorator(greet)