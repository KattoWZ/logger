import time
from utils.uxHelper import clear_screen as clss

class ReturnToMenu(Exception):
    pass
def reqInput(prompt):
    while True:
        value = input(prompt).strip()
        if value == "!":
            print("Returning to main menu.\n")
            time.sleep(0.5)
            clss()
            raise ReturnToMenu
        if value:
            return value
        else:
            print("!!!! This Field is REQUIRED. Please try again.")
