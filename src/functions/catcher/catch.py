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

                colors = ['vermelho', 'verde', 'azul', 'amarelo', 'amarela']
                for color in colors: 
                    if color in text1: 
                        detected_color = color

                print(detected_color)

                arm.main_led.set_color_by_name(detected_color)

                speak(text1)