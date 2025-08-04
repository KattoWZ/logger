from utils.completer import enable_autocomplete
from config import JSON_DIR, ri, pt, rm
from utils.uxHelper import pause_and_clear as pcl, clear_screen as clss
from pathlib import Path
import json
import readline

def list_entries():
    enable_autocomplete() #Autocomplete
    filename = ri("Input the file name: ").strip().lower()
    json_path = JSON_DIR / f"{filename}.json"
    with open(json_path, "r") as f:
        data = json.load(f)
        
    #to print the title
    title = data[0]["Title"]
    clss()
    pt(f"{title}")
    #Loop throught the "Content" field to grab all content
    for i, entry in enumerate(data[0]["Content"], start=1):
        uuid = entry.get("UUID", "Unknown")
        clock = entry.get("Date and Time", "Unknown")
        task = entry.get("Task", "Unknown")
        status = entry.get("Status", "Unknown")
        progress = entry.get("Progress", "-")
        detail = entry.get("Detail", "")
            
        print(f"[entry number {i}]")
        print(f"UUID     : {uuid}")
        print(f"Time     : {clock}")
        print(f"Task     : {task}")
        print(f"Status   : {status}")
        print(f"Progress : {progress}")
        print(f"Detail   : {detail}")
        print("-" * 40)
    pcl()
