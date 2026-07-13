from time import time
from multiprocessing import Process
def calculate(n1,n2):
    sum=0
    for n in range(n1,n2):
        sum+=n*n


if __name__=='__main__':
    num=50_000_000
    start=time()
    calculate(0,num)
    stop=time()
    print(f" Time Taken in Normal: {stop-start:2f} seconds")


    mid=num//2

    start=time()

    t1=Process(target=calculate,args=(0,mid))
    t2=Process(target=calculate,args=(mid,num))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    stop=time()

    print(f" Time Taken in multiprocessing: {stop-start:2f} seconds")