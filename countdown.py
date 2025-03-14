import time
import datetime
import sys
from playsound import playsound





def count_down(m=25, s=0):

    total_seconds = m * 60 + s

    while total_seconds >= 0:
        print(total_seconds)
        time.sleep(1)
        total_seconds -= 1
    
    return True

def ring(m, s):
    if count_down(m, s):
        print("hey!")
        playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

