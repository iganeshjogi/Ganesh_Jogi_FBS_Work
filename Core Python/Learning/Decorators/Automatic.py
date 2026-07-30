def myDecorator(fun):
    def wrapper():
        print('This is start of decoration.')
        fun()
        print('This is end of decoration.')
    return wrapper

@myDecorator
def greet():
    print('Good Evening!')

greet()