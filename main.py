from core.create import create_log as cr
from core.update import update_log as up
from core.lists import list_log as ll
from core.delete import delete as dl
from core.quit  import quit_program as qp
from core.export2excell import export_to_excel as ex
from core.edit import edit_log as ed
from core.entryList import list_entries as le
from utils.uxHelper import clear_screen as clss
from config import log_dir, ri, pt, datetime, rm
from pathlib import Path
import time

def main():
    # os.makedirs(log_dir, exist_ok=True)
    Path(log_dir).mkdir(parents=True, exist_ok=True)
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
