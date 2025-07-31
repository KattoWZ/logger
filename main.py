from core.create import json_create as jc
from core.update import json_update as ju
from core.lists import list_log as ll
from core.delete import delete as dl
from core.quit  import quit_program as qp
from core.export2excell import export_to_excel as ex
from core.read import read_log as rd
from core.entryListJSON import list_entries as le
from core.edit import edit_entries as ee
from core.convert import convert_whole as cw
from utils.uxHelper import clear_screen as clss
from config import LOG_DIR, JSON_DIR, ri, pt, datetime, rm
from pathlib import Path
import time

def main():
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    Path(JSON_DIR).mkdir(parents=True, exist_ok=True)
    menu_actions = {
        "n" : jc,
        "u" : ju,
        "e" : ee,
        "l" : ll,
        "q" : qp,
        "x" : ex,
        "d" : dl,
        "r" : rd,
        "le": le,
        "cw" : cw
    }
        
    while True:
        try:
            pt("LOG SYSTEM by KattoWilkatz")
            print(" "*10 +  "MAIN MENU")
            print("Insert '!' to return to main menu")            
            print("\n (N) Create New Log")
            print(" (U) Update Exisiting Log")
            print(" (R) Read Exisiting Log")
            print(" (E) Edit Exisiting Log")
            print(" (L) Show List Existing Logs")
            print(" (X) Export to excel[WIP_don't use]")
            print(" (D) Delete files")
            print(" (Q) Quit")
            print(" (LE) lists entries")
            print(" (CW) Convert JSON to log")
        
            choice = input("> ").strip().lower()
            action = menu_actions.get(choice)
        
            if action:
                action() #Call the corresponding function!
            else:
                clss()
                print(f"'{choice}' is an Invalid option. Please enter the correct options.")
            # print("hello")
        except rm:
            continue
        except KeyboardInterrupt:
            print("\n Exit program, exited by user. No changes made.")
            break
if __name__ == "__main__":
    main()
