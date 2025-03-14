import time
import datetime
import sys
from playsound import playsound
import countdown


def main():
    print("Welcome to the JAPT - Just Another Pomodoro Timer!")
    focus_min = int(input("How long should the focus session be? (minutes): "))
    focus_sec = int(input("Sec: "))
    rest = int(input("How long should the short break be? (minutes): "))
    cycles = int(input("How many Pomodoro cycles? (default 4): "))


    print("Starting Pomodoro timer")
    countdown.ring(focus_min, focus_sec)


if __name__ == "__main__":
    main()