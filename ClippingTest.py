import paraview.simple as prw

base ='C:\\Users\Alexis\\Desktop\\ParaviewData\\tree3D_elastodyn.2.2'

camera = prw.GetActiveCamera()
camAngle = camera.GetViewAngle()
camPos = camera.GetPosition()
print("Angle camera: %d", camAngle)
print("Position camera: %d", camPos)

cells = {}

for i in range(0,18):
    cells[i] = EnSightReader(CaseFileName= base + '\\' + str(i) + '\\micromesh.case')
    print(cells[i].PointArrays)
    Show()
Render()

# ClipType: type du clip {'Plane','Box','Sphere','Scalar'}
"""
clipBox = prw.Clip(Input=data,ClipType='Box')
clipBox.ClipType.Position = camera.GetPosition()
clipBox.ClipType.Length = [1.0, 1.0, 1.0]
clipBox.Invert = 0
clipBox.Crinkleclip = 0
"""

# def deleteAll(cells):




# Show(clipBox)
# Hide(data)
# Render()