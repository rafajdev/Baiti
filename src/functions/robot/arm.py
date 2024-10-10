from models.Servo import Servo

s1 = Servo(pin=8)
s2 = Servo(pin=9)

s1.move(0, 1.5)
s1.move(90, 1.5)
s1.move(180, 1.5) 
s2.move(90, 1.5)

s1.end_operation()
s2.end_operation()