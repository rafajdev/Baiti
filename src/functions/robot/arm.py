from models.Servo import Servo

s1 = Servo(pin=8)

s1.move(0, 1.5)
s1.move(90, 1.5)
s1.move(180, 1.5) 

s1.end_operation()