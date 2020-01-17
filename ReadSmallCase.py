from paraview.simple import *
#include <vtkCamera.h>
"""
cone = Cone()
print(cone.ListProperties())
Show()
"""
base ='C:\Users\Jules\Desktop\Paraview\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\'
obj = EnSightReader(CaseFileName='C:\Users\Jules\Desktop\Paraview\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\MHMSolution.case')
Show()
i=0
while (i<16):
    temp=EnSightReader(CaseFileName= base+'\0\micromesh.case')
    print(temp.PointArrays)
    i=i+1
camera=GetActiveCamera()
camera.SetPosition(49,0,0)
camera.SetViewAngle(1)
angle=camera.GetViewAngle()
position=camera.GetPosition()
print(angle)
print(position)
Render()