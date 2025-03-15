import time
import datetime
import sys
from playsound import playsound
import countdown
from settings import settings
import typer

app = typer.Typer(help = "Main info about app")



app.add_typer(countdown.app, name="start", help = "Some text", invoke_without_command=True)
app.add_typer(
    settings.app, 
    name="Settings",  
    help="Pomodoro settings commands.",  # Short description
    rich_help_panel="""\nSome text about command\n
Examples:
    python3 main.py Settings show
    python3 main.py Settings set
"""
)



def show_help():
    """Shows help when no command is provided"""
    app(["--help"])  # Correctly invokes help
    raise typer.Exit()  # Ensures the program exits after showing help

if __name__ == "__main__":
    if len(sys.argv) == 1:  # No arguments provided
        show_help()
    else:
        app()

#if __name__ == "__main__":
 #   countdown_2.app()


# add typer.echo instead of print

# python main pomodoro -> starts pomodoro sessions (with default settings in json)
# python main settings -> shows options I can choose
    # settings show -> show defined settings
    # settings set -> set settings and save

# python main graph today -> show todays sessions
# python main graph week -> show sessions during week
# python main graph all -> all sessions

# user can pause sessions with "p", or stop "s"/ctrl+c

# some beautiful help menu and logo creation

# python main block show -> what websites I block
# python main block set -> set another blocked website
# python main block remove -> remove specific website
# python main block remove all -> remove all blocked websites