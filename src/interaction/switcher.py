from .speech import *
from .json_handler import json_h
from functions.robot import control

help_message = json_h.read('standard_messages')['help']['pt-BR']

def switch(value):
   if value is None:
      speak(json_h.read('standard_messages')['listening error']['pt-BR'])
      return 'comp_error'
   else:
      text = value.lower()
      
      if text == 'ajuda':
         speak(help_message)
         return 'pass'
      elif text == 'eita':
         speak('eita')
         return 'pass'
      elif text == 'piano':      
         speak('another one bites the dust')
         return 'pass'
      elif text == 'teste':
         speak('executando o braço')
         control.arm.testing()
         return 'pass'
      elif text == 'acender led':
         speak('Qual cor deseja que o led acenda?')
         user_response = listen()
         control.arm.main_led.on_talk(user_response)
         return 'pass'
      elif text == 'apagar led':
         speak('Apagando o led!')
         control.arm.main_led.off()
         return 'pass'
      elif text == 'encerrar':
         speak('Certo, até mais!')
         return 'exit'
      else:
         return text