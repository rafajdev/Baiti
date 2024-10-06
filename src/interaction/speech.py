import speech_recognition 
from .speech_handler import play, handle
from functions.robot.buzzer import beep

def listen():
   recognizer = speech_recognition.Recognizer()
   mic = speech_recognition.Microphone()
   
   with mic as source:
      recognizer.adjust_for_ambient_noise(source)
      beep()
      print("Ouvindo...") # Substituir por buzzer e display

      try:
         audio = recognizer.listen(source)
         text = recognizer.recognize_google(audio, language="pt-BR")

         print(f"Você: {text}")
         return text
      
      except speech_recognition.UnknownValueError as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
      
      except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None       
           
def speak(text):
   handle(text)
   play()