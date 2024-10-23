from .Camera import Camera
from interaction.speech import *

cam = Camera("src/assets/images/image.jpeg", 2)

def cam_request():
   speak("Modo camera ativo!")
   
   while True:
      speak("O que deseja fazer agora?")
      user_response = listen()
      
      if user_response == 'voltar':
         speak("Saindo do modo camera...")
         return 'pass'
      elif user_response == 'foto':
         speak("Foto tirada!")
         cam.take_picture()
      elif user_response == 'analisar':
         speak("O que quer que eu analise na imagem?")
         result = cam.analyze_picture(listen())
         
         if result == 'no_image':
            speak("Nenhuma imagem encontrada! Que tal tirar uma nova?")
         else:
            speak(result)
      else:
         speak("Comando inválido! Tente novamente!")