import generalDefs as methods
import rich
import subprocess
import json

from generalDefs import loading

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

    seconds = int(game['length'])
    minutes = seconds // 60
    hours = minutes // 60
    seconds -= (hours * 3600 + minutes * 60)

    rich.print(f"Game took {hours} hour(s) and {minutes} and minute(s) and {seconds} second(s) ")
rich.print(f"[orange1][bold]====================================================")
rich.print("\n        [bright_white][bold]Enter anything to get back to [deep_pink4]menu[/deep_pink4]\n")
s = input()
loading()
subprocess.run(["python", "menu.py"], check=True)
