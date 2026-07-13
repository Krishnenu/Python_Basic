from threading import Thread
from time import sleep,time
# I/O Bound
class Hellow(Thread):
    def run(self):
        for i in range(5):
            print("Hellow", i + 1)
            sleep(0.03)

class Hii(Thread):
    def run(self):
        for i in range(5):
            sleep(0.02)
            print("Hi", i + 1)


if __name__ == "__main__":
    t1 = Hellow()
    t2 = Hii()

    # t1.run()
    # t2.run()
    # t1.start()
    # t2.start()


# with functions 


def hellow():
    for i in range(5):
        print("Hellow", i + 1)
        sleep(0.03)

def hii():
    for i in range(5):
        sleep(0.02)
        print("Hi", i + 1)

def download(filename):
    print("downloading files: ",filename)
    sleep(2)
    print("downloading complete")


if __name__ == "__main__":
    t1 = Thread(target=hellow)
    t2 = Thread(target=hii)

    t1.start()
    t2.start()

    t1.join()# wait for thread to complete first
    t2.join()


    files=["video.mp4","music.mp3","data.csv","image.png"]
    start=time()
    for f in files:
        download(f)
    end =time()
    print(f" serial time {end-start:2f} seconds")

    #using mutlithreading
    threads=[]
    for f in files:
        t=Thread(target=download,args=(f,))
        threads.append(t)

    start=time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end =time()
    print(f" parrel with time {end-start:2f} seconds")

    print ("done")
