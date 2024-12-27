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
# TODO FIX THIS VVVVVV

# rich.print("[violet][bold]to go back to menu , Enter : [yellow]menu[/yellow]\n")
# rich.print("[violet][bold]Enter anything else to continue: [yellow]menu[/yellow]\n")
# s = input()
# if (s == "menu"):
#     subprocess.run(["python", "menu.py"], check=True)
with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def checkinfovalidation(username, email, password):
    if (username.strip() == ""):
        rich.print("[bold][red]Username cannot be empty[/red][bold]")
        return False
    if (" " in username):
        rich.print(
            "[red][bold]Username shouldn't contain any space [bright_yellow](use underline(_) instead)[/bright_yellow]")
        return False
    if (not checkpasswordlength(password)):
        rich.print("[bold][red]Password is too short , Try again [/red][bold]")
        return False
    if (not checkemailpattern(email)):
        rich.print("[bold][red]Enter a valid email , Try again [/red][bold]")
        return False
    for user in users:
        if user["username"] == username:
            rich.print("[bold][red]Username already exists , Try again [/red][bold]")
            return False
        if user["email"] == email:
            rich.print("[bold][red]Email already exists , Try again [/red][bold]")
            return False
    return True


def checkpasswordlength(password):
    return len(password) >= 8


def checkemailpattern(email):
    return re.match(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', email)


def addnewuser(new_user):
    if (checkinfovalidation(new_user["username"], new_user["email"], new_user["password"])):
        users.append(new_user)
        savejson(users)


def getuserinfo():
    user = {
        "username": "",
        "email": "",
        "password": "",
        "rank": "1000",
        "isloggedin": False,
        "isPlayer2": False,
        "uuid": str(uuid.uuid4())
    }
    while (True):
        rich.print("[light_goldenrod3][bold]Enter your username :")
        username = input()
        rich.print("[light_goldenrod3][bold]Enter your email :")
        email = input()
        rich.print("[light_goldenrod3][bold]Enter your password :")
        password = input()
        if (checkinfovalidation(username, email, password)):
            user["username"] = username
            user["password"] = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user["email"] = email
            addnewuser(user)
            rich.print("[green][bold]User added successfully [/green][/bold]")
            break


getuserinfo()
rich.print("[blue][italic]You can Sign in now![/blue][/italic]")
time.sleep(2)
subprocess.run(["python", "menu.py"], check=True)
