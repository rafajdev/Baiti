from arduino import use_board
import time

class Servo:
   """
   Servo motor control class
   
   Parameters
   ----------
   pin: int
      The pin number to which the servo is connected
   """
   def __init__(self, pin, initialAng = 0):
      self.pin = use_board().get_pin(f'd:{pin}:s')
      self.currentAng = initialAng

   def move(self, angle, vel):
      if angle < 0 or angle > 180:
         raise ValueError('Angle must be between 0 and 180 degrees')
      
      step =  1 if angle > currentAng else -1
      
      while currentAng != angle:
         currentAng += step
         self.pin.write(currentAng)
         time.sleep(vel/1000) 
      
   def end_operation(self):
      """
      Exit the board
      """
      use_board().exit()
      return 0