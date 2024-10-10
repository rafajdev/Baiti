from functions.robot.arduino import board
import time

class Servo:
   def __init__(self, pin):
      self.pin = board.get_pin(f'd:{pin}:s')

   def move(self, angle, delay=1):
      self.pin.write(angle)
      time.sleep(delay)
      return angle
   def end_operation(self):
      board.exit()
      return 0