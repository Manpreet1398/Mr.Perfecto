import queue
import threading
import time

'''FIFO'''


def putting_thread(q):
    while True:
        print('starting point')
        time.sleep(10)
        q.put(5)
        print("put something")


q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,), daemon=True)
t.start()
q.put(5)
x = q.get()
print(x)
print("first item get")
'''this will freeze the program as q is empty'''
q.empty()
print("is this empty", q.get())
print("Q.finished")
#q.qsize a method to check size of the queue