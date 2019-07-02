import threading


class MyThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print("Thread {} has started\n".format(self.number))
        self.func(*self.args)
        print('thread {} has finished\n'.format(self.number))


def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)


thread_list = []

for i in range(50):
    t = MyThread(number=i + 1, func=double, args=[i, 3])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()
