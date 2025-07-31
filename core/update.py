from config import LOG_DIR, JSON_DIR, ri,pt,lt, datetime, rm
from core.convert import converter_entry as ce
from utils.completer import enable_autocomplete
from utils.uxHelper import clear_screen as clss
from pathlib import Path
import os
import json
import readline
import uuid

def json_update():
    enable_autocomplete()
    input_name = ri("Input log name: ").strip().lower()
    filename = f"{input_name}.json"
    json_path = JSON_DIR / f"{filename}"

    #Check if the file is exist or not, returning to main menu when not found
    if not json_path.exists():
        print(f"Log file '{filename}.log' not found !!")
        print("Please create the log file first")
        psc()
        return
    print(f"Log file '{filename}.log' found! Now updating..")

    with open(json_path,"r") as file:
        data = json.load(file)

    while True:
        #Creating or adding new log entry
        pt("Adding log entry")
        task = ri("Input task: ")
        status = ri("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").strip().lower()
        progress = "-"
        if status == "o":
            status_text = "On Progress"
            progress = ri("Progress: ")
            if not progress.endswith("%"): #Check if the % is present or typed by the user or not
                progress += "%"
        elif status == "f":
            status_text = "Finish"
            progress = "100%"
        elif status == "p":
            status_text = "Plan"
            progress = "0%"
        elif status == "c":
            status_text = "Canceled"
            progress = "Canceled"
        else:
            status_text = "Unknown"
            progress = "-"
            print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")
    
    
        if progress.endswith("%"):
            # try:
            #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
            percent_value = int(progress.strip('%'))
            filled_blocks = percent_value // 10
            empty_block = 10 - filled_blocks
            bar = "█" * filled_blocks + "." * empty_block
            progress_bar = f"[{bar}] {percent_value}%"
        else:
            progress_bar = f"[{progress}]"
        detail = input("Input the detail(optional): ")
        timestamp = datetime.now().replace(microsecond=0)
        
        #the Entry
        json_entry = {
                "UUID" : str(uuid.uuid4()),
                "Date and Time" : f"{timestamp}",
                "Task" : task,
                "Status" : status_text,
                "Progress" : progress_bar,
                "Detail" : detail
            }
        data[0]["Content"].append(json_entry)
    
        with open(json_path,"w") as file:
            json.dump(data, file, indent=4)
    
        #convert JSON to txt
        if filename.endswith(".json"):
            filename = filename[:-5] + ".log"
        raw_text = ce(json_path)
        raw_path = LOG_DIR / f"{filename}"
        raw_path.chmod(0o666) #unlock the file to be writeable
        with open(raw_path, 'a', encoding='utf-8') as file:
            file.write(raw_text)
        raw_path.chmod(0o444) #re-lock the file to be read-only
        print(f"\n Log file updated")
        again = input("\n Do you want to add another log entry? (Y/N): ").strip().lower()
        if again != "y":
            clss()
            print("\n Log update session ended.")
            break
