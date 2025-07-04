from create import create_log as cr
from update import update_log as up
from lists import list_log as ll
from delete import delete as dl
from quit  import quit_program as qp
from export_excell import export_to_excel as ex
from edit import edit_log as ed
from config import log_dir, ri, pt, datetime, rm
from utils.uxHelper import clear_screen as clss
from entryList import list_entries as le
import time
import os

def main():
    os.makedirs(log_dir, exist_ok=True)
    menu_actions = {
        "n" : cr,
        "u" : up,
        "l" : ll,
        "q" : qp,
        "x" : ex,
        "d" : dl,
        "e" : ed,
        "le": le
    }
        
    while True:
        try:
            pt("LOG SYSTEM by KattoWilkatz")
            print(" "*10 +  "MAIN MENU")
            print("Insert '!' to return to main menu")            
            print("\n (N) Create New Log")
            print(" (U) Update Exisiting Log")
            print(" (E) Edit Exisiting Log")
            print(" (L) Show List Existing Logs")
            print(" (X) Export to excel[WIP_don't use]")
            print(" (D) Delete files")
            print(" (Q) Quit")
            print(" (LE) lists entries")
        
            choice = input("> ").strip().lower()
            action = menu_actions.get(choice)
        
            if action:
                action() #Call the corresponding function!
            else:
                print("Invalid option. Please enter the correct options.")
        except rm:
            continue
        
        except KeyboardInterrupt:
            print("\n Exit program, exited by user. No changes made.")
            break
if __name__ == "__main__":
    main()
