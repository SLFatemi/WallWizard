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
    for user in users:
        stored_pass = user["password"].encode('utf-8')
        if (user["username"] == usertocheck):
            if (bcrypt.checkpw(passwordtocheck.encode('utf-8'), stored_pass)):
                user["isloggedin"] = True
                savejson(users)
                return True
            rich.print("[bold][red] Password is incorrect , Try again [/red][/bold]")
            return False
    rich.print("[bold][red]Username doesn't exists , Try again [/red][/bold]")
    return False


if (isloggedin() != False):
    rich.print(
        f"[purple][bold]You are already logged in as [italic][blue]{isloggedin()} [/italic][/blue] [/purple][/bold]\n")
    rich.print("[violet][bold]to logout , Enter : [yellow]logout[/yellow]")
    rich.print("[violet][bold]to go back to menu , Enter : [yellow]menu[/yellow]\n")
    while (True):
        s = input()
        if (s == 'logout'):
            rich.print(
                f"[purple][bold]You have successfully logged out , you can Sign in now[/purple][/bold]\n")
            for user in users:
                if (user["username"] == isloggedin()):
                    user["isloggedin"] = False
            savejson(users)
            break
        elif (s == "menu"):
            subprocess.run(["python", "menu.py"], check=True)
        else:
            rich.print("[bold][red]To get back to menu, Enter : [yellow]menu[/yellow] , or Try again[/red][/bold]")

while (True):
    rich.print("[blue][bold]Enter your username :")
    username = input()
    rich.print("[blue][bold]Enter your password :")
    password = input()
    if (checkuserValidation(username, password)):
        rich.print(f"[green][bold]\nWelcome , [blue]{username}![/blue][/green][/bold]")
        break

time.sleep(2)
subprocess.run(["python", "menu.py"], check=True)
