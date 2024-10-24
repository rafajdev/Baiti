from interaction.speech import *
from utils.json_handler import json_h

def led_on_talk(element):
   """
   Listen for user voice input and set the RGB LED color accordingly.

   This function listens for user voice input, attempts to set the RGB LED color
   based on the user's response, and returns a status code based on the result.

   Parameters
   ----------
   element : RGBLed
       The RGB LED object to control.

   Returns
   -------
   str
       Either 'pass' if the color was set successfully, or 'comp_error' if there was an error
       setting the color.
   """
   user_response = listen()
   
   if user_response is None:
      return 'comp_error'
   result = element.set_color_by_name(user_response)

   if result == 'color_error':
      speak(json_h.read('standard_messages')['error']['pt-BR'])
      return 'pass'
   else:
      speak("Led acendido! O que deseja fazer agora?")
      return 'pass'