from interaction.speech import *
from utils.json_handler import json_h

def led_on_talk(element):
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