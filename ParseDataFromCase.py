#from paraview.simple import *
from array import *

def test_Choice_Int(i_number):
    assert isinstance(i_number, list)

class Cellule:
    nbrCoordonne = 0
    name=''
    x_array = array('d')
    y_array = array('d')
    z_array = array('d')
    def init(self, iteratorFile):

        fichier = open("C:\Users\dietf\OneDrive\Bureau\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\MHMSolution.geo","r")
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        lalignesuivante = fichier.readline()
        self.name = lalignesuivante
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
            print('x ', self.y_array[i])
            lalignesuivante = fichier.readline()

            self.z_array.append(float(lalignesuivante))
            print('x ', self.z_array[i])
            i += 1

        #print(fichier.read())
        fichier.close()


    def getCoordonne(self):
        return self.coo

    def getNombreCoordonne(self):
        print ("Il y a", self.nbrCoordonne, "personnes!")


#class Elemet_3D:
 #   def init(self):

p1 = Cellule(0)
print ('name ' + p1.name)
print ('nbr coordonne ' , p1.nbrCoordonne)