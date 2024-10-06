import pyfirmata2
import time

port = 'COM5'
board = pyfirmata2.Arduino(port)
it = pyfirmata2.util.Iterator(board)
it.start()

buzzer_pin = board.get_pin('d:5:p')

def beep():
    buzzer_pin.write(0.5)
    time.sleep(0.5)
    buzzer_pin.write(0)
    board.exit()
