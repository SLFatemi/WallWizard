import rich
import time


def clear():
    print("\033[2J\033[H", end="")


def printLine():
    rich.print("[royal_blue1]==================== WallWizard ====================\n")


def loading(color="cyan1", length=4):
    i = 0
    while (i < length):
        print("\033[A                             \033[A")
        rich.print(f"\n[{color}][bold]\t\t\t|")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print(f"[{color}][bold]\t\t\t/")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print(f"[{color}][bold]\t\t\t-")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        rich.print(f"[{color}][bold]\t\t\t\\")
        time.sleep(0.15)
        print("\033[A                             \033[A")
        i += 1
