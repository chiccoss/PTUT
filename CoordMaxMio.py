# from paraview.simple import *
from array import *
import os

NBCOORDS = 3


def test_Choice_Int(i_number):
    assert isinstance(i_number, list)


def getNbMesh(dirPath):
    onlyfiles = next(os.walk(dirPath))[2]  # dir is your directory path as string
    number = len(onlyfiles)  # nombre de file sans les dossiers dans le dossier

    list = os.listdir(dirPath)  # dir is your directory path
    number_files = len(list)

    return number_files - number


class Cellule:
    nbrCoordonne = 0
    name = ''

    def __init__(self, dirPath, iteratorFile):
        self.x_array = []
        self.y_array = []
        self.z_array = []
        print('iterateur ', iteratorFile)
        fichier = open(dirPath + str(iteratorFile) + "\\micromesh.geo", "r")
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        self.name = ('Mesh ' + str(iteratorFile))
        print(self.name)
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        print('Coordonnee ' + lalignesuivante)
        self.nbrCoordonne = int(lalignesuivante)
        i = 0
        lalignesuivante = fichier.readline()
        while i < self.nbrCoordonne:
            self.y_array.append(float(lalignesuivante))
            print('y ', self.y_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0
        while i < self.nbrCoordonne:
            self.x_array.append(float(lalignesuivante))
            print('x ', self.x_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0
        while i < self.nbrCoordonne:
            self.z_array.append(float(lalignesuivante))
            print('z ', self.z_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0

        fichier.close()


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Element_3D:
    liste = []
    dirPath = ''
    xmax = 9999
    xmin = 9999
    ymin = 9999
    ymax = 9999
    zmax = 9999
    zmin = 9999

    def __init__(self, dirPath):
        self.nbMesh = getNbMesh(dirPath)
        i = 0
        dirPath = dirPath
        liste = [self.nbMesh]
        for currentMesh in range(self.nbMesh):
            self.liste.append(Cellule(dirPath, currentMesh))
            print((currentMesh + 1), "OUT OF", self.nbMesh, "DONE")

    def test_x(self, numeroCell, x, marge, iterateur):
        if self.liste[numeroCell].x_array[iterateur] < x + marge and self.liste[numeroCell].x_array[iterateur] > x - marge:
            return True

    def test_y(self, numeroCell, y, marge, iterateur):
        if self.liste[numeroCell].y_array[iterateur] < y + marge and self.liste[numeroCell].x_array[iterateur] > y - marge:
            return True

    def test_z(self, numeroCell, z, marge, iterateur):
        if self.liste[numeroCell].z_array[iterateur] < z + marge and self.liste[numeroCell].z_array[iterateur] > z - marge:
            return True

    def test_Cellule(self, numeroCell, marge, positionJoueur):
        i = 0
        while (i < self.liste[numeroCell].nbrCoordonne):
            if self.test_z(numeroCell, positionJoueur.z, marge, i) == True and self.test_y(numeroCell, positionJoueur.y,marge,i) == True and self.test_x(numeroCell, positionJoueur.x, marge, i) == True:
                return True

    def mesurer_Grille(self):
        self.xmax = self.gerer_xmax()
        print("xmax : ", self.xmax)
        self.xmin = self.gerer_xmin()
        print("xmin : ", self.xmin)
        self.ymax = self.gerer_ymax()
        print("ymax : ", self.ymax)
        self.ymin = self.gerer_ymin()
        print("ymin : ", self.ymin)
        self.zmax = self.gerer_zmax()
        print("zmax : ", self.zmax)
        self.zmin = self.gerer_zmin()
        print("zmin : ", self.zmin)

    def gerer_xmax(self):
        imax = 0
        max = 0
        i = 0
        y = 0
        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if max < self.liste[i].x_array[y]:
                    max = self.liste[i].x_array[y]
                    imax = i
                    break

                y = y + 1

            i = i + 1

        return max

    def gerer_xmin(self):
        imin = 0
        min = 0
        i = 0
        y = 0
        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if min > self.liste[i].x_array[y]:
                    min = self.liste[i].x_array[y]
                    imin = i
                    break

                y = y + 1

            i = i + 1
        return min

    def gerer_ymax(self):
        imax = 0
        max = 0
        i = 0

        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if max < self.liste[i].y_array[y]:
                    max = self.liste[i].y_array[y]
                    imax = i
                    break

                y = y + 1

            i = i + 1
        return max

    def gerer_ymin(self):
        imin = 0
        min = 0
        i = 0

        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if min > self.liste[i].y_array[y]:
                    min = self.liste[i].y_array[y]
                    imin = i
                    break

                y = y + 1

            i = i + 1
        return min

    def gerer_zmax(self):
        imax = 0
        max = 0
        i = 0

        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if max < self.liste[i].z_array[y]:
                    max = self.liste[i].z_array[y]
                    imax = i
                    break

                y = y + 1

            i = i + 1
        return max

    def gerer_zmin(self):
        imin = 0
        min = 0
        i = 0

        while i < self.nbMesh:
            y = 0
            while y < self.liste[i].nbrCoordonne:
                if min > self.liste[i].z_array[y]:
                    min = self.liste[i].z_array[y]
                    imin = i
                    break

                y = y + 1

            i = i + 1
        return min

    def InsertGrid(self):

        aspRat = [1, 1, 0.1]  # divide bathymetry by 100
        if self.xmin == 9999 or self.xmax == 9999 or self.ymin == 9999 or self.ymax == 9999 or self.zmin == 9999 or self.zmax == 9999:
            return
        else:
            grid = AddGrid(xlevels=[self.xmin,0.1,0.8,  self.xmax],
                           ylevels=[self.ymin,0.1,0.8, self.ymax],
                           zlevels=range(self.zmin, self.zmax, 1),
                           bounds=[self.xmin , self.xmax , self.ymin , self.ymax , self.zmin ,
                                   self.zmax], ratios=aspRat, AxisColor=[23, 87, 223],
                           AxisWidth=1)

            MakeSelectable()  # case=FindSource('MHMSolution')
        Show()
        Render()


class tetraedre:
    nbrCoordonne = 0
    name = ''

    def __init__(self, dirPath, iteratorFile):
        self.x_array = []
        self.y_array = []
        self.z_array = []
        print('iterateur ', iteratorFile)
        fichier = open(dirPath + str(iteratorFile) + "/micromesh.geo", "r")
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        self.name = ('Mesh ' + str(iteratorFile))
        print(self.name)
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        print('Coordonnee ' + lalignesuivante)
        self.nbrCoordonne = int(lalignesuivante)
        i = 0
        lalignesuivante = fichier.readline()
        while i < self.nbrCoordonne:
            self.x_array.append(float(lalignesuivante))
            print('x ', self.x_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0
        while i < self.nbrCoordonne:
            self.y_array.append(float(lalignesuivante))
            print('y ', self.y_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0
        while i < self.nbrCoordonne:
            self.z_array.append(float(lalignesuivante))
            print('z ', self.z_array[i])
            lalignesuivante = fichier.readline()
            i = i + 1
        i = 0

        fichier.close()





#class Grille:
    #Cellule=[][12][12]


"""def creer(self):
    for currentMesh in range(self.nbMesh):"""

dirPath = "C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/"

element3D = Element_3D(dirPath)
element3D.mesurer_Grille()
element3D.InsertGrid()
# element3D.mesurer_Grille()
