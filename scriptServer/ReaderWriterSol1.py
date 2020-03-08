import threading

class Reader_writer(Object):
    "Reader - writer solution using simple locks"
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.mutex1 = threading.Lock()
        self.mutex2 = threading.Lock()
        self.readPending = threading.Lock()
        self.writeBlock = threading.Lock()
        self.readBlock = threading.Lock()

# This is kind of complicated locking stuff. Don't worry about why there
# are so many locks, it is just part of the known solution to
# the readers and writers problem.
#
# The basic idea of the readers and writers algorithm is to use locks to
# quickly see how many other readers and writers there are.  writeBlock
# is the only lock held while reading the data.  Thus the reader only
# prevents writers from entering the critical section.  Both writeBlock
# and readBlock are held while writing to the data.  Thus the writer
# blocks readers and other writers.

# Note: This shows reader() and writer() methods.  The critical section
#   code could be added directly to these methods.
#   Antother valid way to structure the code is to make methods for
#   start_read(), end_read(), start_write(), end_write(). Other
#   methods for read(), write() could be added to the class; or, the
#   threads that use the class could read and write extrenal to the
#   class.

    def reader(self, lastread):
        "Reader of readers and writers algorithm"
        self.readPending.acquire()
        self.readBlock.acquire()
        self.mutex1.acquire()
        self.readers = self.readers + 1
        if self.readers == 1: self.writeBlock.acquire()
        self.mutex1.release()
        self.readBlock.release()
        self.readPending.release()
        
		
		
        self.mutex1.acquire()
        self.readers = self.readers - 1
        if self.readers == 0: self.writeBlock.release()
        self.mutex1.release()
        return retVal

    def writer(self, data):
        "Writer of readers and writers algorithm"
        self.mutex2.acquire()
        self.writers = self.writers + 1
        if self.writers == 1: self.readBlock.acquire()
        self.mutex2.release()
        self.writeBlock.acquire()
        #--------------------------
        #
        # critical section
        #
        #--------------------------
        self.writeBlock.release()
        self.mutex2.acquire()
        self.writers = self.writers - 1
        if self.writers == 0: self.readBlock.release()
        self.mutex2.release()