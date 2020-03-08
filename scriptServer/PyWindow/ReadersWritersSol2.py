import threading
import os
from vtk import *
from paraview.simple import *


class ReaderWriterCallback:

    def __init__(self):
        self.camera = GetActiveCamera()
        self.mutex1 = threading.Lock()
        # print('hello mutex lock')
        self.data = "C:/Users/sohayb/scriptServer/thiIsTheFile.txt"
        self.timer_count = 0
        # print('hello after assigning data')
        # self.file = open(self.data)
        # print('hello from END init camera')
        # GetActiveView()

    def writer(self, obj, event):
        while True:
            print('hello from Writer')
            x = 0
            y = 0
            z = 0
            print("Inside Writer\n")
            with open(self.data, 'a') as the_file:
                the_file.write(str(self.camera.GetPosition()) + '\n')
            iren = obj
            # Render()
            # self.timer_count += 0.1
            print(self.timer_count)
            print(self.camera.GetPosition())
            self.camera.SetPosition(self.timer_count, self.timer_count, 0);
            iren = obj
            Render()
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
        global scene, rv, source
        ans = None
        try:
            ans = GetAnimationScene()
        except NameError:
            for i in servermanager.ProxyManager().GetProxiesInGroup("animation").values():
                if i.IsA("vtkSMAnimationSceneProxy"):
                    ans = i
                    break

        if ans:
            # Turn of caching so that we can get the bounds for the
            # data for each time step
            # ans.Caching = False
            scene = ans.GetClientSideObject()
            # Remove the previous observer.
            try:
                scene.RemoveObserver(callbackid)
            except NameError:
                pass

        rv = GetActiveView()

        if rv:
            # Add the observer to the VTK scene with priority 1 so that it happens before
            # anything else

            # Create a sphere
            sphere = Sphere()
            print("Made Sphere")
            camera = GetActiveCamera()
            print("Made GetActiveCamera Create fenetre vtk")
            # sphere.SetCenter(0.0, 0.0, 0.0)
            # sphere.SetRadius(5)
            Show(sphere)
            Render()
            CallBack = ReaderWriterCallback()
            CallBack.camera = camera
            callbackid = scene.AddObserver('TimerEvent', CallBack.writer, 1.0)
            timerId = scene.CreateRepeatingTimer(1000)

            # start the interaction and timer
            # renderWindowInteractor.Start()

            source = GetActiveSource()
            bds = source.GetDataInformation().GetBounds()
            # Center of bounds
            # first_bounds = map(lambda x, y: (x + y) / 2, bds[0:6:2], bds[1:6:2])
            # first_focal = rv.CameraFocalPoint[:]
            # first_pos = rv.CameraPosition[:]
            # view_up = rv.CameraViewUp[:]


# if __name__ == "__main__":
#  camera = vtkCamera()

Fen = FenetreVtk()  # (Camera=camera)
Fen.launchFenVtk()
print("Fenetre launched")
