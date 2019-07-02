import threading
import time


def sleeper(n, name):
    print("Hi I am {},gonna sleep for 5 seconds \n".format(name))
    time.sleep(n)
    print("%s woke up after sleep \n" % (name))


t = threading.Thread(target=sleeper, name="Thread1", args=(5, "Thread1"))
t.start()
''' join block interpretor to execute the task til the time thread finishes executing its function'''
t.join()
print("Hi")
print("Woke up please")
