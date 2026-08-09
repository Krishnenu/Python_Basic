from multiprocessing import Process
import time

def take_order(name):
    print(f"Start of {name}")
    time.sleep(5)
    print(f"End of {name}")


if __name__ =="__main__":
    chai_makers=[
        Process(target=take_order,args=(f"chai maker {i+1}",))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    for p in chai_makers:
        p.join()

print("completed")