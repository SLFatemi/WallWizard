import generalDefs as methods
import rich
import subprocess
import json
from pygame import mixer

# subprocess.run(["python", "coreGameplay/game.py"], check=True)
# exit()


# =================== PLAY MUSIC ===================
methods.clear()
# rich.print("\n    [cyan1][italic][bold]Hang tight in there![/italic][/bold][white] Getting things ready...\n")
# methods.loading("cyan1", 1)
mixer.init()


def playnavsoundeffect():
    mixer.music.load('nav.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()


def playerrsoundeffect():
    mixer.music.load('error.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()


methods.clear()
lastplacecursor = 0
try:
    with open("manageUsers/users.json", 'r') as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            users = []
except:
    with open("manageUsers/users.json", 'a+') as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            users = []
with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def printMenu(n, menu):
    # methods.clear()
    methods.printLine()
    for user in users:
        if (user["isloggedin"] == True):
            usrname = user["username"]
            rich.print(
                f"[dark_turquoise][bold]You're currently logged in as [italic][deep_pink4]{usrname} [/italic][/deep_pink4 ] \n")
    if (n > len(menulist) - 1):
        n = 4
    if (n < 0 and n != -1):
        n = 0
    for _ in menu:
        if (menu.index(_) == n):
            global lastplacecursor
            lastplacecursor = n
            rich.print(f" ▶ [bright_yellow]{_}[/bright_yellow]")
        else:
            rich.print("  ", f"[bright_white]{_}")


def checkmenuinput(ch, n):
    expectedinputs = ['s', 'S', 'W', 'w']
    ch = ch.strip()
    if (ch in expectedinputs):
        if (expectedinputs.index(ch) < 2):
            if (n != len(menulist) - 1):
                playnavsoundeffect()
                return n + 1
            playerrsoundeffect()
            rich.print("[bright_red][bold]You can't move any lower[/bold][bright_red]")
            return 10
        else:
            if (n != 0):
                playnavsoundeffect()
                return n - 1
            playerrsoundeffect()
            rich.print("[bright_red][bold]You can't move any higher[/bold][bright_red]")
            return -10
    else:
        rich.print("[bright_red][bold]Invalid input , Try again[/bold][bright_red]")
        playerrsoundeffect()
        return lastplacecursor


def selectedMenu(n):
    script_map = {
        0: "manageUsers/signin.py",
        1: "manageUsers/register.py",
        2: "start.py",
        3: "showlog.py",
        4: "exit.py"
    }
    script_to_run = script_map.get(n)
    subprocess.run(["python", script_to_run], check=True)
    exit()


menulist = ["Sign in", "Register", "Start", "Recent Games", "Exit"]
n = 0
printMenu(n, menulist)
while (True):
    rich.print(
        "\n[dark_cyan][bold]Use [magenta2]'w'[/magenta2] to go up, [magenta2]'s'[/magenta2] to go down and [magenta2]'Space'[/magenta2] to select[/bold]")
    menuinput = input("")
    if (menuinput == " "):
        selectedMenu(n)
    methods.clear()
    inp = checkmenuinput(menuinput, n)
    printMenu(inp, menulist)
    if (inp <= 4 and inp >= 0):
        n = inp
