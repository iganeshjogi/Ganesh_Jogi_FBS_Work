from threading import Thread
import time

def fun1(str):
    for char in str:
        print(char, end = ' ', flush = True)
        time.sleep(1)

def fun2(str):
    for char in str:
        print(char, end = ' ', flush = True)
        time.sleep(1)


t1 = Thread(name='Thread1', target=fun1, args=('11111111111111111111',))
t2 = Thread(name='Thread2', target=fun2, args=('22222222222222222222',))

t1.start()
t1.join(3)
t2.start()