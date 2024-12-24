from markdown_it.common.utils import isWhiteSpace

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
# s = bcrypt.hashpw(b"12345", bcrypt.gensalt())
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
        rich.print("[bold][red]Username cannot be empty [/red][bold]")
        return False
    if (not checkpasswordlength(password)):
        rich.print("[bold][red]Your passowrd is too short , Try again [/red][bold]")
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
        "uuid": str(uuid.uuid4())
    }
    while (True):
        username = input("Enter your username : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        if (checkinfovalidation(username, email, password)):
            user["username"] = username
            user["password"] = password
            user["email"] = email
            addnewuser(user)
            rich.print("[green][bold]User added successfully [/green][/bold]")
            break


getuserinfo()
rich.print("[blue][italic]You can Sign in now![/blue][/italic]")
time.sleep(2)
subprocess.run(["python", "menu.py"], check=True)
