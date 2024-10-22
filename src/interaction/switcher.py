from .speech import *
from utils.json_handler import json_h
from functions.robot import control

def switch(value: str):
   if value is None:
      return 'comp_error'
   text = value.lower()

   switch_map = {
      'ajuda': lambda: speak(json_h.read('standard_messages')['help']['pt-BR']),
      'eita': lambda: speak('eita'),
      'piano': lambda: speak('another one bites the dust'),
      'teste': lambda: (speak('executando o braço'), control.arm.testing()),
      'acender led': lambda: (speak('qual cor deseja que o led acenda?'), led_on_talk(control.arm.main_led)),
      'apagar led': lambda: (speak('apagando o led!'), control.arm.main_led.off(), speak('o que deseja fazer agora?')),
      'encerrar': lambda: 'exit'
   }

   action = switch_map.get(text)

   if action:
      result = action()
      if result == 'exit':
         speak('Certo, Até logo!')
         return result
      else:
         return 'pass'
   else:
      return text

def led_on_talk(element):
   user_response = listen()
   result = element.set_color_by_name(user_response)

   if result == 'color_error':
      speak(json_h.read('standard_messages')['error']['pt-BR'])
      return 'pass'
   else:
      speak("Led acendido! O que deseja fazer agora?")
      return 'pass'
