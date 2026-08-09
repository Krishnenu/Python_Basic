import threading
import time

def take_milk():
    print("Boiling milk...")
    time.sleep(3)
    print("Milk boiled...")


def bun_tost():
    print("Toast Bun...")
    time.sleep(3)
    print("Done with toast...")


start=time.time()
t1=threading.Thread(target=take_milk)
t2=threading.Thread(target=bun_tost)
t1.start()
t2.start()
t1.join()
t2.join()

# take_milk()
# bun_tost()
end=time.time()

print(f"time taken: {end-start:.2f}")