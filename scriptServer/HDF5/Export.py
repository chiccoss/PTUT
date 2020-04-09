import tkinter as tk
from math import *
from tkinter.filedialog import *

import h5py
import numpy as np


# In[70]:


class Cellule:
    nbrCoordonne = 0
    name = ''

    def __init__(self, dirPath, iteratorFile):
        self.x_array = []
        self.y_array = []
        self.z_array = []
        print('iterateur ', iteratorFile)
        fichier = open(dirPath +"/"+ str(iteratorFile) + "/micromesh.geo", "r")
        for i in range(7):
                lalignesuivante = fichier.readline()
        self.name = ('Mesh ' + str(iteratorFile))
        print(self.name)
        lalignesuivante = fichier. readline()
        lalignesuivante = fichier.readline()
        if(lalignesuivante is None):
            print("erreur coord ")
            exit()
        print('Coordonnee ' + lalignesuivante)
        self.nbrCoordonne = int(lalignesuivante)

        lalignesuivante = fichier.readline()
        if(lalignesuivante is None):
            print("erreur coord ")
            exit()
        for i in range(self.nbrCoordonne):
            self.x_array.append(float(lalignesuivante))
            print('x ', self.x_array[i])
            lalignesuivante = fichier.readline()
            if(lalignesuivante is None):
                print("erreur coord ")
                exit()
        for i in range(self.nbrCoordonne):
            self.y_array.append(float(lalignesuivante))
            print('y ', self.y_array[i])
            lalignesuivante = fichier.readline()
            if(lalignesuivante is None):
                print("erreur coord ")
                exit()
        for i in range(self.nbrCoordonne):
            self.z_array.append(float(lalignesuivante))
            print('z ', self.z_array[i])
            lalignesuivante = fichier.readline()
            if(lalignesuivante is None):
                print("erreur coord ")
                exit()
        fichier.close()

# In[71]:


class Element_3D:
    liste = []
    dirPath = ''
    nbMesh = 0

    def __init__(self, dirPath):
        self.dirPath = dirPath
        self.nbMesh = getNbMesh(dirPath)
        liste = [self.nbMesh]
        print("Reading coordinates...")
        for currentMesh in range(self.nbMesh):
            tempCell = Cellule(dirPath, currentMesh)
            self.liste.append(tempCell)
            print("   ", str(currentMesh + 1), "out of", self.nbMesh, "mesh read")
        print(" ")

    # In[72]:


def getNbMesh(dirPath):
    onlyfiles = next(os.walk(dirPath))[2]  # dir is your directory path as string
    number = len(onlyfiles)  # nombre de file sans les dossiers dans le dossier

    list = os.listdir(dirPath)  # dir is your directory path
    number_files = len(list)

    return number_files - number


# In[73]:


def Plan(c, planVar, planVal,infOuSup):  # planVar est égal à (x,y,z) ,planVal est la valeur par rapport à laquelle la cellule est testé ,infOuSup prend la valeur "inf" ou "sup"
    if planVar == "x":
        if infOuSup == "inf":
            i = 0
            while i < c.nbrCoordonne:
                if c.x_array[i] < planVal:
                    return True
                i += 1
        if infOuSup == "sup":
            i = 0
            while i < c.nbrCoordonne:
                if c.x_array[i] > planVal:
                    return True
                i += 1
    if planVar == "y":
        if infOuSup == "inf":
            i = 0
            while i < c.nbrCoordonne:
                if c.y_array[i] < planVal:
                    return True
                i += 1
        if infOuSup == "sup":
            i = 0
            while i < c.nbrCoordonne:
                if c.y_array[i] >= planVal:
                    return True
                i += 1
    if planVar == "z":
        if infOuSup == "inf":
            i = 0
            while i < c.nbrCoordonne:
                if c.z_array[i] < planVal:
                    return True
                i += 1
        if infOuSup == "sup":
            i = 0
            while i < c.nbrCoordonne:
                if planVal < c.z_array[i]:
                    return True
                i += 1
    return False


def isInGridCell2D(cell, nbGridCell, currentGridCell, gridCellSize):
    infXLimit = floor(currentGridCell % sqrt(nbGridCell)) * gridCellSize
    supXLimit = (floor(currentGridCell % sqrt(nbGridCell)) + 1) * gridCellSize

    infYLimit = floor(currentGridCell / sqrt(nbGridCell)) * gridCellSize
    supYLimit = (floor(currentGridCell / sqrt(nbGridCell)) + 1) * gridCellSize

    if (Plan(cell, "x", infXLimit, "sup") == True) and (Plan(cell, "x", supXLimit, "inf") == True) and (Plan(cell, "y", infYLimit, "sup") == True) and (Plan(cell, "y", supYLimit, "inf") == True):
        return True
    else:
        return False


