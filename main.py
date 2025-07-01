from create import create_log as cr
from update import update_log as up
from lists import list_log as ll
from delete import delete as dl
from quit  import quit_program as qp
from export_excell import export_to_excel as ex
from config import log_dir, ri, pt, datetime
import os

def main():
    os.makedirs(log_dir, exist_ok=True)
    try:
            menu_actions = {
                "n" : cr,
                "u" : up,
                "l" : ll,
                "q" : qp,
                "e" : ex,
                "d" : dl
            }
        
            pt("LOG SYSTEM by KattoWilkatz")
            while True:
                
                print("\n (N) Create New Log")
                print(" (U) Update Exisiting Log")
                print(" (L) Show List Existing Logs")
                print(" (E) Export to excel[WIP_don't use]")
                print(" (D) Delete files")
                print(" (Q) Quit")
            
                choice = input("> ").strip().lower()
                action = menu_actions.get(choice)
            
                if action:
                    action() #Call the corresponding function!
                else:
                    print("Invalid option. Please enter the correct options.")
        
    except KeyboardInterrupt:
        print("\n Log cancelled. No changes made.")
            
if __name__ == "__main__":
    main()
