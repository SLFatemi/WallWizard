import generalDefs as methods
import bcrypt
import time
import re
import rich
import json
import uuid
import subprocess

methods.clear()
methods.printLine()

with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def findplayer1():
    for user in users:
        if (user["isloggedin"] == True):
            return user["username"]
    return False


def findplayer2():
    for user in users:
        if (user["isPlayer2"] == True):
            return user["username"]
    return False


rich.print(f"[bright_white][bold]Player1 : [violet]{findplayer1()}\t\t[/violet] Player2 : [violet]{findplayer2()}")
rich.print(f"\n   [bright_green][bold]Waiting for Player1 to make a move")
