from config import  log_dir, ri, pt
from pathlib import Path

#Delete Program
def delete():
    print("Insert '!' to return to main menu")            
    pt("Purge the FILE")
    doc = ri("Insert the name of the file to be removed: ").strip().lower()
    filepath = log_dir / f"{doc}.txt"
    if filepath.exists():
        print("\n===============================")
        print(f"Log file '{doc}.txt' is FOUND")
        print("===============================")
    else:
        print("\n===============================")
        print(f"Log file '{doc}.txt' is NOT FOUND")
        print("===============================")
        return #exit the funtion to let user to check the lists
    delConfirmation = ri(f"Are you sure to remove the {doc}.txt file? (Y/N): ").strip().lower()
    if delConfirmation == 'y':
        filepath.unlink()
        print("\n===============================")
        print(f"'{doc}.txt' has been removed")
        print("===============================")
    else:
        print("\n Canceling")
        return #canceling and exitting the funtion    
#EOL Delete Program
