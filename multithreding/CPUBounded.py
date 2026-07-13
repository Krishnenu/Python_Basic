from time import time
from threading import Thread
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

    t1=Thread(target=calculate,args=(0,mid))
    t2=Thread(target=calculate,args=(mid,num))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    stop=time()

    print(f" Time Taken in parrallel: {stop-start:2f} seconds")

# because of GIL its taking almost same time in both case its like locking one task till that 
# other is waiting so almost same time took in both if i do multithreading - 
# Thread - share the momory lightweight fast to create, share same GIL
# Soln is that : multiprocsessing  takes time to create, haveing own memory and GIL

