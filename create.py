from config import  log_dir, ri, pt, datetime,rm
from pathlib import Path
import os

#creating a log file
def create_log():
    pt("Create Log")
    while True:
        doc = ri("Input file name to generate (without .txt): ").lower()
        filepath = log_dir / f"{doc}.txt"

        if filepath.exists(): #change this to use pathlib later
            print("The log file is already exists, Try a different name.")
        else:
            break #no same file name, proceed to create new file
       
    name = ri("Input name for HEADER: ")
    author = ri("Input the author name: ")
    timestamp = datetime.now().replace(microsecond=0)

    log_entry = (
        pt(f"{name.upper()} LOGS") + "\n" +
        f"[Date of Creation] : {timestamp}\n"
        f"[Author] : {author.upper()}\n"
        
    )

    with open(filepath,"a") as file:
        file.write(log_entry)
        print(f"\n '{doc}.txt' file sucessfully created in '{log_dir}/{doc}.txt'")
#EOL create file log
