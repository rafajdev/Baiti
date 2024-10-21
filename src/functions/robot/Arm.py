from .Servo import Servo
from .RGBLed import RGBLed
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
        
        self.right_init_angle = 0
        self.claw_init_angle = 140
        self.base_init_angle = 90
        self.left_init_angle = 90
        
        self.right = Servo(2, self.board, self.right_init_angle)
        self.claw = Servo(3, self.board, self.claw_init_angle)
        self.base = Servo(4, self.board, self.base_init_angle)
        self.left = Servo(5, self.board, self.left_init_angle)
        
        self.main_led = RGBLed(9, 10, 11, self.board)

    def testing(self):
        """
        Perform a testing routine for the arm by moving different servos to predefined positions.
        """
        self.main_led.on(1, 1, 1)
        self.base.move(0, 5)
        self.claw.move(0, 5)
        time.sleep(0.5)
        self.right.move(30, 8)
        self.left.move(170, 8)
        self.claw.move(150, 5)
        time.sleep(0.5)
        self.right.move(self.right_init_angle, 5)
        self.base.move(self.base_init_angle, 5)
        time.sleep(0.75)
        self.claw.move(100, 5)
        time.sleep(0.5)
        self.right.move(30, 8)
        self.left.move(150, 8)
        time.sleep(0.25)
        self.right.move(self.right_init_angle, 5)
        self.left.move(self.left_init_angle, 5)
        self.claw.move(self.claw_init_angle, 5)
        self.main_led.off()
        

    def _printf(self):
        print("Oi")

    def end_operation(self):
        """
        End the operation by exiting the board connection.
        """
        self.board.exit()