from multiprocessing.pool import ThreadPool
from random import randint
import threading
import time

MAX_THREADS = 5  # Number of threads that can run concurrently.
print_lock = threading.Lock()  # Prevent overlapped printing from threads.


def myFunc():
    print('myFunc')
    time.sleep(random.randint(0, 1))  # Pause a variable amount of time.
    print('myFunc')
    print_lock.acquire()
    print('myFunc')
    print_lock.release()


def test():
    pool = ThreadPool(processes=MAX_THREADS)

    for _ in range(100):  # Submit as many tasks as desired.
        pool.apply_async(myFunc, args=())

    pool.close()  # Done adding tasks.
    pool.join()  # Wait for all tasks to complete.
    print('done')


if __name__ == '__main__':
    test()
