from multiprocessing import Process


def f2(name):
    print('hello1', name)

def f1(name):
    print('hello2', name)


if __name__ == '__main__':
    p = Process(target=f1, args=('bob',)).start()

    p1 = Process(target=f2, args=('CHICCO',)).start()

    # p.join()
