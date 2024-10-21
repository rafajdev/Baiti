from .Servo import Servo
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
    """
    This class represents an arm with multiple servos for controlling different parts.
    """
    def __init__(self):
        """
        Initialize the arm with servos for various components.
        """
        self.board = use_board()
        self.right = Servo(1, self.board, 0)
        self.claw = Servo(2, self.board, 140)
        self.base = Servo(4, self.board, 90)
        self.left = Servo(3, self.board, 90)

    def testing(self):
        """
        Perform a testing routine for the arm by moving different servos to predefined positions.
        """
        self.base.move(90, 10)
        self.claw.move(140, 10)
        self.right.move(20, 10)
        self.left.move(170, 10)
        self.test.move(90, 10)
        time.sleep(0.5)
        self.base.move(0, 10)
        self.claw.move(110, 10)
        self.test.move(0, 10)

    def _printf(self):
        print("Oi")

    def end_operation(self):
        """
        End the operation by exiting the board connection.
        """
        self.board.exit()