import threading
import time

total = 4


def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item \n')
        total += 1
    print('creation is done \n')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item \n', total)
        total += 1
    print('creation is done \n', total)


def limits_items():
    # print('finished sleeping')

    global total
    while True:
        if total > 5:

            print('overload \n', total)
            total -= 3
            print('subtracted 3 \n', total)
        else:
            time.sleep(1)
            print('waiting \n', total)


creator1 = threading.Thread(target=creates_items)
creator2 = threading.Thread(target=creates_items_2)
limitor = threading.Thread(target=limits_items, daemon=True)

print(limitor.isDaemon())

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()

print('our ending value of total is', total)