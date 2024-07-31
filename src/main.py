import typer

app = typer.Typer()


@app.command()
def run():
    print(f"Running application")


@app.command()
def test():
    print(f"Testing application. It works!")


if __name__ == "__main__":
    app()