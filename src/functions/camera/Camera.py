import cv2
import os
import google.generativeai as genai
from interaction.config import apiConfig
import time 

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
        self.camera_index = camera_index
        self.image_storage_path = image_storage_path
        self.camera = None  

    def _open_camera(self):
        """
        Open the camera if it's not already opened.
        """
        if self.camera is None or not self.camera.isOpened():
            self.camera = cv2.VideoCapture(self.camera_index)

    def take_picture(self):
        """
        Take a picture with the camera.
        """
        self._open_camera()

        if not self.camera.isOpened():
            print("Erro ao acessar a câmera!")
            return

        for _ in range(5):
            self.camera.read()

        time.sleep(0.05)  

        ret, frame = self.camera.read()

        if ret:
            cv2.imwrite(self.image_storage_path, frame)
            print("Foto tirada e salva!")
        else:
            print("Erro ao capturar a imagem!")

    def release(self):
        """
        Release the camera and close all windows.
        """
        if self.camera is not None:
            self.camera.release()
            self.camera = None
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
        if not os.path.exists(self.image_storage_path):
            return "no_image"
        
        API = apiConfig()
        model = API[1]
        
        file = genai.upload_file(path=self.image_storage_path)
        
        result = model.generate_content(
            [file, "\n\n", request]
        )
        
        return result.text
