import threading
import time

def take_order():
    for i in range(1,4):
        print(i)
        time.sleep(1)


def take_brew():
    for i in range(1,5):
        print(i)
        time.sleep(2)


order_thread=threading.Thread(target=take_order)
order_brew=threading.Thread(target=take_brew)

order_thread.start()
order_brew.start()


order_brew.join()
order_thread.join()
