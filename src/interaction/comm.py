from .config import apiConfig
from .speech import *
from .switcher import switch
from utils.json_handler import json_h
from end import finale

def init():
   API = apiConfig()
   chat = API[0]
   
   user_history = []
   model_history = []
   
   speak(json_h.read('standard_messages')['greetings']['pt-BR'])
   
   while True:
      user_response = listen()
      algorithm_response = switch(user_response)

      if algorithm_response == 'exit':
         finale()
         break
      elif algorithm_response == 'comp_error' or algorithm_response == 'pass':
         continue
      
      chat_response = chat.send_message(algorithm_response)
      
      user_history.append(user_response)
      model_history.append(chat_response.text)
      
      print(chat_response.text)
      speak(chat_response.text)

   #  json_h.add_to_history('user', user_history)
   #  json_h.add_to_history('model', model_history)