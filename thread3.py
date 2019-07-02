import threading
import time


def sleeper(n, name):
    print("I am %s gonna sleep for %s seconds \n" % (name, n))
    time.sleep(n)
    print("%s woke up after %s seconds \n" % (name, n))


start = time.time()
for n in range(5):
    sleeper(5, "Ankit")
end = time.time()
timetaken = end - start
print("timetaken ", timetaken)

print("Hi Thread")
print("Please woke up")

l = []
start = time.time()
for th in range(5):
    t = threading.Thread(target=sleeper, name="Thread" + str(th), args=(5, "Thread" + str(th)))
    l.append(t)
    t.start()
    print("%s start here and ends here" % (t.name))
for t in l:
    t.join()

end = time.time()
print("All thread executed in duration " + str(end - start))


def sleeper(n, name):
    print("I am %s gonna sleep for %s seconds \n" % (name, n))
    time.sleep(n)
    print("%s woke up after %s seconds \n" % (name, n))


start = time.time()

for i in range(5):
    print("Iteration %s has started" % (i))
    sleeper(5, i)

end = time.time()
print("All task executed in duration " + str(end - start))
