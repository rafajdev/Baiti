from functions.robot.control import arm 
from functions.camera.control import cam
from interaction.speech import *

def start():
    speak('Modo bloco ativo!')
    speak('O que deseja fazer?')

    while True:
        user_response = listen()

        if user_response is None:
            pass

        else:
            if user_response.lower() == 'voltar':
                speak("Saindo do modo camera...")
                return 'pass'
            elif user_response.lower() == 'analisar bloco':
                cam.take_picture()
                text1 = cam.analyze_picture('qual a cor do bloco?')
                text2 = cam.analyze_picture('qual o formato do bloco?')
                speak(text1)
                speak(text2)
0
