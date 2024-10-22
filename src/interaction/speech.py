import speech_recognition 
from .speech_handler import play, handle

def listen() -> str:
   """
   Listen for user voice input and return the text.

   This function uses the speech_recognition library to listen for user voice input, 
   and the recognize_google method to convert the audio to text. The language is set to pt-BR.

   Returns:
      str: The text from the user's voice input, or None if an error occurred.
   """
   recognizer = speech_recognition.Recognizer()
   with speech_recognition.Microphone() as source:
      recognizer.adjust_for_ambient_noise(source, duration=0.5)
      print("Ouvindo...")  # Substituir por buzzer e display

      try:
         audio = recognizer.listen(source)
         text = recognizer.recognize_google(audio, language="pt-BR")

         print(f"Você: {text}")
         return text
      
      except (speech_recognition.UnknownValueError, speech_recognition.RequestError) as e:
         print(f"Ocorreu um erro inesperado: {e}")
         return None

      except Exception as e:
         print(f"Ocorreu um erro inesperado: {e}")
         return None
           
def speak(text):
   """
   Speak the given text by handling it and playing the audio.
   """
   handle(text)
   play()