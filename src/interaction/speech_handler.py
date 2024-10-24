from gtts import gTTS
import pygame
import time
from pydub import AudioSegment

def generate_speech(text: str):
    """
    Generate a speech audio file based on given text.

    The generated audio file is saved in the "src/assets/audios/speech.mp3" file.

    Parameters
    ----------
    text : str
        The text to be converted to speech.
    """
    try:
        speech_generator = gTTS(text, lang="pt-BR")
        speech_generator.save("src/assets/audios/speech.mp3")

        audio = AudioSegment.from_mp3("src/assets/audios/speech.mp3")
        audio = audio.speedup(playback_speed=1.3)
        audio.export("src/assets/audios/speech.mp3", format="mp3")
    except Exception as e:
        print(f"Error generating speech: {e}")

def play_speech():
    """
    Play the generated speech audio file.

    This function initializes the Pygame mixer, loads the speech audio file, plays it,
    and waits until the audio finishes playing before quitting Pygame.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("src/assets/audios/speech.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except Exception as e:
        print(f"Error playing speech: {e}")
    finally:
        pygame.quit()