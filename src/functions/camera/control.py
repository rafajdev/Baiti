from .Camera import Camera
from interaction.speech import *

cam = Camera("src/assets/images/image.jpeg", 2)

def cam_request():
   speak("Modo camera ativo!")
   
   while True:
      user_response = listen()
      
      if user_response == 'voltar':
         speak("Saindo do modo camera...")
         return 'pass'
      elif user_response == 'foto':
         speak("Foto tirada!")
         cam.take_picture()
         speak("O que deseja fazer agora?")
      elif user_response == 'fotos':
         speak("Foto tirada!")
         cam.take_picture()
         speak("O que deseja fazer agora?")
      elif user_response == 'analisar':
         speak("O que quer que eu analise na imagem?")
         result = cam.analyze_picture(listen())
         
         if result is None:
            speak("Não entendi. Tente novamente!")
         elif result == 'no_image':
            speak("Nenhuma imagem encontrada! Que tal tirar uma nova?")
         else:
            speak(result)
            speak("O que deseja fazer agora?")
      elif user_response is None:
         pass
      else:
         speak("Comando inválido! Tente novamente!")