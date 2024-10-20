from .config import apiConfig
from .speech import *
from .switcher import switch
from .json_handler import json_h

def init(): 
   try:
      chat = apiConfig()
      speak(json_h.read('standard_messages')['greetings']['pt-BR'])
      
      while True:
         user_response = listen()
         algorithm_response = switch(user_response)

         print(algorithm_response)

         if algorithm_response == 'comp_error' or algorithm_response == 'pass':
            continue
         elif algorithm_response == 'exit':
            break
         else:
            chat_response = chat.send_message(algorithm_response)
            speak(chat_response.text)
   except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}") # Fazer isto aparecer no display com um icone