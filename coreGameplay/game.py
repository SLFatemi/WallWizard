import os 
import sys
#This is for add module from parent dir
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import generalDefs as methods
import bcrypt
import time
import re
import rich
from rich.console import Console
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


def printBoard(arrBoard, arrHFences, arrVFences):
    for i in range(17):
        if (i % 2 == 0):
            for j in range(9):
                if (j == 0):
                    print("    ", end="")
                if (arrBoard[i // 2][j] != "0"):
                    cell = "🟥" if arrBoard[i // 2][j] == "1" else "🟦"
                    console.print(cell, end=" ")
                else:
                    console.print("⬛ ", end=" ")
                if (j < 8):
                    rich.print(f"[bold]{arrVFences[i // 2][j]}", end=" ")
        else:
            for j in range(9):
                if (j == 0):
                    print("    ", end="")
                rich.print(f"[bold]{arrHFences[i // 2][j]}", end="   ")
        print()


console = Console()
# ======================= initialize board ===========================
arrBoard = [["0" for i in range(9)] for j in range(9)]
arrVFences = [["┃" for i in range(8)] for j in range(9)]
arrHFences = [["━━" for i in range(9)] for j in range(8)]
rich.print(
    f"[bright_white][bold]Player1 : [bright_red]{findplayer1()}\t\t\t    [/bright_red] Player2 : [bright_blue]{findplayer2()}")
rich.print(f"\n\t[white][bold]Waiting for [bright_red]Player1[/bright_red] to make a move\n")
# ==========TEST==========
arrBoard[0][4] = "2"
arrBoard[7][4] = "1"
printBoard(arrBoard, arrHFences, arrVFences)

class move_table:
    def __init__(self):
        pass

class wall_table:
    def __init__(self):
        pass