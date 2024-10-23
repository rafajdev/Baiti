from .Servo import Servo
from .RGBLed import RGBLed
from utils.json_handler import json_h
import pyfirmata2
import time

def use_board():
   try:
      board = pyfirmata2.Arduino(json_h.read('config')['arduino_board'])
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
        self.main_led.set_color_by_name("branco")
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
        
    def move_up(self):
        """Move the left servo up at a velocity of 3."""
        self.left.move(180, 4)
        
    def move_down(self):
        """Move the left servo down at a velocity of 6."""
        self.left.move(90, 6)
        
    def move_open(self):
        """Move the claw servo to open at a velocity of 3."""
        self.claw.move(90, 3)
        
    def move_close(self):
        """Move the claw servo to close at a velocity of 3."""
        self.claw.move(140, 4)
        
    def move_front(self):
        """Move the right servo front at a velocity of 5."""
        self.right.move(40, 5)
        
    def move_back(self):
        """Move the right servo back at a velocity of 3."""
        self.right.move(0, 4)
        
    def move_left(self):
        """Move the base servo left at a velocity of 5."""
        self.base.move(180, 5)
        
    def move_right(self):
        """Move the base servo right at a velocity of 5."""
        self.base.move(0, 5)
        
    def move_middle(self):
        """Move the base servo to the middle at a velocity of 5."""
        self.base.move(90, 5)

    def move_left_diagonal(self):
        self.base.move(135, 5)

    def move_right_diagonal(self):
        self.base.move(45, 5)
        
    def move_default(self):
        """Move all servos to their default angles at a velocity of 5."""
        self.base.move(self.base_init_angle, 5)
        self.right.move(self.right_init_angle, 5)
        self.left.move(self.left_init_angle, 5)
        self.claw.move(self.claw_init_angle, 5)

    def end_operation(self):
        """
        End the operation by exiting the board connection.
        """
        self.board.exit()