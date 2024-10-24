from .speech import *
from utils.json_handler import json_h
from functions.robot import control 
from functions.camera.control import cam_request
from functions.catcher import catch
from functions.robot.control_led import led_on_talk

def switch(value: str):
   if value is None:
      return 'comp_error'
   text = value.lower()

   switch_map = {
      # help command
      'ajuda': lambda: speak(json_h.read('standard_messages')['help']['pt-BR']),
      
      # test commands
      'eita': lambda: speak('eita'),
      'piano': lambda: speak('another one bites the dust'),
      'teste': lambda: (speak('executando o braço'), control.arm.testing()),
      
      # led commands
      'acender led': lambda: (speak('qual cor deseja que o led acenda?'), led_on_talk(control.arm.main_led)),
      'acender le': lambda: (speak('qual cor deseja que o led acenda?'), led_on_talk(control.arm.main_led)),
      'acender luz': lambda: (speak('qual cor deseja que o led acenda?'), led_on_talk(control.arm.main_led)),
      'apagar le': lambda: (speak('apagando o led'), control.arm.main_led.off(), speak('o que deseja fazer agora?')),
      'apagar led': lambda: (speak('apagando o led!'), control.arm.main_led.off(), speak('o que deseja fazer agora?')),
      
      # arm commands
      'esquerda': lambda: control.arm.move_left(),
      'direita': lambda: control.arm.move_right(),
      'diagonal esquerda': lambda: control.arm.move_left_diagonal(),
      'diagonal direita': lambda: control.arm.move_right_diagonal(),
      'frente': lambda: control.arm.move_front(),
      'atras': lambda: control.arm.move_back(),
      'atrás': lambda: control.arm.move_back(),
      'cima': lambda: control.arm.move_up(),
      'baixo': lambda: control.arm.move_down(),
      'meio': lambda: control.arm.move_middle(),
      'abrir garra': lambda: control.arm.move_open(),
      'fechar garra': lambda: control.arm.move_close(),      
      'voltar ao normal': lambda: control.arm.move_default(),
      'voltar normal': lambda: control.arm.move_default(),
      
      # camera commands
      'modo câmera': lambda: (cam_request(), speak('o que deseja fazer agora?')),
      'modo bloco': lambda: (catch.start(), speak('O que deseja fazer agora?')),
      'modo blo': lambda: (catch.start(), speak('O que deseja fazer agora?')),
      'Monobloco': lambda: (catch.start(), speak('O que deseja fazer agora?')),
            
      # end command
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