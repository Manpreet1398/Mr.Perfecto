import threading

import time

lock = threading.Lock()

x = 0
COUNT = 1000000


def adding_2():
    global x
    with lock:
        #with (open/close)
        for i in range(COUNT):
            x += 2


def adding_3():
    global x
    with lock:
        for i in range(COUNT):
            x += 3


def subtracing_4():
    global x
    with lock:
        for i in range(COUNT):
            x -= 4


def aubtracting_1():
    global x
    with lock:
        for i in range(COUNT):
            x -= 1


t = threading.Thread(target=adding_2, )
t2 = threading.Thread(target=adding_3, )
t3 = threading.Thread(target=subtracing_4, )
t4 = threading.Thread(target=aubtracting_1, )

t.start()
t2.start()
t3.start()
t4.start()

t.join()
t2.join()
t3.join()
t4.join()

print(x)

''' when we are using with loc i.e using lock.acquire() and lock.release()



def aubtracting_1():
    global x
    lock.acquire()
    for i in range(COUNT):
        x -= 1
    lock.release()
'''