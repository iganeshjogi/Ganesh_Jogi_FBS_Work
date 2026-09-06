from threading import Thread

def deposit(amt):
    with open('Core Python/Demos/MultiThreading/balance.txt', 'r') as fp:
        bal = int(fp.read())
        bal = bal + amt
    with open('Core Python/Demos/MultiThreading/balance.txt', 'w') as fp:
        fp.write(str(bal))

def withdraw(amt):
    with open('Core Python/Demos/MultiThreading/balance.txt', 'r') as fp:
        bal = int(fp.read())
        bal = bal - amt
    with open('Core Python/Demos/MultiThreading/balance.txt', 'w') as fp:
        fp.write(str(bal))

t1 = Thread(name='Thread1', target=deposit, args=(20000,))
t2 = Thread(name='Thread2', target=withdraw, args=(10000,))

t1.start()
t2.start()