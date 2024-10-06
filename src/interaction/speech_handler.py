from gtts import gTTS
import pygame
import time

def handle(text):
   tts = gTTS(text, lang="pt-BR")
   tts.save('baiti/src/assets/audio/speech.mp3')

def play():
   pygame.init()
   pygame.mixer.init()
   pygame.mixer.music.load('baiti/src/assets/audio/speech.mp3')  
   time.sleep(0.5) 
   
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
      time.sleep(1)

   pygame.quit()