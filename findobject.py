import sys
sys.path.append("C:/Users/sohayb/Documents/ParaView-5.4.1-Qt5-OpenGL2-Windows-64bit/bin/Lib/site-packages/paraview/simple.py")
from simple import *

Cone(guiName='MySuperCones')
Show()
Render()
myCone = FindSource('MySuperCones')
oggetto = FindSource('32')
CONO = FindSource('MySuperCones')
ExtractBlock(Slice(myCone))
print(0)
