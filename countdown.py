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


def app_loop():
    print("Welcome to the JAPT - Just Another Pomodoro Timer!")
    focus_min = int(input("How long should the focus session be? (minutes): "))
    focus_sec = int(input("Sec: "))
    rest = int(input("How long should the short break be? (minutes): "))
    cycles = int(input("How many Pomodoro cycles? (default 4): "))

    while True:
        print("Starting Pomodoro timer! Time to work!")
        for _ in range(0, cycles):
            count_down(focus_min, focus_sec)
            print("Time to rest!")
            playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

            count_down(rest)
            print("Time to work!")
            playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

        print("Time to long break!")
        count_down(m=15)
        playsound('sounds/mixkit-arcade-retro-game-over-213.wav')

        next_round = input("Wanna start again? (Y/n)")

        if next_round == "y" or next_round == "Y" or next_round == "":
            continue
        else:
            print("Goodbye!")
            break

