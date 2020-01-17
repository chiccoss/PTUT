from paraview.simple import *
#include <vtkCamera.h>

cone = Cone()
Show()

camera=GetActiveCamera()
camera.SetPosition(10,0,0)
camera.SetViewAngle(0)
angle=camera.GetViewAngle()
position=camera.GetPosition()
print(angle)
print(position)
Render()

"""
//list properties
cone.ListProperties()
cone.Propriete1
"""