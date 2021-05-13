import sounddevice as sd
from src.constants import SAMPLE_RATE, SECONDS

def record():

    myrecording = sd.rec(int(SECONDS*SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()  # Wait until recording is finished

    return myrecording

