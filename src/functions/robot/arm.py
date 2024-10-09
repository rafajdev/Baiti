from .arduino import board
import time

class Servo:
    def __init__(self, pin):
        self.pin = board.get_pin(f'd:{pin}:s')

    def move(self, angle, delay=1):
        self.pin.write(angle)
        time.sleep(delay)
        return angle

s1 = Servo(pin=8)
s2 = Servo(pin=9)

s1.move(0)
s1.move(180)
s1.move(90) 
s2.move(0)

board.exit()