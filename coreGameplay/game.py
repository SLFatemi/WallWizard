from fileinput import close

from PIL.ImageColor import colormap

import generalDefs as methods
import bcrypt
import time
import re
import rich
from rich.console import Console
import json
import uuid
import subprocess

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


def printBoard(arrBoard, arrHFences, arrVFences, turn):
    methods.printLine()
    rich.print(
        f"[bright_white][bold]Player1 : [bright_red]{findplayer1()}\t\t\t    [/bright_red] Player2 : [bright_blue]{findplayer2()}")
    if (turn == "p1"):
        rich.print(f"\n\t[white][bold]Waiting for [bright_red]Player1[/bright_red] to make a move\n")
    else:
        rich.print(f"\n\t[white][bold]Waiting for [bright_blue]Player2[/bright_blue] to make a move\n")
    for i in range(17):
        if (i % 2 == 0):
            for j in range(9):
                if (j == 0):
                    print("\t", end="")
                if (arrBoard[i // 2][j] != "0"):
                    cell = "[bright_red]1" if arrBoard[i // 2][j] == "1" else "[bright_blue]2"
                    console.print(cell, end=" ")
                else:
                    console.print("0", end=" ")
                if (j < 8):
                    cell = "┃" if arrVFences[i // 2][j] == "1" else " "
                    rich.print(f"[bold]{cell}", end=" ")
        else:
            for j in range(9):
                if (j == 0):
                    print("\t", end="")
                cell = "━━" if arrHFences[i // 2][j] == "1" else "  "
                rich.print(f"[bold]{cell}", end="  ")
        print()


def isWallUP(row, colmn):
    try:
        if (arrHFences[row - 1][colmn] == "1"):
            return True
    except:
        return False


def isWallDOWN(row, colmn):
    try:
        if (arrHFences[row][colmn] == "1"):
            return True
    except:
        return False


def isWallRIGHT(row, colmn):
    try:
        if (arrVFences[row][colmn] == "1"):
            return True
    except:
        return False


def isWallLEFT(row, colmn):
    try:
        if (arrVFences[row][colmn - 1] == "1"):
            return True
    except:
        return False


def findlistofmove(row, colmn):
    listofmoves = ['w', 's', 'd', 'a']
    if (row <= 0 or arrBoard[row - 1][colmn] != "0" or isWallUP(row, colmn)):
        listofmoves.remove('w')
    if (row >= 8 or arrBoard[row + 1][colmn] != "0" or isWallDOWN(row, colmn)):
        listofmoves.remove('s')
    if (colmn <= 0 or arrBoard[row][colmn - 1] != "0" or isWallLEFT(row, colmn)):
        listofmoves.remove('a')
    if (colmn >= 8 or arrBoard[row][colmn + 1] != "0" or isWallRIGHT(row, colmn)):
        listofmoves.remove('d')
    return listofmoves


def changeplayer1pos(row, colmn, inpt):
    if (inpt not in findlistofmove(row, colmn)):
        # print(findlistofmove(row, colmn))
        rich.print("[bold][bright_red] You can't make that move")
        return False
    arrBoard[row][colmn] = "0"
    if (inpt == 'w'):
        arrBoard[row - 1][colmn] = "1"
        return (row - 1, colmn)
    if (inpt == 's'):
        arrBoard[row + 1][colmn] = "1"
        return (row + 1, colmn)
    if (inpt == 'd'):
        arrBoard[row][colmn + 1] = "1"
        return (row, colmn + 1)
    if (inpt == 'a'):
        arrBoard[row][colmn - 1] = "1"
        return (row, colmn - 1)


def changeplayer2pos(row, colmn, inpt):
    if (inpt not in findlistofmove(row, colmn)):
        rich.print("[bold][bright_red]You can't make that move")
        return False
    arrBoard[row][colmn] = "0"
    if (inpt == 'w'):
        arrBoard[row - 1][colmn] = "2"
        return (row - 1, colmn)
    if (inpt == 's'):
        arrBoard[row + 1][colmn] = "2"
        return (row + 1, colmn)
    if (inpt == 'd'):
        arrBoard[row][colmn + 1] = "2"
        return (row, colmn + 1)
    if (inpt == 'a'):
        arrBoard[row][colmn - 1] = "2"
        return (row, colmn - 1)


console = Console()
# ======================= initialize board ===========================
arrBoard = [["0" for i in range(9)] for j in range(9)]
arrVFences = [["0" for i in range(8)] for j in range(9)]
arrHFences = [["0" for i in range(9)] for j in range(8)]
# ======================= TEST ==========================
arrHFences[7][4] = "1"
arrVFences[6][4] = "1"
arrHFences[5][4] = "1"
arrVFences[4][4] = "1"
rowp1 = 8
rowp2 = 0
colmnp1 = 4
colmnp2 = 4
arrBoard[rowp2][colmnp2] = "2"
arrBoard[rowp1][colmnp1] = "1"
turn = 'p1'
printBoard(arrBoard, arrHFences, arrVFences, turn)
while (True):
    userinput = input()
    methods.clear()
    if (turn == "p1"):
        output = changeplayer1pos(rowp1, colmnp1, userinput)
        if (output == False):
            printBoard(arrBoard, arrHFences, arrVFences, turn)
            continue
        rowp1 = output[0]
        colmnp1 = output[1]
    if (turn == "p2"):
        output = changeplayer2pos(rowp2, colmnp2, userinput)
        if (output == False):
            printBoard(arrBoard, arrHFences, arrVFences, turn)
            continue
        rowp2 = output[0]
        colmnp2 = output[1]
    if (turn == "p1"):
        turn = "p2"
    else:
        turn = "p1"
    printBoard(arrBoard, arrHFences, arrVFences, turn)
