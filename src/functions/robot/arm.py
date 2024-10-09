from .arduino import board
import time

class Servo:
    def __init__(self, pin):
        self.pin = board.get_pin(f'd:{pin}:s')

    def move(self, angle, delay=1):
        self.pin.write(angle)
        time.sleep(delay)
        return angle

servo_1 = Servo(pin=8)
servo_2 = Servo(pin=9)

servo_1.move(0)
servo_1.move(180)
servo_1.move(90) 
servo_2.move(0)

board.exit()