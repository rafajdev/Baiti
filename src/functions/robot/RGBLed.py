import time
class RGBLed:
    """
    Class for controlling the RGB LED light

    Attributes
    ----------
    red_pin : int
        The pin to which the red pin is connected
    green_pin : int
        The pin to which the green pin is connected
    blue_pin : int
        The pin to which the blue pin is connected
    board : pyfirmata2.Arduino
        The board to which the LED is connected

    Methods
    -------
    on(red, green, blue) : None
        Turn the LED on with the specified red, green, and blue values
    off() : None
        Turn the LED off
    blink(red, green, blue, times, delay) : None
        Blink the LED the specified number of times with the specified delay
    """
    import time

class RGBLed:
    def __init__(self, red_pin, green_pin, blue_pin, board):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.board = board
        self.red_led_pin = self.board.get_pin(f'd:{red_pin}:o')
        self.green_led_pin = self.board.get_pin(f'd:{green_pin}:o')
        self.blue_led_pin = self.board.get_pin(f'd:{blue_pin}:o')
    
    def set_color(self, red, green, blue):
        self.red_led_pin.write(red)
        self.green_led_pin.write(green)
        self.blue_led_pin.write(blue)
    
    def off(self):
        self.set_color(0, 0, 0)
    
    def set_color_by_name(self, color):
        colors = {
            'vermelho': (1, 0, 0),
            'verde': (0, 1, 0),
            'azul': (0, 0, 1),
            'amarelo': (1, 1, 0),
            'magenta': (1, 0, 1),
            'ciano': (0, 1, 1),
            'branco': (1, 1, 1)
        }
        
        if color.lower() in colors:
            self.set_color(*colors[color.lower()])
            return 'pass'
        else:
            return 'color_error'
    
    def blink(self, red, green, blue, times, delay):
        for _ in range(times):
            self.set_color(red, green, blue)
            time.sleep(delay)
            self.off()
            time.sleep(delay)