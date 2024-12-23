import rich
import subprocess


def clear():
    print("\033[2J\033[H", end="")


def printMenu(n, menu):
    rich.print("[blue]===============WallWizard================[/blue]")
    print()
    if (n == -1):
        return
    for _ in menu:
        if (menu.index(_) == n):
            rich.print(f" ▶ [yellow]{_}[/yellow]")
        else:
            print(_)


def checkmenuinput(ch, n):
    expectedinputs = ['D', 'd', 'U', 'u']
    if (ch in expectedinputs):
        if (expectedinputs.index(ch) < 2):
            if (n != len(menulist) - 1):
                return n + 1
            print()
            rich.print("[bold]You can't move any lower[/bold]")
            return -1
        else:
            if (n != 0):
                return n - 1
            print()
            rich.print("[bold]You can't move any higher[/bold]")
            return -1
    else:
        return -1


def selectedMenu(n):
    script_map = {
        0: "manageUsers/signin.py",
        1: "manageUsers/register.py",
        2: "start.py",
        3: "exit.py"
    }
    script_to_run = script_map.get(n)
    subprocess.run(["python", script_to_run], check=True)
    exit()


menulist = ["Sign in", "Register", "Start", "Exit"]
n = 0
printMenu(n, menulist)
while (True):
    rich.print("[bold]Use 'U' to go up , and 'D' to go down and Use 'Space' to select :[/bold]")
    menuinput = input("")
    if (menuinput == " "):
        selectedMenu(n)
    clear()
    inp = checkmenuinput(menuinput, n)
    printMenu(inp, menulist)
    if (inp != -1):
        n = inp
