import numpy as np
import sounddevice as sd

def beep(duration: float, frequency: float, sample_rate: int):
    """
    Generate a beep sound using the sounddevice library.

    Parameters
    ----------
    duration : float
        The duration of the beep sound in seconds. (Usually between 0.1 and 0.5)
    frequency : float
        The frequency of the beep sound in Hz. (Usually between 240 and 4800)
    sample_rate : int
        The sample rate of the beep sound. (Usually 44100)

    Returns
    -------
    tuple
        A tuple with the elements:
        - "beeped": A string indicating that the sound has been played.
        - duration: The duration of the beep sound in seconds.
        - frequency: The frequency of the beep sound in Hz.
        - sample_rate: The sample rate of the beep sound.

    Examples
    --------
    >>> beep(1, 440, 44100)
    ('beeped', 1.0, 440.0, 44100)

    """
    # Create a numpy array with the time values
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate the beep sound wave
    beep = np.sin(frequency * t * 2 * np.pi)

    # Play the beep sound
    sd.play(beep, samplerate=sample_rate)

    # Wait until the sound has finished playing
    sd.wait()

    # Return a tuple with the beep sound's parameters
    return ("beeped", duration, frequency, sample_rate)

beep(1, 440, 44100)