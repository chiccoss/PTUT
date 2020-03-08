# Our example needs the VTK Python package
import sys
import vtk
import os
import argparse

frame_counter = 0


def make_sphere():
    global renderer
    # ---------------------------------------------------------------
    # The following code is identical to render_demo.py...
    # ---------------------------------------------------------------
    # create a sphere
    sphere_src = vtk.vtkSphereSource()
    sphere_src.SetRadius(1.0)
    sphere_src.SetCenter(0.0, 0.0, 0.0)
    sphere_src.SetThetaResolution(20)
    sphere_src.SetPhiResolution(20)
    # extract the edges
    edge_extractor = vtk.vtkExtractEdges()
    edge_extractor.SetInputConnection(sphere_src.GetOutputPort())
    # map sphere and edges separately
    sphere_mapper = vtk.vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere_src.GetOutputPort())
    edge_mapper = vtk.vtkPolyDataMapper()
    edge_mapper.SetInputConnection(edge_extractor.GetOutputPort())
    # define different rendering styles for sphere and edges
    sphere_actor = vtk.vtkActor()
    sphere_actor.SetMapper(sphere_mapper)
    sphere_actor.GetProperty().SetColor(1, 0.5, 0)
    edge_actor = vtk.vtkActor()
    edge_actor.SetMapper(edge_mapper)
    edge_actor.GetProperty().SetColor(0, 0.5, 0)
    edge_actor.GetProperty().SetLineWidth(3)
    # add resulting primitives to renderer
    renderer.AddActor(sphere_actor)
    renderer.AddActor(edge_actor)


def save_frame():
    global frame_counter
    global window
    global args
    # ---------------------------------------------------------------
    # Save current contents of render window to PNG file
    # ---------------------------------------------------------------
    file_name = args.output + str(frame_counter).zfill(5) + ".png"
    image = vtk.vtkWindowToImageFilter()
    image.SetInput(window)
    png_writer = vtk.vtkPNGWriter()
    png_writer.SetInputConnection(image.GetOutputPort())
    png_writer.SetFileName(file_name)
    window.Render()
    png_writer.Write()
    frame_counter += 1
    if args.verbose:
        print(file_name + " has been successfully exported")


def print_camera_settings():
    global renderer
    # ---------------------------------------------------------------
    # Print out the current settings of the camera
    # ---------------------------------------------------------------
    camera = renderer.GetActiveCamera()
    print("Camera settings:")
    print("  * position:        %s" % (camera.GetPosition(),))
    print("  * focal point:     %s" % (camera.GetFocalPoint(),))
    print("  * up vector:       %s" % (camera.GetViewUp(),))
    print("  * clipping range:  %s" % (camera.GetClippingRange(),))


def key_pressed_callback(obj, event):
    global args
    # ---------------------------------------------------------------
    # Attach actions to specific keys
    # -------------------------------------------------------------------
    key = obj.GetKeySym()
    if key == "s":
        save_frame()
    elif key == "c":
        print_camera_settings()
    elif key == "q":
        if args.verbose:
            print("User requested exit.")
        sys.exit()


def main():
    # global renderer
    global window
    global args
    global renderer

    parser = argparse.ArgumentParser(
        description='Illustrate the use of vtkRenderWindowInteractor')
    parser.add_argument('-r', '--resolution', type=int, metavar='int', nargs=2, help='Image resolution',
                        default=[1024, 768])
    parser.add_argument('-b', '--background', type=int, metavar='int', nargs=3, help='Background color',
                        default=[0, 0, 0])
    parser.add_argument('-o', '--output', type=str, metavar='filename', help='Base name for screenshots',
                        default='frame_')
    parser.add_argument('-v', '--verbose', action='store_true', help='Toggle on verbose output')

    args = parser.parse_args()

    renderer = vtk.vtkRenderer()
    print('background color={}'.format(args.background))
    renderer.SetBackground(args.background[0], args.background[1], args.background[2])
    make_sphere()
    renderer.ResetCamera()

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    print('resolution={}'.format(args.resolution))
    window.SetSize(args.resolution)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)

    # ---------------------------------------------------------------
    # Add a custom callback function to the interactor
    # ---------------------------------------------------------------
    interactor.AddObserver("KeyPressEvent", key_pressed_callback)

    interactor.Initialize()
    window.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
