from paraview.simple import *
import threading
import os
import sys
import time
import asyncio


class ReaderWriterCallback:

    def __init__(self):
        # self.camera = GetActiveCamera()
        # self.mutex1 = threading.Lock()
        # self.mutex2 = threading.Lock()
        # self.mutex1.acquire()

        #          self.mutex2.acquire()
        #          self.mutex2.release()
        # self.read = "r"
        # self.write = "a"
        # self.data = "C:/Users/sohayb/scriptServer/PyWindow/txt.txt"
        # self.ReaderFile = open(self.data, "r")
        # self.WriterFile = open(self.data, "a")
        #           print('hello mutex lock')
        self.timer_count = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        # self.mutex = threading.Lock()
        # print('hello after assigning data')
        # self.file  = open(self.data)
        # print('hello from END init camera')

        self.tab = [["6", "15", "3", "14"], ["7", "0", "9", "8"], ["2", "5", "13", "12"], ["1", "4", "11", "10"]]
        # GetActiveView()<<<<>>>>

    def CloseFiles(self):
        self.ReaderFile.close()
        self.WriterFile.close()

    def writer(self):
        # test = False
        # while test:

        for i in range(10):
            # self.timer_count = 0.1
            # self.mutex1.acquire()
            # self.mutex2.acquire() da utilizzare per reader and writer

            self.mutex.acquire()
            self.x, self.y, self.z = self.camera.GetPosition()
            # print(self.x, self.y, self.z)
            # print(time.time(), flush=True)
            # threading.sleep(20)  # 50 Hz
            self.mutex.release()

            # 0,02 s = 20 ms = 50 mhz
            time.sleep(1)
        """
            if not self.WriterFile.closed():
                self.WriterFile.write(str(self.camera.GetPosition()) + '\n')
                self.WriterFile.flush()
                # threading.sleep(20)
            else:
                self.WriterFile = open(self.data, self.write)
                self.WriterFile.write(str(self.camera.GetPosition()) + '\n')
                self.WriterFile.flush()
                # threading.sleep(20)
            # threading.sleep(100)
            # self.timer_count += 0.1
            # the_file.write(str(self.camera.GetPosition()) + '\n')
            # self.mutex1.release() da utilizzare per reader and writer
        """

    def ParseCoord(self, string):  # Parse x,y,z from file
        coord = [0, 0, 0]
        i = 0
        for val in string.split(","):
            coord.insert(i, val)
            i = i + 1

        coord[0] = coord[0].replace('(', '')
        coord[2] = coord[2].replace(')', '')

        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]
        return x, y, z

    def DeleteAllMesh(self):
        i = 7
        while i != 0:
            d = FindSource("EnSightReader" + str(i))
            Delete(d)
            i = i - 1

    def EnsightReadersBruh(self, string):

        print("Inside Reader bruh")
        sys.stdout.flush()
        base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'
        if string == "bs":
            for i in range(len(self.tab)):
                temp = EnSightReader(CaseFileName=base + self.tab[0][i] + '/micromesh.case')
            return
        if string == "bd":
            for i in range(len(self.tab)):
                temp = EnSightReader(CaseFileName=base + self.tab[1][i] + '/micromesh.case')
            return
        if string == "hg":
            for i in range(len(self.tab)):
                temp = EnSightReader(CaseFileName=base + self.tab[2][i] + '/micromesh.case')
            return
        if string == "hd":
            for i in range(len(self.tab)):
                print(i)
                temp = EnSightReader(CaseFileName=base + self.tab[3][i] + '/micromesh.case')
            return
        else:
            return

    def FindMeshToUpload(self):
        print("Inside file mesh")
        if 0.0 < self.x < 0.5 and 0.0 < self.y < 0.5:
            self.EnsightReadersBruh("bs")  # les carreaux en bas a gauche (6, 15, 3, 14)
        if 0.5 < self.x < 1 and 0.0 < self.y < 0.5:
            self.EnsightReadersBruh("bd")  # les carreaux en bas a droite (7 ,0, 9 ,8)
        if 0.0 < self.x < 0.5 and 0.5 < self.y < 1:
            self.EnsightReadersBruh("hg")  # les carreaux en haut a gauche (2 ,5, 13, 12)
        if 0.5 < self.x < 1 and 0.5 < self.y < 1:
            self.EnsightReadersBruh("hd")  # les carreaux en haut a droite (1, 4 ,11, 10)
        else:
            print("Inside return")
            sys.stdout.flush()
            Show()
            Render()
            return

    def updateView(self):
        camera = GetActiveCamera()
        camera.SetPosition(0.5, 0.0, 0.4)

        self.x, self.y, self.z = camera.GetPosition()
        print("Position Written")
        sys.stdout.flush()
        self.FindMeshToUpload()
        # time.sleep(2)

    def launchAfter(self):
        time.sleep(3)
        self.DeleteAllMesh()

    def reader(self):
        # print("Inside Reader")
        # test = False
        # while test:
        # for i in range(200):
        # self.timer_count = 0.1
        # self.mutex1.acquire() da utilizzare per reader and writer
        # self.mutex.acquire()  # blocking=False
        # self.camera.SetPosition(self.x, self.y, self.z)

        self.x, self.y, self.z = self.camera.GetPosition()
        # print(self.x, self.y, self.z)
        # print(time.time(), flush=True)
        # threading.sleep(20)  # 50 Hz
        # self.mutex.release()
        time.sleep(1)
        # 0,02 s = 20 ms = 50 mhz

        self.DeleteAllMesh()
        self.FindMeshToUpload()
        # Render()
        # threading.sleep(20)
        # self.mutex.release()

        """
            if not self.ReaderFile.closed():
                # threading.sleep(100)
                self.ReaderFile = open(self.data, self.read)
                # self.x, self.y, self.z = \
                self.ParseCoord(self.ReaderFile.read())
                self.DeleteAllMesh()
                self.FindMeshToUpload(self.x, self.y)
            else:
                # threading.sleep(100)
                self.ReaderFile = open(self.data, self.read)
                # self.x, self.y, self.z =
                self.ParseCoord(self.ReaderFile.read())
                self.DeleteAllMesh()
                self.FindMeshToUpload(x, y)
            
            #  self.timer_count += 0.1
            # self.mutex2.release() da utilizzare per reader and writer
        """


