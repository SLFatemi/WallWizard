import os
import sys
import copy
import time
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generalDefs import loading
import subprocess
import generalDefs as methods
import rich
from dfs import dfs_recursive
import json

with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []
with open("manageUsers/gamelog.json", 'r') as file:
    try:
        logs = json.load(file)
    except json.JSONDecodeError:
        logs = []


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def savejsonlog(logs):
    with open("manageUsers/gamelog.json", 'w') as gamelog:
        json.dump(logs, gamelog, indent=4)


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


def wall_valid(row1, col1, row2, col2, wall_h, wall_v, wall_row, wall_col, mode):
    if (mode == 'h'):
        wall_h[wall_row][wall_col], wall_h[wall_row][wall_col + 1] = "1", "1"
    else:
        wall_v[wall_row][wall_col], wall_v[wall_row + 1][wall_col] = "1", "1"
    visited = [[False for i in range(9)] for j in range(9)]
    dfs_recursive(arrBoard, row1, col1, visited, wall_h, wall_v, "2")
    result1 = False
    for i in range(0, 9):
        if (visited[0][i]):
            result1 = True
            break
    visited = [[False for i in range(9)] for j in range(9)]
    dfs_recursive(arrBoard, row2, col2, visited, wall_h, wall_v, "1")
    result2 = False
    for i in range(0, 9):
        if (visited[8][i]):
            result2 = True
            break
    return result1 and result2


# =============== TOO SLOW ===============


# def printBoard(arrBoard, arrHFences, arrVFences, turn):
#     # methods.printLine()
#     rich.print(
#         f"[bright_white][bold]Player1 : [bright_red]{findplayer1()}\t\t\t    [/bright_red] Player2 : [bright_blue]{findplayer2()}")
#
#     rich.print(
#         "[bright_white][bold]  Enter [bright_green]'w'[/bright_green] to place a wall or Enter [bright_green]'m'[/bright_green] to move \n\t   [deep_pink4]Enter 'leave' to surrender[/deep_pink4]")
#     rich.print(
#         "[white]     Use 'w,a,s,d' to move across the board \n\t   'r' to rotate the wall")
#     if (turn == "p1"):
#         rich.print(f"\t[white][bold]Waiting for [italic][bright_red]Player1[/bright_red][italic] to make a move\n")
#     if (turn == "p2"):
#         rich.print(f"\t[white][bold]Waiting for [italic][bright_blue]Player2[/bright_blue][/italic] to make a move\n")
#     for i in range(17):
#         if (i % 2 == 0):
#             for j in range(9):
#                 if (j == 0):
#                     print("\t", end="")
#                 if (arrBoard[i // 2][j] != "0"):
#                     cell = "[bright_red]1" if arrBoard[i // 2][j] == "1" else "[bright_blue]2"
#                     console.print(cell, end=" ")
#                 else:
#                     console.print("[white]0", end=" ")
#                 if (j < 8):
#                     if (arrVFences[i // 2][j] == '1'):
#                         cell = "[bright_white]┃"
#                     elif (arrVFences[i // 2][j] == '2'):
#                         cell = "[cyan]┃"
#                     else:
#                         cell = " "
#                     rich.print(f"{cell}", end=" ")
#         else:
#             for j in range(9):
#                 if (j == 0):
#                     print("\t", end="")
#                 if (arrHFences[i // 2][j] == '1'):
#                     cell = "[bright_white]━━"
#                 elif (arrHFences[i // 2][j] == '2'):
#                     cell = "[cyan]━━"
#                 else:
#                     cell = "  "
#                 rich.print(f"[bright_white]{cell}", end="  ")
#         print()


