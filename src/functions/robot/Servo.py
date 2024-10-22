import time

class Servo:
   """
   A class used to represent a Servo motor
   
   Attributes
   ----------
   pin : int
      The pin where the servo is connected
   board : pyfirmata2.Arduino
      The board where the servo is connected
   initAngle : int
      The initial angle of the servo
   """

   def __init__(self, pin: int, board, initAngle: int):
      """
      Parameters
      ----------
      pin : int
         The pin where the servo is connected
      board : pyfirmata2.Arduino
         The board where the servo is connected
      initAngle : int
         The initial angle of the servo
      """
      self.board = board
      self.initAngle = initAngle
      self.pin = self.board.get_pin(f'd:{pin}:s')
      self.pin.write(self.initAngle)      
      

   def move(self, angle: int, vel: int):
      """
      Move the servo to the given angle with the given velocity
      
      Parameters
      ----------
      angle : int
         The angle to move the servo to
      vel : int
         The velocity of the servo
      """
      if angle < 0 or angle > 180:
         raise ValueError('Angle must be between 0 and 180 degrees')
      
      currentAng = self.pin.read()
      step =  1 if angle > currentAng else -1
      
      while currentAng != angle:
         currentAng += step
         self.pin.write(currentAng)
         time.sleep(vel/1000) 
      
      print(currentAng) # Remover depois
      
   def end_operation(self):
      """
      Ends the servo operation
      """
      self.board.exit()
      return 0

