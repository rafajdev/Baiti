from Servo import Servo
import pyfirmata2
import time

def use_board():
   try:
      board = pyfirmata2.Arduino('/dev/ttyUSB0')
      return board
   except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")
      return None

class Arm:
   def __init__(self):
      self.board = use_board()
      self.base = Servo(2, self.board)
      self.claw = Servo(3, self.board)
      self.right = Servo(4, self.board)
      self.left = Servo(5, self.board)
      self.test = Servo(6, self.board)
      
   def testing(self):
      self.base.move(90, 10)
      self.claw.move(140, 10)
      self.right.move(20, 10)
      self.left.move(170, 10)
      self.test.move(90, 10)
      time.sleep(0.5)
      self.base.move(0, 10)
      self.claw.move(110, 10)
      self.test.move(0, 10)
      
   def printf(self):
      print("Oi")

   def end_operation(self):
      self.board.exit()

      
# Remember to Initialize the servos on start of the program, cuz theyll flick only once