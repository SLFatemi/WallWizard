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


def isloggedin():
    for user in users:
        if (user["isloggedin"] == True):
            return user["username"]
    return False


def checkuserValidation(usertocheck, passwordtocheck):
    usertocheck = usertocheck.strip()
    passwordtocheck = passwordtocheck.strip()
    for user in users:
        stored_pass = user["password"].encode('utf-8')
        if (user["username"] == usertocheck):
            if (bcrypt.checkpw(passwordtocheck.encode('utf-8'), stored_pass)):
                user["isloggedin"] = True
                savejson(users)
                return True
            rich.print("[bold][red]Password is incorrect , Try again [/red][/bold]")
            return False
    rich.print("[bold][red]Username doesn't exists , Try again [/red][/bold]")
    return False


if (isloggedin() != False):
    rich.print(
        f"[khaki3][bold]You are already logged in as [italic][deep_pink4]{isloggedin()} [/italic][/deep_pink4] [/khaki3][/bold]\n")
    rich.print("[bright_white][bold]to logout , Enter : [medium_orchid1]logout[/medium_orchid1]")
    rich.print("[bright_white][bold]to go back to menu , Enter : [medium_orchid1]menu[/medium_orchid1]\n")
    while (True):
        s = input()
        if (s == 'logout'):
            rich.print(
                f"[orchid][bold]You have successfully logged out , you can Sign in now\n")
            for user in users:
                if (user["username"] == isloggedin()):
                    user["isloggedin"] = False
            savejson(users)
            break
        elif (s == "menu"):
            subprocess.run(["python", "menu.py"], check=True)
        else:
            rich.print(
                "[bold][bright_white]To get back to menu, Enter : [yellow]menu[/yellow] , or Try again[/bright_white][/bold]")

while (True):
    rich.print("[light_goldenrod3][bold]Enter your username :")
    username = input()
    rich.print("[light_goldenrod3][bold]Enter your password :")
    password = input()
    if (checkuserValidation(username, password)):
        rich.print(f"[green][bold]\nWelcome , [deep_pink4]{username}![/deep_pink4][/green][/bold]")
        break

time.sleep(2)
subprocess.run(["python", "menu.py"], check=True)
