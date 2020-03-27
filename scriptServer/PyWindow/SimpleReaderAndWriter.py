from paraview.simple import *
import threading
import os
import sys
import time
import random


def EnsightReadersBruh(string):
    print("Inside Reader bruh")
    tab = [["6", "15", "3", "14"], ["7", "0", "9", "8"], ["2", "5", "13", "12"], ["1", "4", "11", "10"]]
    base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'
    if string == "bs":
        for i in range(len(tab)):
            temp = EnSightReader(CaseFileName=base + tab[0][i] + '/micromesh.case')
            Show(temp)
        Render()
        # await asyncio.sleep(1)
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


def FindMeshToUpload(x, y):
    print("Inside file mesh")
    if 0.0 < x < 0.5 and 0.0 < y < 0.5:
        EnsightReadersBruh("bs")  # les carreaux en bas a gauche (6, 15, 3, 14)
    if 0.5 < x < 1 and 0.0 < y < 0.5:
        EnsightReadersBruh("bd")  # les carreaux en bas a droite (7 ,0, 9 ,8)
    if 0.0 < x < 0.5 and 0.5 < y < 1:
        EnsightReadersBruh("hg")  # les carreaux en haut a gauche (2 ,5, 13, 12)
    if 0.5 < x < 1 and 0.5 < y < 1:
        EnsightReadersBruh("hd")  # les carreaux en haut a droite (1, 4 ,11, 10)


def updateView():
    camera = GetActiveCamera()
    i = random.randint(0, 3)
    if i == 0:
        camera.SetPosition(0.1, 0.1, 0.0)
    if i == 1:
        camera.SetPosition(0.6, 0.1, 0.0)
    if i == 2:
        camera.SetPosition(0.1, 0.6, 0.0)
    if i == 3:
        camera.SetPosition(0.6, 0.6, 0.0)
    x, y, z = camera.GetPosition()
    FindMeshToUpload(x, y)


threadWriter = threading.Thread(target=updateView).start()
#threadWriter
#threadWriter.join()
