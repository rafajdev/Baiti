import pyfirmata2
import time

def beep():
   board = pyfirmata2.Arduino('COM5')
   
   pin_buzzer = board.digital[13]
   
   pin_buzzer.write(1)
   time.sleep(0.5)
   pin_buzzer.write(0)
   board.exit()