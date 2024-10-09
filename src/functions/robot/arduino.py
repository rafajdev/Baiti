import pyfirmata2

try:
   board = pyfirmata2.Arduino('/dev/ttyACM0')
except Exception as e:
   print(f"Ocorreu um erro inesperado: {e}")
