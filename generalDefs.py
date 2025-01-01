import rich
import time


def clear():
    print("\033[2J\033[H", end="")


def printLine():
    rich.print("[royal_blue1]==================== WallWizard ====================\n")


def loading():
    i = 0
    while (i < 4):
        print("\033[A                             \033[A")
        rich.print("\n[cyan1][bold]\t\t\t|")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print("[cyan1][bold]\t\t\t/")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print("[cyan1][bold]\t\t\t-")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print("[cyan1][bold]\t\t\t\\")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        i += 1
