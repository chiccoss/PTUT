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
        fichier = open("C:\\Users\\dietf\\OneDrive\\Bureau\\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\\"+str(iteratorFile)+"\\micromesh.geo","r")
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

def Plan(c,VALxyz,planVal,infOuSup): #planVar est égal à (x,y,z) ,planVar est la valeur par rapport à laquelle la cellule est testé ,infOuSup prend la valeur "inf" ou "sup"
    if(planVar=="x"):
        if(infOuSup=="inf"):
            i=0
            while(i<3):
                if(c.x_array[i]<planVal):
                    return true
                i+=1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.x_array[i] > planVal):
                    return true
                i += 1
    if (planVar == "y"):
        if (infOuSup == "inf"):
            i = 0
            while (i < 3):
                if (c.y_array[i] < planVal):
                    return true
                i += 1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.y_array[i] > planVal):
                    return true
                i += 1
    if (planVar == "z"):
        if (infOuSup == "inf"):
            i = 0
            while (i < 3):
                if (c.z_array[i] < planVal):
                    return true
                i += 1
        if (infOuSup == "sup"):
            i = 0
            while (i < 3):
                if (c.z_array[i] > planVal):
                    return true
                i += 1
    return false