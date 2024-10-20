import time

class Servo:
   """
   Servo motor control class
   
   Parameters
   ----------
   pin: int
      The pin number to which the servo is connected
   """
   def __init__(self, pin, board):
      self.board = board
      self.pin = self.board.get_pin(f'd:{pin}:s')

   def move(self, angle, vel):
      if angle < 0 or angle > 180:
         raise ValueError('Angle must be between 0 and 180 degrees')
      
      currentAng = self.pin.read()
      step =  1 if angle > currentAng else -1
      
      while currentAng != angle:
         currentAng += step
         self.pin.write(currentAng)
         time.sleep(vel/1000) 
      
      print(currentAng)
      
   def end_operation(self):
      """
      Exit the board
      """
      self.board.exit()
      return 0