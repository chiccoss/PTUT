import vtk


class vtkTimerCallback():
    def __init__(self):
        self.timer_count = 0

    def WriteInFile(self, obj, event):
        # print(self.timer_count)
        # print(self.actor.GetPosition())
        print("From Write File")
        with open("C:/Users/sohayb/scriptServer/thiIsTheFile.txt", 'a') as f:
            f.write(str(self.actor.GetPosition()) + '\n')
        # iren = obj
        # iren.GetRenderWindow().Render()
        # self.timer_count += 0.1

    def PrintOnScreen(self, obj, event):
        # print(self.timer_count)
        print("From PrintOnScreen")
        print(self.actor.GetPosition())
        # print(self.actor.GetPosition())
        # iren = obj
        # iren.GetRenderWindow().Render()
        # self.timer_count += 0.1

    def SetPosi(self, obj, event):
        print("From SetPosi")
        print(self.timer_count)
        # print(self.actor.GetPosition())
        self.actor.SetPosition(self.timer_count, self.timer_count, 0)
        iren = obj
        iren.GetRenderWindow().Render()
        self.timer_count += 0.1


def main():
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
    renderWindow = vtk.vtkRenderWindow()
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
    cb = vtkTimerCallback()
    cb.actor = actor
    # renderWindowInteractor.AddObserver('TimerEvent', cb.PrintOnScreen, 3)
    renderWindowInteractor.AddObserver('Mouse', cb.WriteInFile)
    renderWindowInteractor.AddObserver('TimerEvent', cb.SetPosi)
    # timerId = renderWindowInteractor.CreateRepeatingTimer(1000)  # in ms

    # start the interaction and timer
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
