import os
import google.generativeai as genai
from utils.json_handler import json_h
from dotenv import load_dotenv

def apiConfig() -> list:
    """
    Configure the Generative AI model and initiate a chat session.

    This function sets up the Generative AI model using the API key specified in the .env file.
    It also initializes a chat session with the existing history from the configuration.

    Returns:
      list: A list containing the chat object and the GenerativeModel instance, [chat, model].

    """
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        chat = model.start_chat(
            history=json_h.read('config')['history']
        )

        return [chat, model]
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")