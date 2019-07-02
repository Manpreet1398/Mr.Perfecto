import queue
import threading
import time

'''LIFO Q'''
q=queue.LifoQueue()
for i in range(5):
    q.put(i)
while not q.empty():
    print (q.get(),end=' ')

q=queue.PriorityQueue()
q.put(4)
q.put(1)
q.put(3)
q.put(2)

