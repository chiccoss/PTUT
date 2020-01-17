from paraview.simple import *
#include <vtkCamera.h>
"""
cone = Cone()
print(cone.ListProperties())
Show()
"""

obj = EnSightReader(CaseFileName='C:\Users\Jules\Desktop\Paraview\tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3\MHMSolution.case')
Show()
print(obj.ListProperties())
print(obj)
camera=GetActiveCamera()
camera.SetPosition(49,0,0)
camera.SetViewAngle(1)
angle=camera.GetViewAngle()
position=camera.GetPosition()
print(angle)
print(position)
Render()