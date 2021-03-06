import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} has started".format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        print("{} has finished".format(self.getName()))


def sleeper(n, name):
    print("Hi i am {} , gonna sleep for 5 seconds\n".format(name))
    time.sleep(5)
    print("%s woke up after sleep \n" % (name))


for i in range(4):
    t = MyThread(target=sleeper, name="thread" + str(i), args=(5, "thread" + str(i)))
    t.start()
