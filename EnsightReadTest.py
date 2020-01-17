from paraview.simple import *
#include <vtkCamera.h>
"""
cone = Cone()
print(cone.ListProperties())
Show()
"""

base ='C:\Users\Jules\Desktop\Paraview\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\'
"""
obj = EnSightReader(CaseFileName='C:\Users\Jules\Desktop\Paraview\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\MHMSolution.case')
Show()
"""


i=0
while (i<16):
    temp=EnSightReader(CaseFileName= base+'\'+str(i)+'\micromesh.case')
    i=i+1
    Show()
    Render()
temp.ListProperties()
j=1
t=FindSource('EnSightReader2')

Hide(t)
Render()

"""while (j<17):
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