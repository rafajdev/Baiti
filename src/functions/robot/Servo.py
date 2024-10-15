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
   def __init__(self, pin):
      self.pin = use_board().get_pin(f'd:{pin}:s')

   def move(self, angle, delay=1):
      """
      Move the servo to a specific angle

      Parameters
      ----------
      angle: int (0-180)
         The angle to which the servo should be moved
      delay: float
         The time to wait before releasing the servo
      Returns
         The angle: int (The angle to which the servo was moved)
      """
      
      if angle < 0 or angle > 180:
         raise ValueError('Angle must be between 0 and 180 degrees')
      
      self.pin.write(angle)
      time.sleep(delay)
      return angle
      
   def end_operation(self):
      """
      Exit the board
      """
      use_board().exit()
      return 0
