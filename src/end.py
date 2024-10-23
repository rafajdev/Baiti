from functions.robot.control import arm
from functions.camera.control import cam

def finale():
    arm.end_operation()
    cam.release() 
    