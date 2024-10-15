from Servo import Servo

s1 = Servo(pin=8)

s1.move(0, 1000)
s1.move(90, 1000)
s1.move(180, 1000)
s1.move(90, 1000)

s1.end_operation()