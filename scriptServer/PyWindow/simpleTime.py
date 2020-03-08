import threading
import time
import sys
import os




def print_hello():
    filev =open("Hi.txt", "a")
    for i in range(10):
        filev.write("Hello")
        filev.flush()
        print("AFTER flush waiting for one second",flush=True)
        time.sleep(1)
    filev.close()

    #os.fsync(filev.fileno())
    #fileld = filev.fileno()
    #print(fileld)
    #filev.close()



def print_hi():
    for i in range(4):
        time.sleep(3)
        print("Hi")
        sys.stdout.flush()


t1 = threading.Thread(target=print_hello)
#  t2 = threading.Thread(target=print_hi)
t1.start()
#  t2.start()
