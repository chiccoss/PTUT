# from paraview.simple import *
from array import *
import os


def test_Choice_Int(i_number):
    assert isinstance(i_number, list)


class Cellule:
    nbrCoordonne = 0
    name = ''
    x_array = []
    y_array = []
    z_array = []

    def __init__(self, iteratorFile):
        self.x_array.clear()
        self.y_array.clear()
        self.z_array.clear()

        print('iterateur ', iteratorFile)
        fichier = open(
            "C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/" + str(
                iteratorFile) + "/micromesh.geo", "r")
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
        print('Coordonnée ' + lalignesuivante)
        self.nbrCoordonne = int(lalignesuivante)
        i = 0
        while i < 3:
            lalignesuivante = fichier.readline()

            self.x_array.append(float(lalignesuivante))
            print('x ', self.x_array[i])
            lalignesuivante = fichier.readline()

            self.y_array.append(float(lalignesuivante))
            print('y ', self.y_array[i])
            lalignesuivante = fichier.readline()

            self.z_array.append(float(lalignesuivante))
            print('z ', self.z_array[i])
            i += 1

        fichier.close()

    def getNombreCoordonne(self):
        print("Il y a ", self.nbrCoordonne, " personnes!")


class Element_3D:
    liste = []

    def __init__(self,base):
        onlyfiles = next(os.walk(base))[2]  # dir is your directory path as string
        number=len(onlyfiles)  # nombre de fichier sans les dossiers dans le dossier

        allFiles = os.listdir(base)  # dir is your directory path
        number_files = len(allFiles)
        num = number_files - number

        i = 0
        while i < num:
            c = Cellule(i)
            self.liste.append(c)
            i = i + 1




e1 = Element_3D(base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/')

print("cou" + "cou")
print("cou", e1.liste[2].name)
print("cou", e1.liste[6].name)