async def updateView(i):
    camera = GetActiveCamera()
    if i == 0:
        camera.SetPosition(0.1, 0.1, 0.0)
    if i == 1:
        camera.SetPosition(0.6, 0.1, 0.0)
    if i == 2:
        camera.SetPosition(0.1, 0.6, 0.0)
    if i == 3:
        camera.SetPosition(0.6, 0.6, 0.0)
    else:
        camera.SetPosition(0.6, 0.6, 0.0)

    x, y, z = camera.GetPosition()
    # print(x, y, z, flush=True)
    await FindMeshToUpload(x, y)


async def EnsightReadersBruh(string):
    print("Inside Reader bruh")
    tab = [["6", "15", "3", "14"], ["7", "0", "9", "8"], ["2", "5", "13", "12"], ["1", "4", "11", "10"]]
    base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'
    if string == "bs":
        for i in range(len(tab)):
            temp = EnSightReader(CaseFileName=base + tab[0][i] + '/micromesh.case')
            Show(temp)
        Render()
        await asyncio.sleep(1)
        return
    if string == "bd":
        for i in range(len(tab)):
            temp = EnSightReader(CaseFileName=base + tab[1][i] + '/micromesh.case')
            Show(temp)
        Render()
        return
    if string == "hg":
        for i in range(len(tab)):
            temp = EnSightReader(CaseFileName=base + tab[2][i] + '/micromesh.case')
            Show(temp)
        Render()
        return
    if string == "hd":
        for i in range(len(tab)):
            # print(i)
            temp = EnSightReader(CaseFileName=base + tab[3][i] + '/micromesh.case')
            Show(temp)
        Render()
        return
    else:
        return

async def FindMeshToUpload(x, y):
    print("Inside file mesh")
    if 0.0 < x < 0.5 and 0.0 < y < 0.5:
        await EnsightReadersBruh("bs")  # les carreaux en bas a gauche (6, 15, 3, 14)
    if 0.5 < x < 1 and 0.0 < y < 0.5:
        await EnsightReadersBruh("bd")  # les carreaux en bas a droite (7 ,0, 9 ,8)
    if 0.0 < x < 0.5 and 0.5 < y < 1:
        await EnsightReadersBruh("hg")  # les carreaux en haut a gauche (2 ,5, 13, 12)
    if 0.5 < x < 1 and 0.5 < y < 1:
        await EnsightReadersBruh("hd")  # les carreaux en haut a droite (1, 4 ,11, 10)


# ReaderFile = open("C:/Users/sohayb/scriptServer/PyWindow/txt.txt", "r")
# WriterFile = open("C:/Users/sohayb/scriptServer/PyWindow/txt.txt", "a")

# ReaderFile = "C:/Users/sohayb/scriptServer/PyWindow/txt.txt"
# WriterFile = "C:/Users/sohayb/scriptServer/PyWindow/txt.txt"

# READWRITE = ReaderWriterCallback()

# threadWriter = threading.Thread(target=READWRITE.writer)
# threadReader = threading.Thread(target=)
# th = threading.Thread(target=READWRITE.launchAfter)

# threadWriter.start()
# threadReader.start()
# th.start()
for i in range(20):
    asyncio.run(updateView(i))
    # Interact()

    # time.sleep(1.0)
    # sys.stdout.flush()
# threadWriter.join()
# threadReader.join()
# th.join()
# READWRITE.DeleteAllMesh()


# READWRITE.CloseFiles()

# TODO : ADD LISTENER TO END WRITER AND RADER FUNCTION
