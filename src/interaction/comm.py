from .config import apiConfig
from .speech import *
from .switcher import switch
from .json_handler import json_h

def init(): 

      chat = apiConfig()
      speak(json_h.read('standard_messages')['greetings']['pt-BR'])
      
      while True:
         user_response = listen()
         algorithm_response = switch(user_response)

         print(algorithm_response) # Print para visualização (lembrar de apagar depois)
         if algorithm_response == 'comp_error' or algorithm_response == 'pass':
            continue
         elif algorithm_response == 'exit':
            break
         else:
            chat_response = chat.send_message(algorithm_response)
            speak(chat_response.text)
            
            # json_h.add_to_history('user', user_response)
            # json_h.add_to_history('model', chat_response.text)