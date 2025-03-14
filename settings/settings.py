import os
import json
CONFIG_FILE = "settings.json"  # Define the settings file path

# Load settings from file or use defaults
def load_settings():
    """Load settings from a JSON file. If the file doesn't exist, return defaults."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return DEFAULT_SETTINGS

# Save new settings to file
def save_settings(focus_min: int, rest_min: int, cycles: int):
    """Save new settings to a JSON file."""
    new_settings = {
        "focus_min": focus_min,
        "rest_min": rest_min,
        "cycles": cycles
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(new_settings, file, indent=4)
    print("✅ Settings saved successfully!") 



app = typer.Typer()

app.add_typer(greet.app, name="greet", aliases=["g"])
app.add_typer(math_ops.app, name="math", aliases=["m"])

def show_help():
    """Shows help when no command is provided"""
    raise typer.Exit(app(["--help"]))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:  # No arguments
        show_help()
    else:
        app()
