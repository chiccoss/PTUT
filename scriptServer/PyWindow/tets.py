import threading


def useFile(f1, f2):
    f1.open()
    f1.write("This is file 1")

    f2.write("This is file 2")


def printt():
    f1 = open("C:/Users/sohayb/scriptServer/thiIsTheFile.txt")
    f2 = open("C:/Users/sohayb/scriptServer/thiIsTheFile.txt")
    useFile(f1, f2)


thread = threading.Thread(target=printt)
thread.start()
thread.join()
print("Sorti")