def isInGridCell3D(cell, nbGridCell, currentGridCell, gridCellSize):
    infXLimit = floor(currentGridCell % nbGridCell ** (1. / 3.)) * gridCellSize
    supXLimit = (floor(currentGridCell % nbGridCell ** (1. / 3.)) + 1) * gridCellSize

    infYLimit = floor((currentGridCell / nbGridCell ** (1. / 3.)) % nbGridCell ** (1. / 3.)) * gridCellSize
    supYLimit = (floor((currentGridCell / nbGridCell ** (1. / 3.)) % nbGridCell ** (1. / 3.)) + 1) * gridCellSize

    infZLimit = floor(currentGridCell / (pow(nbGridCell ** (1. / 3.), 2))) * gridCellSize
    supZLimit = (floor(currentGridCell / (pow(nbGridCell ** (1. / 3.), 2))) + 1) * gridCellSize

    if (Plan(cell, "x", infXLimit, "sup")) and (Plan(cell, "x", supXLimit, "inf")) and (Plan(cell, "y", infYLimit, "sup")) and (Plan(cell, "y", supYLimit, "inf")) and (Plan(cell, "z", infZLimit, "sup")) and (Plan(cell, "z", supZLimit, "inf")):
        return True
    else:
        return False

def export_HDF(directoryPath, HDFLocation, gridCellSize, dimension):
    element3D = Element_3D(directoryPath)
    print("Exporting to HDF...")
    TTLINSERT = 0
    if gridCellSize > 0.5 or gridCellSize <= 0:
        print("    gridCellSize must be between ]0;0.5[ \n    Aborting Export...")
        return
    else:
        nbGridCell = int(pow(1 / gridCellSize, dimension))

        with h5py.File(HDFLocation, 'w') as hdf:
            for currentGridCell in range(nbGridCell):
                Group = hdf.create_group(("GridCell{}".format(currentGridCell)))
                Locs = []

                for currentMesh in range(element3D.nbMesh):
                    loc = currentMesh
                    if dimension == 3:
                        if isInGridCell3D(element3D.liste[currentMesh], nbGridCell, currentGridCell, gridCellSize):
                            TTLINSERT+=1
                            Locs.append(loc)
                    elif dimension == 2:
                        if isInGridCell2D(element3D.liste[currentMesh], nbGridCell, currentGridCell, gridCellSize):
                            Locs.append(loc)
                matrixLoc = np.array(Locs)
                Group.create_dataset("Location", data=matrixLoc, compression='gzip', compression_opts=9)
                print(TTLINSERT)
                print("   ", str(currentGridCell + 1), "out of", str(nbGridCell), "GridCell exported")
                TTLINSERT = 0

def do_Export():
    filename = str(fileEntry.get())
    directory = str(directoryEntry.get())
    gridDimension = int(tkvar.get())
    gridCell = float(gridCellSizeEntry.get())
    export_HDF(directory, filename, gridCell, gridDimension)


# In[78]:


def setFileEntry():
    fileEntry.insert(0, str(asksaveasfilename(initialdir="/", title="Select file",
                                              filetypes=(("hdf5 files", "*.h5"), ("all files", "*.*")))))


# In[79]:


def setDirectoryEntry():
    directoryEntry.insert(0, str(askdirectory()))


# In[80]:
"""
MAIN WINDOW
"""
window = tk.Tk()

window.title("Python GUI App")
window.configure(width=500, height=300)
window.configure(bg='lightgray')

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

fileEntry = tk.Entry(window)
directoryEntry = tk.Entry(window)

tk.Label(window, text=".hdf5 Directory: ").grid(row=0, padx=5)
fileEntry.grid(row=0, column=1)
tk.Button(window,
          text='Select File',
          command=setFileEntry).grid(row=0,
                                     column=2,
                                     sticky=tk.W,
                                     padx=5)

tk.Label(window, text=".case Directory: ").grid(row=1, padx=5)
directoryEntry.grid(row=1, column=1)
tk.Button(window,
          text='Select Directory',
          command=setDirectoryEntry).grid(row=1,
                                          column=2,
                                          sticky=tk.W,
                                          padx=5)
tkvar = StringVar(window)
choices = {3, 2}
tkvar.set(3)
popupMenu = OptionMenu(window, tkvar, *choices)
Label(window, text="Dimension: ").grid(row=3, column=0)
popupMenu.grid(row=3, column=1)

tk.Label(window, text="gridCellSize: ").grid(row=3, padx=5, column=2)
gridCellSizeEntry = tk.Entry(window)
gridCellSizeEntry.grid(row=3, column=3)

tk.Button(window,
          text='Quit',
          command=window.quit).grid(row=5,
                                    column=3,
                                    sticky=tk.W)

tk.Button(window,
          text='Export To HDF5', command=do_Export).grid(row=5,
                                                         column=0,
                                                         sticky=tk.W)

window.mainloop()