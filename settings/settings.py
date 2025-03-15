import os
import json
from typing import Optional
import typer


app = typer.Typer(help = "Some settings")

CONFIG_FILE = "settings/settings.json" 



def load_settings():
    """
    Load Pomodoro settings from a JSON file. If the file doesn't exist, return message that configure file missing
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return f"Configure file missing"



@app.command()
def show() -> None:
    """
    Show configured settings for 'Focus' phase, 'Rest' phase and and 'Study cycles'

    Todo:
        * Configure if user sets 1 minutes -> it should print 1 minute instead of 1 minutes
        * same for cycles
        * you can use probably inflect library
    """
    settings = load_settings()
    if not isinstance(settings, str):
        print(f"Settings:\n")
        print(f'{"Focus phase:".ljust(20, ".")}{settings["focus_min"]:02} minutes')
        print(f'{"Rest phase:".ljust(20, ".")}{settings["rest_min"]:02} minutes')
        print(f'{"Number of cycles:".ljust(20, ".")}{settings["cycles"]:02} cycles\n')
    else:
        print("Configuration file missing or is in wrong directory. Check settings.json in settings/ folder")

    


@app.command()
def set(
    focus_min: Optional[int] = None,
    rest_min: Optional[int] = None,
    cycles: Optional[int] = None
):
    """
    Set different Pomodoro settings (Focus phase, Rest phase, Study cycles). Only positive integers allowed 
    Saves the given settings to a file in JSON format.

    Example:
        set_settings 10 10 10 (focus, rest, cycles)

    Args:
        param1 (int): How long the focus phase should be (minutes)
        param2 (int): How long the rest phase should be (minutes)
        param3 (int): How many study cycles you want 

    Returns:
        None
    """
    if None in [focus_min, rest_min, cycles]:
        focus_min = get_positive_int("How long the focus phase should be? (minutes)")
        rest_min = get_positive_int("How long the rest phase should be? (minutes)")
        cycles = get_positive_int("How many study cycles should be set?")   

    new_settings = {
        "focus_min": focus_min,
        "rest_min": rest_min,
        "cycles": cycles
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(new_settings, file, indent=4)
    print("Setting saved!") 



def get_positive_int(input_message):
    """
    Get positive  from the user, otherwise want user about wrong input
    
    Args:
        param1 (str): Prompt message

    Returns:
        bool: True if user type positive integer, False otherwise
    """
    while True:
        try:
            value = int(input(f"{input_message.ljust(50, '.')} "))
            if value <= 0:
                print("Input should be a positive integer.")
                continue
            return value
        except ValueError:
            print("Input should be a positive integer.")
