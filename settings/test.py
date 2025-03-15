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