from threading import Thread, Lock
from Sync import sync
from time import sleep


def main():
    lock = Lock()

    @sync(lock)
    def func1():
        print("Starting func1()")
        sleep(2)
        print("Done func1()")

    @sync(lock)
    def func2():
        print("Starting func2()")
        sleep(2)
        print("Done func2()")

    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
