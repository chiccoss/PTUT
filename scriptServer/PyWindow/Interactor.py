# Our example needs the VTK Python package
import sys
import vtk
import os
import argparse


def print_camera_settings():
    camera = GetActiveCamera()
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
    if key == "t":
        camera = GetActiveCamera()
        camera.Setposition(0, 0, 0)
        Render()
    elif key == "s":
        camera = GetActiveCamera()
        camera.Setposition(12, 12, 0)
        Render()
    elif key == "p":
        print_camera_settings()
        Render()
    elif key == "q":
        if args.verbose:
            print("User requested exit.")
        Render()
        sys.exit()


def DummyFunc1(obj, ev):
    print("Before Event")


def main():
    s = Sphere()
    camera = GetActiveCamera()
    camera.AddObserver("KeyPressEvent", key_pressed_callback)
    camera.AddObserver('MiddleButtonPressEvent', DummyFunc1)
    print("Observer added")
    Show(s)
    Render()


main()
