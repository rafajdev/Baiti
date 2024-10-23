import cv2
import os
import google.generativeai as genai
from interaction.config import apiConfig

class Camera:
   def __init__(self, camera_index: int = 0):
      self.camera = cv2.VideoCapture(camera_index)
      
   def take_picture(self):
      if not self.camera.isOpened():
         print("Erro ao acessar a câmera!")
         return
      
      ret, frame = self.camera.read()
      
      if ret:
         cv2.imwrite('src/assets/images/image.jpeg', frame)
         print("Foto tirada e salva!")
         self._release()
      else:
         print("Erro ao capturar a imagem!")

   def _release(self):
      self.camera.release()
      cv2.destroyAllWindows()
        
   def analyze_picture(self, request: str):
      if not os.path.exists('src/assets/images/image.jpeg'):
         return "no_image"
      
      API = apiConfig()
      model = API[1]
      
      file = genai.upload_file(path="src/assets/images/image.jpeg")
      
      result = model.generate_content(
         [file, "\n\n", request]
      )
      
      return result.text
