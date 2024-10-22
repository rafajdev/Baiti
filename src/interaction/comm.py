from .config import apiConfig
from .speech import *
from .switcher import switch
from .json_handler import json_h

def init():
   chat = apiConfig()
   speak(json_h.read('standard_messages')['greetings']['pt-BR'])
   user_history = []
   model_history = []

   while True:
      user_response = listen()
      algorithm_response = switch(user_response)

      if algorithm_response == 'exit':
         break
      elif algorithm_response == 'comp_error' or algorithm_response == 'pass':
         continue
      
      user_history.append(user_response)
      chat_response = chat.send_message(algorithm_response)
      model_history.append(chat_response.text)
      speak(chat_response.text)

   # json_h.add_to_history('user', user_history)
   # json_h.add_to_history('model', model_history)