def printBoard(arrBoard, arrHFences, arrVFences, turn):
    # methods.printLine()
    board_str = []
    board_str.append(
        f"[bright_white][bold]Player1 : [bright_red]{findplayer1()}\t\t\t    [/bright_red] Player2 : [bright_blue]{findplayer2()}")
    board_str.append(
        f"[orange3][bold]Remaining walls : [bright_white]{wallsp1}[/bright_white]\t\tRemaining walls : [bright_white]{wallsp2}\n")
    board_str.append(
        "[bright_white][bold]  Enter [bright_green]'w'[/bright_green] to place a wall or Enter [bright_green]'m'[/bright_green] to move \n\t   [deep_pink4]Enter 'leave' to surrender[/deep_pink4]")
    board_str.append(
        "[white]     Use [bright_green]'w,a,s,d'[/bright_green] to move across the board \n\t    Use [bright_green]'r'[/bright_green] to rotate the wall\n")
    if (turn == "p1"):
        board_str.append(
            f"\t[white][bold]Waiting for [italic][bright_red]Player1[/bright_red][/italic] to make a move\n")
    if (turn == "p2"):
        board_str.append(
            f"\t[white][bold]Waiting for [italic][bright_blue]Player2[/bright_blue][/italic] to make a move\n")
    for i in range(17):
        if (i % 2 == 0):
            row_str = "\t"
            for j in range(9):
                if (arrBoard[i // 2][j] != "0"):
                    # cell = "[bright_red]1 " if arrBoard[i // 2][j] == "1" else "[bright_blue]2 "
                    # ====================== COMMENT THIS IF THERE ARE RENDERING ISSUES ===============================
                    cell = "[red]⬛" if arrBoard[i // 2][j] == "1" else "[blue]⬛"
                    row_str += cell
                else:
                    # row_str += "[white]0 "
                    # ====================== COMMENT THIS IF THERE ARE RENDERING ISSUES ===============================
                    row_str += "[grey84]⬛"
                if (j < 8):
                    if (arrVFences[i // 2][j] == '1'):
                        cell = "[dark_orange3]┃"
                    elif (arrVFences[i // 2][j] == '2'):
                        cell = "[cyan]┃"
                    else:
                        cell = " "
                    row_str += cell + " "
            board_str.append(row_str)
        else:
            row_str = "\t"
            for j in range(9):
                if (arrHFences[i // 2][j] == '1'):
                    cell = "[dark_orange3]━━"
                elif (arrHFences[i // 2][j] == '2'):
                    cell = "[cyan]━━"
                else:
                    cell = "  "
                row_str += cell + "  "
            board_str.append(row_str)
    rich.print("\n".join(board_str))  ##


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


def placewall(turn, wallrow=7, wallcolmn=0):
    realarrHFences = copy.deepcopy(arrHFences)
    realarrVFences = copy.deepcopy(arrVFences)
    vertical = True
    while (True):
        if (vertical):
            arrVFences[wallrow][wallcolmn] = '2'
            arrVFences[wallrow + 1][wallcolmn] = '2'
        else:
            arrHFences[wallrow][wallcolmn] = '2'
            arrHFences[wallrow][wallcolmn + 1] = '2'
        printBoard(arrBoard, arrHFences, arrVFences, turn)
        s = input()
        methods.clear()
        if (vertical):
            arrVFences[wallrow][wallcolmn] = '2'
            arrVFences[wallrow + 1][wallcolmn] = '2'
            if (s == 'w'):
                if (wallrow <= 0):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrVFences[wallrow + 1][wallcolmn] = realarrVFences[wallrow + 1][wallcolmn]
                wallrow -= 1
            if (s == 's'):
                if (wallrow >= 7):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrVFences[wallrow][wallcolmn] = realarrVFences[wallrow][wallcolmn]

                wallrow += 1
            if (s == 'd'):
                if (wallcolmn >= 7):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrVFences[wallrow][wallcolmn] = realarrVFences[wallrow][wallcolmn]
                arrVFences[wallrow + 1][wallcolmn] = realarrVFences[wallrow + 1][wallcolmn]
                wallcolmn += 1
            if (s == 'a'):
                if (wallcolmn <= 0):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrVFences[wallrow][wallcolmn] = realarrVFences[wallrow][wallcolmn]
                arrVFences[wallrow + 1][wallcolmn] = realarrVFences[wallrow + 1][wallcolmn]
                wallcolmn -= 1
            if (s == 'r'):
                vertical = False
                arrVFences[wallrow][wallcolmn] = realarrVFences[wallrow][wallcolmn]
                arrVFences[wallrow + 1][wallcolmn] = realarrVFences[wallrow + 1][wallcolmn]
            if (s == " "):
                # ======================= CHECK WITH DFS ===================
                if (not wall_valid(rowp1, colmnp1, rowp2, colmnp2, arrHFences, arrVFences, wallrow, wallcolmn, 'v')):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                # TODO
                # ======================= CHECK OTHER WALLS ===================
                if (realarrHFences[wallrow][wallcolmn] == '1' and realarrHFences[wallrow][wallcolmn + 1] == '1'):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                if (realarrVFences[wallrow][wallcolmn] == '1' or realarrVFences[wallrow + 1][wallcolmn] == '1'):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                arrVFences[wallrow][wallcolmn] = '1'
                arrVFences[wallrow + 1][wallcolmn] = '1'
                break
        else:
            arrHFences[wallrow][wallcolmn] = '2'
            arrHFences[wallrow][wallcolmn + 1] = '2'
            if (s == 'w'):
                if (wallrow <= 0):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrHFences[wallrow][wallcolmn] = realarrHFences[wallrow][wallcolmn]
                arrHFences[wallrow][wallcolmn + 1] = realarrHFences[wallrow][wallcolmn + 1]
                wallrow -= 1
            if (s == 's'):
                if (wallrow >= 7):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrHFences[wallrow][wallcolmn] = realarrHFences[wallrow][wallcolmn]
                arrHFences[wallrow][wallcolmn + 1] = realarrHFences[wallrow][wallcolmn + 1]
                wallrow += 1
            if (s == 'd'):
                if (wallcolmn >= 7):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrHFences[wallrow][wallcolmn] = realarrHFences[wallrow][wallcolmn]
                wallcolmn += 1
            if (s == 'a'):
                if (wallcolmn <= 0):
                    rich.print("[bold][bright_red]\t    You can't make that move")
                    continue
                arrHFences[wallrow][wallcolmn + 1] = realarrHFences[wallrow][wallcolmn + 1]
                wallcolmn -= 1
            if (s == 'r'):
                vertical = True
                arrHFences[wallrow][wallcolmn] = realarrHFences[wallrow][wallcolmn]
                arrHFences[wallrow][wallcolmn + 1] = realarrHFences[wallrow][wallcolmn + 1]
            if (s == " "):
                # ======================= CHECK WITH DFS ===================
                if (not wall_valid(rowp1, colmnp1, rowp2, colmnp2, arrHFences, arrVFences, wallrow, wallcolmn, 'h')):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                # ======================= CHECK OTHER WALLS ===================
                if (realarrVFences[wallrow][wallcolmn] == '1' and realarrVFences[wallrow + 1][wallcolmn] == '1'):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                if (realarrHFences[wallrow][wallcolmn] == '1' or realarrHFences[wallrow][wallcolmn + 1] == '1'):
                    rich.print("[bold][bright_red]\t    You can't place that wall")
                    continue
                arrHFences[wallrow][wallcolmn] = '1'
                arrHFences[wallrow][wallcolmn + 1] = '1'
                break


def findlistofmove(row, colmn):
    listofmoves = ['w', 's', 'd', 'a']
    if (row <= 0 or isWallUP(row, colmn)):
        listofmoves.remove('w')
    if (row >= 8 or isWallDOWN(row, colmn)):
        listofmoves.remove('s')
    if (colmn <= 0 or isWallLEFT(row, colmn)):
        listofmoves.remove('a')
    if (colmn >= 8 or isWallRIGHT(row, colmn)):
        listofmoves.remove('d')
    return listofmoves


def changeplayer1pos(row, colmn, inpt):
    if (inpt not in findlistofmove(row, colmn)):
        # print(findlistofmove(row, colmn))
        rich.print("[bold][bright_red]\t    You can't make that move")
        return False
    arrBoard[row][colmn] = "0"
    if (inpt == 'w'):
        if (arrBoard[row - 1][colmn] != '0'):
            # ========== NEGATIVE INDEXING (can't use try:except) ============
            if (row - 2 >= 0):
                # TODO
                # =================== WALL EXCEPTION HANDLING ==================
                arrBoard[row - 2][colmn] = "1"
                return (row - 2, colmn)
            else:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "1"
                return False
        arrBoard[row - 1][colmn] = "1"
        return (row - 1, colmn)
    if (inpt == 's'):
        if (arrBoard[row + 1][colmn] != '0'):
            try:
                # TODO
                # =================== WALL EXCEPTION HANDLING ==================
                arrBoard[row + 2][colmn] = "1"
                return (row + 2, colmn)
            except:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "1"
                return False
        arrBoard[row + 1][colmn] = "1"
        return (row + 1, colmn)
    if (inpt == 'd'):
        if (arrBoard[row][colmn + 1] != '0'):
            try:
                # TODO
                # =================== WALL EXCEPTION HANDLING ==================
                arrBoard[row][colmn + 2] = "1"
                return (row, colmn + 2)
            except:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "1"
                return False
        arrBoard[row][colmn + 1] = "1"
        return (row, colmn + 1)
    if (inpt == 'a'):
        if (arrBoard[row][colmn - 1] != '0'):
            # ========== NEGATIVE INDEXING (can't use try:except) ============
            if (colmn - 2 >= 0):
                # TODO
                # =================== WALL EXCEPTION HANDLING ==================
                arrBoard[row][colmn - 2] = "1"
                return (row, colmn - 2)
            else:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "1"
                return False
        arrBoard[row][colmn - 1] = "1"
        return (row, colmn - 1)


def wincondition(rowp1, rowp2):
    if (rowp2 == 8):
        rich.print(
            "\n[bold][bright_white][bright_blue]\t   Player2[/bright_blue] is the [gold1]W I N N E R ![/gold1]\n")
        time.sleep(1)
        rich.print("[bold][bright_white]\t    Returning back to menu...\n")
        print("\t\t", end="")
        loading()
        addloganddump(logs, findplayer2())
        subprocess.run(["python", "menu.py"], check=True)
        exit()
    if (rowp1 == 0):
        rich.print(
            "\n[bold][bright_white][bright_red]\t   Player1[/bright_red] is the [gold1]W I N N E R ![/gold1]\n")
        rich.print("[bold][bright_white]\t    Returning back to menu...\n")
        time.sleep(1)
        print("\t\t", end="")
        loading()
        addloganddump(logs, findplayer1())
        subprocess.run(["python", "menu.py"], check=True)
        exit()


def changeplayer2pos(row, colmn, inpt):
    if (inpt not in findlistofmove(row, colmn)):
        # print(findlistofmove(row, colmn))
        rich.print("[bold][bright_red]\t    You can't make that move")
        return False
    arrBoard[row][colmn] = "0"
    if (inpt == 'w'):
        if (arrBoard[row - 1][colmn] != '0'):
            # ========== NEGATIVE INDEXING (can't use try:except) ============
            if (row - 2 >= 0):
                arrBoard[row - 2][colmn] = "2"
                return (row - 2, colmn)
            else:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "2"
                return False
        arrBoard[row - 1][colmn] = "2"
        return (row - 1, colmn)
    if (inpt == 's'):
        if (arrBoard[row + 1][colmn] != '0'):
            try:
                arrBoard[row + 2][colmn] = "2"
                return (row + 2, colmn)
            except:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "2"
                return False
        arrBoard[row + 1][colmn] = "2"
        return (row + 1, colmn)
    if (inpt == 'd'):
        if (arrBoard[row][colmn + 1] != '0'):
            try:
                arrBoard[row][colmn + 2] = "2"
                return (row, colmn + 2)
            except:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "2"
                return False
        arrBoard[row][colmn + 1] = "2"
        return (row, colmn + 1)
    if (inpt == 'a'):
        if (arrBoard[row][colmn - 1] != '0'):
            # ========== NEGATIVE INDEXING (can't use try:except) ============
            if (colmn - 2 >= 0):
                arrBoard[row][colmn - 2] = "2"
                return (row, colmn - 2)
            else:
                rich.print("[bold][bright_red]\t    You can't make that move")
                arrBoard[row][colmn] = "2"
                return False
        arrBoard[row][colmn - 1] = "2"
        return (row, colmn - 1)


def addloganddump(logs, winner):
    log = {
        "id": str(uuid.uuid4())[::5],
        "player1": findplayer1(),
        "player2": findplayer2(),
        "winner": winner,
        "date": date,
        "length": int(end - start)
    }
    logs.append(log)
    savejsonlog(logs)


wallsp1 = 10
wallsp2 = 10
methods.clear()
date = time.ctime(time.time())
start = time.time()
# ======================= initialize board ===========================
arrBoard = [["0" for i in range(9)] for j in range(9)]
arrVFences = [["0" for i in range(8)] for j in range(9)]
arrHFences = [["0" for i in range(9)] for j in range(8)]
rowp1 = 8
rowp2 = 0
colmnp1 = 4
colmnp2 = 4
arrBoard[rowp2][colmnp2] = "2"
arrBoard[rowp1][colmnp1] = "1"
turn = 'p1'
printBoard(arrBoard, arrHFences, arrVFences, turn)
while (True):
    # ========================= WIN CONDITION ============================
    wincondition(rowp1, rowp2)
    ipt = input()
    if (turn == "p1"):
        if (ipt == 'm'):
            userinput = input()
            methods.clear()
            output = changeplayer1pos(rowp1, colmnp1, userinput)
            if (output == False):
                printBoard(arrBoard, arrHFences, arrVFences, turn)
                continue
            rowp1 = output[0]
            colmnp1 = output[1]
        elif (ipt == 'w'):
            methods.clear()
            if (wallsp1 == 0):
                rich.print("[bold][bright_red]\t\tYou're out of walls")
                printBoard(arrBoard, arrHFences, arrVFences, turn)
                continue
            wallsp1 -= 1
            placewall("p1", 4, 4)
        elif (ipt == 'leave'):
            rich.print("[white][bright_red]\t     Player1[/bright_red] has surrendered\n")
            rich.print(
                "[bold][bright_white][bright_blue]\t   Player2[/bright_blue] is the [gold1]W I N N E R ![/gold1]\n")
            time.sleep(1)
            rich.print("[bold][bright_white]\t    Returning back to menu...\n")
            print("\t\t", end="")
            loading()
            # TODO
            end = time.time()
            addloganddump(logs, findplayer2())
            subprocess.run(["python", "menu.py"], check=True)
            exit()
        else:
            methods.clear()
            rich.print("[bold][bright_red]\t\t  Invalid input")
            printBoard(arrBoard, arrHFences, arrVFences, turn)
            continue
    if (turn == "p2"):
        if (ipt == 'm'):
            userinput = input()
            methods.clear()
            output = changeplayer2pos(rowp2, colmnp2, userinput)
            if (output == False):
                printBoard(arrBoard, arrHFences, arrVFences, turn)
                continue
            rowp2 = output[0]
            colmnp2 = output[1]
        elif (ipt == 'w'):
            methods.clear()
            if (wallsp2 == 0):
                rich.print("[bold][bright_red]\t\tYou're out of walls")
                printBoard(arrBoard, arrHFences, arrVFences, turn)
                continue
            wallsp2 -= 1
            placewall("p2", 4, 4)
        elif (ipt == 'leave'):
            rich.print("[white][bright_blue]\t     Player2[/bright_blue] has surrendered\n")
            rich.print(
                "[bold][bright_white][bright_red]\t   Player1[/bright_red] is the [gold1]W I N N E R ![/gold1]\n")
            rich.print("[bold][bright_white]\t    Returning back to menu...\n")
            time.sleep(1)
            print("\t\t", end="")
            loading()
            # TODO
            end = time.time()
            addloganddump(logs, findplayer1())
            subprocess.run(["python", "menu.py"], check=True)
            exit()
        else:
            methods.clear()
            rich.print("[bold][bright_red]\t\t  Invalid input")
            printBoard(arrBoard, arrHFences, arrVFences, turn)
            continue
    if (turn == "p1"):
        turn = "p2"
    else:
        turn = "p1"
    printBoard(arrBoard, arrHFences, arrVFences, turn)
