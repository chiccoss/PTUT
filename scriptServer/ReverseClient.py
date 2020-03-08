from paraview.simple import *
import time
"""
s=Sphere()
Show(s)
#writer = XMLPPolyDataWriter(FileName='sphere.pvtp')
UpdatePipeline()

Render()

time.sleep(2.3)
"""

connect=servermanager.ReverseConnect("11111")
print("Waiting for server....")

Disconnect()