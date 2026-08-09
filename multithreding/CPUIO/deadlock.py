import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_one():
    with lock_a:
        time.sleep(0.1)  # Simulate some work
        with lock_b:     # Will block forever if thread_two has lock_b
            print("Thread One secured both locks!")

def thread_two():
    with lock_b:
        time.sleep(0.1)
        with lock_a:     # Will block forever if thread_one has lock_a
            print("Thread Two secured both locks!")

t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)
t1.start()
t2.start()