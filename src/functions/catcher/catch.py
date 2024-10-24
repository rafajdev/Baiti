from functions.robot.control import arm 
from functions.camera.control import cam
from interaction.speech import *
import time

def start():
    speak('Modo bloco ativo!')
    speak('O que deseja fazer?')
    arm.main_led.set_color_by_name('branco')

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
                text1 = cam.analyze_picture('qual a cor do bloco sobre a mesa?')

                colors = ['vermelho', 'verde', 'azul', 'amarelo', 'amarela']
                for color in colors: 
                    if color in text1: 
                        detected_color = color

                print(detected_color)

                arm.main_led.set_color_by_name(detected_color)

            
                arm.move_default()
                time.sleep(0.2)
                arm.move_open()
                time.sleep(0.2)
                arm.move_down()
                time.sleep(0.2)
                arm.move_front()
                time.sleep(0.2)
                arm.move_close()
                time.sleep(0.2)
                arm.move_up()
                time.sleep(0.2)
                arm.move_back()

                if detected_color == 'vermelho':
                    arm.move_left()
                    time.sleep(0.2)
                    arm.move_front()
                    time.sleep(0.2)
                    arm.move_open()

                if detected_color == 'azul':
                    arm.move_right()
                    time.sleep(0.2)
                    arm.move_front()
                    time.sleep(0.2)
                    arm.move_open()

                if detected_color == 'verde':
                    arm.move_left_diagonal()
                    time.sleep(0.2)
                    arm.move_front()
                    time.sleep(0.2)
                    arm.move_open()

                if detected_color == 'amarelo' or 'amarela':
                    arm.move_right_diagonal()
                    time.sleep(0.2)
                    arm.move_front()
                    time.sleep(0.2)
                    arm.move_open()

                speak(text1)
                arm.move_default()