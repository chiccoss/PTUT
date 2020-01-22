# from paraview.simple import *
# include <vtkCamera.h>
import os

"""
cone = Cone()
print(cone.ListProperties())
Show()
"""
"""
import os
base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'

onlyfiles = next(os.walk(base))[2]  # dir is your directory path as string
number = len(onlyfiles) #nombre de fichier sans les dossiers dans le dossier
print(number)

list= os.listdir(base)  # dir is your directory path
number_files = len(list)
print(number_files) #nombre total de touts les types de fichiers dans le dossier

num=number_files-number

print(num) #number of .case

try:
    num = number_files - len(onlyfiles)
    if num <= 0:
        raise ValueError()
except ValueError:
    print("Error while counting number of files")
"""
# obj = EnSightReader(CaseFileName='C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/MHMSolution.case')
# Show()
# Render()

i = 0
"""
while (i < num):
    try:
        temp = EnSightReader(CaseFileName=base + '/' + str(i) + '/micromesh.case')
        i = i + 1
    except OSError as e:
        print(e.errno)
        print("File not found")

# temp.ListProperties()
# j=1
# t=FindSource('EnSightReader2')
# Show()
# Render()
# Hide(t)
# Render()

"""
"""
while (j<17):
    t=FindSource('EnSightReader'+str(j))
    Delete(t)
    j=j+1
"""

"""
camera = GetActiveCamera()
camera.SetPosition(49, 0, 0)
camera.SetViewAngle(1)
angle = camera.GetViewAngle()
position = camera.GetPosition()
print(angle)
print(position)
Render()
"""



class Cellule:
    nbrCoordonne = 0
    name=''
    x_array = []
    y_array = []
    z_array = []
    def __init__(self, iteratorFile):
        self.x_array.clear()
        self.y_array.clear()
        self.z_array.clear()

        print('iterateur ',iteratorFile)
        fichier = open('C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'+str(iteratorFile)+'/micromesh.geo','r')
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
        while i < 9:
            lalignesuivante = fichier.readline()
            if i <3:
                self.x_array.append(float(lalignesuivante))
                print('x ', self.x_array[i%3])
            if i>=3 and i<6:
                self.y_array.append(float(lalignesuivante))
                print('y ', self.y_array[i%3])
            if i>=6:
                self.z_array.append(float(lalignesuivante))
                print('z ', self.z_array[i%3])
            i += 1

        fichier.close()

def Plan(c,planVar,planVal,infOuSup): #planVar est égal à (x,y,z) ,planVal est la valeur par rapport à laquelle la cellule est testé ,infOuSup prend la valeur "inf" ou "sup"
    if(planVar=="x"):
        if(infOuSup=="inf"):
            i=0
            while(i<3):
                if(c.x_array[i]<planVal):
                    return True
                i+=1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.x_array[i] > planVal):
                    return True
                i += 1
    if (planVar == "y"):
        if (infOuSup == "inf"):
            i = 0
            while (i < 3):
                if (c.y_array[i] < planVal):
                    return True
                i += 1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.y_array[i] > planVal):
                    return True
                i += 1
    if (planVar == "z"):
        if (infOuSup == "inf"):
            i = 0
            while (i < 3):
                if (c.z_array[i] < planVal):
                    return True
                i += 1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.z_array[i] > planVal):
                    return True
                i += 1
    return False

c=Cellule(3)
print(Plan(c,"z",-1,"sup"))







