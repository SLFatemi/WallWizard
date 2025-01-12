import generalDefs as methods
import rich
import subprocess
import json

methods.clear()
methods.printLine()

with open("manageUsers/gamelog.json", 'r') as file:
    try:
        logs = json.load(file)
    except json.JSONDecodeError:
        logs = []

for game in logs:
    rich.print(f"[orange1][bold]============= GAME ID : [white]{game['id']}[/white] =============\n")
    rich.print(f"Player1 : [bright_red]{game['player1']}[/bright_red]\t\t\tPlayer2 : [bright_blue]{game['player2']}\n")
    rich.print(f"\t      [gold1]W I N N E R ![/gold1] : {game['winner']}\n")
    rich.print(f"    Game was played on: {game['date']}\n")
    # TODO CONVERT SECOND TO MINUTES AND HOUR
    rich.print(f"\t     Game took {game['length']} second(s)\n")
