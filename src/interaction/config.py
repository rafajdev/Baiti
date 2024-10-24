import os
import google.generativeai as genai
from utils.json_handler import json_h
from dotenv import load_dotenv

def apiConfig():
   """
   Initialize the Gemini model and start a chat session using the history from the config.
   
   The Gemini model is configured with the API key from the .env file,
   and the chat session is started with the history from the config.
   
   Returns:
      A chat object representing the chat session.
   """
   load_dotenv()
   api_key = os.getenv('GOOGLE_API_KEY')

   try:
      genai.configure(api_key=api_key)
      model = genai.GenerativeModel("gemini-1.5-flash")

      chat = model.start_chat(
         history = json_h.read('config')['history']
      )
      
      return chat
   except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}") # Fazer isto aparecer em um display se possível
      




api_key = os.getenv('GOOGLE_API_KEY')


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


result = model.generate_content(
    [myfile, "\n\n", "Can you tell me about the instruments in this photo?"]
)
