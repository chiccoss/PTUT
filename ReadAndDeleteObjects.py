from paraview.simple import *
#include <vtkCamera.h>
import os
"""
cone = Cone()
print(cone.ListProperties())
Show()
"""

base ='C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'



onlyfiles = next(os.walk(base))[2] #dir is your directory path as string
#print len(onlyfiles)
#print num
list = os.listdir(base) # dir is your directory path
number_files = len(list)
#print number_files

try:
    num=number_files-len(onlyfiles)
    if num <= 0:
        raise ValueError()
except ValueError:
    print("Error while counting number of files")

#obj = EnSightReader(CaseFileName='C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/MHMSolution.case')
#Show()
#Render()

i=0
while (i<num):
    try:
        temp=EnSightReader(CaseFileName= base+'/'+str(i)+'/micromesh.case')
        i=i+1
    except OSError as e:
        print(e.errno) 
        print("File not found")
    
#temp.ListProperties()
#j=1
#t=FindSource('EnSightReader2')
#Show()
#Render()
#Hide(t)
#Render()
"""
while (j<17):
    t=FindSource('EnSightReader'+str(j))
    Delete(t)
    j=j+1
"""
camera=GetActiveCamera()
camera.SetPosition(49,0,0)
camera.SetViewAngle(1)
angle=camera.GetViewAngle()
position=camera.GetPosition()
print(angle)
print(position)
Render()

