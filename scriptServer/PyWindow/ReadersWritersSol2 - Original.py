import threading
import os
from vtk import *
# from paraview.simple import *

class ReaderWriterCallback:

    def __init__(self):
        # self.camera = GetActiveCamera()
        self.mutex1 = threading.Lock()
        # print('hello mutex lock')
        self.data = "C:/Users/sohayb/scriptServer/thiIsTheFile.txt"
        self.timer_count = 0
        # print('hello after assigning data')
        # self.file = open(self.data)
        # print('hello from END init camera')
        # GetActiveView()

    def writer(self, obj, event):
        print('hello from Writer')
        x = 0
        y = 0
        z = 0
        print("Inside Writer\n")
        with open(self.data, 'a') as the_file:
            the_file.write(str(self.actor.GetPosition()) + '\n')
        iren = obj
        iren.GetRenderWindow().Render()
        # self.timer_count += 0.1
        print(self.timer_count)
        print(self.actor.GetPosition())
        self.actor.SetPosition(self.timer_count, self.timer_count, 0);
        iren = obj
        iren.GetRenderWindow().Render()
        self.timer_count += 0.1

    def reader(self):
        #  i in range(20):
        print("Inside Reader" + str(i))
        self.mutex1.acquire()
        print("Coordinates At Position " + str(i))
        print(threading.current_thread())
        with open(self.data) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
        # self.file = open(self.data, "r")
        # print(self.file.read())
        print('\n')
        fp.close()
        # Test if var getted are equal to the precedent
        # If yes don t do nothing
        # else delete everything in the scene and ensight reader every thing that is not
        # time sleep to give time to the program to render()
        self.mutex1.release()

    # s=Sphere()
    # Show(s)
    # writer = XMLPPolyDataWriter(FileName='sphere.pvtp')
    # UpdatePipeline()
    # Render()
    # base = 'C:/Users/sohayb/Desktop/tree2D_advection_f1sigma0_1e-2_ccross_2_subelems0001_subfaces00_L1_K3/'

    # i=0
    # while (i<num):
    # temp=EnSightReader(CaseFileName= base+'/'+str(i)+'/micromesh.case')
    # i=i+1
    # Show(temp)
    # Render()

    # self.camera = Camera
    # , Camera):


class FenetreVtk:

    def launchFenVtk(self):
        # Create a sphere
        sphereSource = vtk.vtkSphereSource()
        sphereSource.SetCenter(0.0, 0.0, 0.0)
        sphereSource.SetRadius(5)

        # Create a mapper and actor
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphereSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        prop = actor.GetProperty()

        # Setup a renderer, render window, and interactor
        renderer = vtk.vtkRenderer()
        renderWindow =  vtk.vtkRenderWindow()# GetActiveView()
        # renderWindow.SetWindowName("Test")

        renderWindow.AddRenderer(renderer)
        renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        renderWindowInteractor.SetRenderWindow(renderWindow)

        # Add the actor to the scene
        renderer.AddActor(actor)
        renderer.SetBackground(1, 1, 1)  # Background color white

        # Render and interact
        renderWindow.Render()

        # Initialize must be called prior to creating timer events.
        renderWindowInteractor.Initialize()

        # Sign up to receive TimerEvent
        cb = ReaderWriterCallback()
        cb.actor = actor
        renderWindowInteractor.AddObserver('TimerEvent', cb.writer)
        # timerId = renderWindowInteractor.CreateRepeatingTimer(100)

        # start the interaction and timer
        renderWindowInteractor.Start()


if __name__ == "__main__":
    #  camera = vtkCamera()

    Fen = FenetreVtk()  # (Camera=camera)
    Fen.launchFenVtk()


