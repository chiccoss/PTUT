#connection = Connect("LAPTOP-5T63V61S", 11111)
# create an INET, STREAMing socket
#s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
#s.connect(("localhost", 11111))

#connect=Connect("laptop-5t63v61s", 11111)



#s=Sphere()
#Show(s)
#writer = XMLPPolyDataWriter(FileName='sphere.pvtp')
#UpdatePipeline()

#Render()

#time.sleep(2.3)

#Disconnect()


import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
	
def ReadFile(name):
	file = open(name, "r") 
	print (file.read() )
   
   
if __name__ == "__main__":

	ReadFile("thiIsTheFile.txt")

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)