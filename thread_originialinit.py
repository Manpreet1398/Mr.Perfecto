import threading
import time


class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        # can retain all methods and attributes from original Thread class init method
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print("Thread starting")
        super(MyThread, self).run(*args, **kwargs)
        print("Thread has finished")

def sleeper(num, style):
    print("we are sleeping for {} seconds as {}".format(num, style))
    time.sleep(num)


t = MyThread(number=3, style='yellow', target=sleeper, args=(5, 'yellow'))
t.start()
 #create a class and override methods of class ,const,run without using super and with super
#create a method,list,key method,list 1 list 2 ,and read in list 3 using threading, use with and without lock