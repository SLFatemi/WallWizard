import generalDefs as methods
import rich
import subprocess
import json

from generalDefs import loading

methods.clear()
methods.printLine()

with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []
userrankdic = {}
for user in users:
    userrankdic.setdefault(user["username"], int(user["rank"]))
userrankdic = dict(sorted(userrankdic.items(), key=lambda item: item[1], reverse=True))
i = 0
for user in userrankdic.items():
    if (i == 0):
        rich.print(f"     {i + 1} : [gold1]{user[0]}[/gold1]\t\t\t[white]Rank[/white]: [gold1]{user[1]}\n")
    if (i == 1):
        rich.print(
            f"     {i + 1} : [bright_black]{user[0]}[/bright_black]\t\t\t[white]Rank[/white]: [light_slate_grey]{user[1]}\n")
    if (i == 2):
        rich.print(
            f"     {i + 1} : [orange4]{user[0]}[/orange4]\t\t\t[white]Rank[/white]: [orange4]{user[1]}\n")
    elif (i > 2):
        rich.print(
            f"     {i + 1} : [white]{user[0]}[/white]\t\t\t[white]Rank[/white]: [bright_blue]{user[1]}\n")
    i += 1
rich.print(f"[orange1][bold]==============================================")
rich.print("\n        [bright_white][bold]Enter anything to get back to [deep_pink4]menu[/deep_pink4]\n")
s = input()
loading()
subprocess.run(["python", "menu.py"], check=True)
