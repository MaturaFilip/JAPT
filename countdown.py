import time
import datetime
import sys
from playsound import playsound
import typer
from typing import Optional


app = typer.Typer()

def count_down(minutes: int):
    """
    Time counter for given minuter. Print time every 1 minute.

    Args:
        param1: (int): Minutes

    Returns:
        bool: The return value. True for success, False otherwise
    """
    total_seconds = minutes * 60

    while total_seconds >= 0:
        #if total_seconds % 60 == 0:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{timer}", end = "", flush = True)
        time.sleep(1)
        total_seconds -= 1
    
    return True




#@app.command()
@app.callback()
def start(
    focus_min: Optional[int] = 25,
    rest_min: Optional[int] = 25,
    cycles: Optional[int] = 25
):
    """
    Get user inputs for 'study' session, 'rest' session and how many cycle user want. After cycles ask user for continue session or quit

    Args:
        focus_min (int): Focus session duration in minutes
        rest_min (int): Rest session duration in minutes
        cycles (int): Number of Pomodoro cycles

    Return:
        None
"""

    while True:
        print("Starting Pomodoro timer! Time to work!")
        for _ in range(0, cycles):
            count_down(focus_min)
            print("Time to rest!")
            playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

            count_down(rest_min)
            print("Time to work!")
            playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

        print("Time to long break!")
        count_down(m=15)
        playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

        next_round = input("Wanna start again? (Y/n)")

        if next_round.lower() in ["y", ""]:
            continue
        else:
            print("Goodbye!")
            break
