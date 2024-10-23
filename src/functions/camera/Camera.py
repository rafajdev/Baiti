import cv2
import os
import google.generativeai as genai
from interaction.config import apiConfig

class Camera:
   """
   A class to handle the camera functionality.

   Parameters
   ----------
   camera_index : int
      The index of the camera to use. Default is 0.

   Attributes
   ----------
   camera : cv2.VideoCapture
      The camera object.

   Methods
   -------
   take_picture()
      Take a picture with the camera.
   analyze_picture(request)
      Analyze the picture taken and return the result.
   """

   def __init__(self, image_storage_path: str, camera_index: int = 0):
      self.camera = cv2.VideoCapture(camera_index)
      self.image_storage_path = image_storage_path
      
   def take_picture(self):
      """
      Take a picture with the camera.
      """
      if not self.camera.isOpened():
         print("Erro ao acessar a câmera!")
         return
      
      ret, frame = self.camera.read()
      
      if ret:
         cv2.imwrite(self.image_storage_path, frame)
         print("Foto tirada e salva!")
         self._release()
      else:
         print("Erro ao capturar a imagem!")

   def _release(self):
      """
      Release the camera and close all windows.
      """
      self.camera.release()
      cv2.destroyAllWindows()
        
   def analyze_picture(self, request: str):
      """
      Analyze the picture taken and return the result.

      Parameters
      ----------
      request : str
         The request to pass to the AI model.

      Returns
      -------
      str
         The result of the analysis.
      """
      if not os.path.exists('src/assets/images/image.jpeg'):
         return "no_image"
      
      API = apiConfig()
      model = API[1]
      
      file = genai.upload_file(path="src/assets/images/image.jpeg")
      
      result = model.generate_content(
         [file, "\n\n", request]
      )
      
      return result.text
