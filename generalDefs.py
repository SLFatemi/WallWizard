import rich


def clear():
    print("\033[2J\033[H", end="")


def printLine():
    rich.print("[royal_blue1]===============WallWizard===============\n")
