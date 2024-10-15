import pyfirmata2

def use_board():
   try:
      board = pyfirmata2.Arduino('/dev/ttyACM1')
      return board
   except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")
      return None
      
