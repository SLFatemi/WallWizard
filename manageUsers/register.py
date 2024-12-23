from markdown_it.common.utils import isWhiteSpace
import generalDefs as methods
import bcrypt
import re
import rich
import json
import uuid
import subprocess

# s = bcrypt.hashpw(b"12345", bcrypt.gensalt())

with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def checkUsername(username):
    if (isWhiteSpace(username)):
        rich.print("[bold][red] Username cannot be empty [/red][bold]")
        return False


def checkpasswordlength(password):
    return len(password) >= 8


def checkemailpattern(email):
    return re.match(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', email)


methods.clear()
methods.printLine()

rich.print("[bold][/bold]")
