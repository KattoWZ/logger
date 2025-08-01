from config import LOG_DIR, JSON_DIR, ri,pt,lt, datetime, rm
from core.convert import converter_entry as ce
from utils.completer import enable_autocomplete
from utils.uxHelper import clear_screen as clss
from utils.progress_status import status, progress
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
        stats = status()
        print(stats)
        prog = progress(status)
        detail = input("Input the detail(optional): ")
        timestamp = datetime.now().replace(microsecond=0)
        
        #the Entry
        json_entry = {
                "UUID" : str(uuid.uuid4()),
                "Date and Time" : f"{timestamp}",
                "Task" : task,
                "Status" : stats,
                "Progress" : prog,
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
