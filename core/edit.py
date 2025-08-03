from utils.completer import enable_autocomplete
from config import JSON_DIR, ri, pt, rm, LOG_DIR
from core.convert import converter_entry as ce, converter_title as ct, convert
from utils.uxHelper import pause_and_clear as pcl, clear_screen as clss
from utils.progress_status import get_progress_optional,get_status_optional
from pathlib import Path
import json
import readline

def edit_entries():
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
        
        
        task = entry.get("Task", "Unknown")
        status = entry.get("Status", "")
        progress = entry.get("Progress", "-")
        detail = entry.get("Detail", "")
                   
        print(f"[entry number {i}]")        
        print(f"Task     : {task}")
        print(f"Status   : {status}")
        print(f"Progress : {progress}")
        print(f"Detail   : {detail}")
        print("-" * 40)

    choice = int(input("\nWhich task number do you want to edit? "))-1 #-1 is because index start with 0, not 1
    edit_entry = data[0]["Content"][choice]
    # TODO : make the edit as an option, what field the user want's to edit
    edit_entry['Task'] = input(f"New Task (current: {edit_entry['Task']}): ") or edit_entry['Task']
    print(f"New Task: {edit_entry['Task']}")

    print(f"Current Status: {edit_entry['Status']}")
    edit_entry['Status'] = get_status_optional() or edit_entry['Status']
    print(f"New Status: {edit_entry['Status']}")

    print(f"Current Progress: {edit_entry['Progress']}")
    edit_entry['Progress'] = get_progress_optional(edit_entry['Status'], edit_entry['Progress'])
    print(f"New Progress: {edit_entry['Progress']}")

    edit_entry['Detail'] = input(f"New Detail (current: {edit_entry['Detail']}): ") or edit_entry['Detail']
    

    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

    #convert everything back to .log
    raw_path = LOG_DIR / f"{filename}.log"
    raw_path.chmod(0o666) #unlock the file to be writeable
    convert(json_path, raw_path)
    raw_path.chmod(0o444) #re-lock the file to be read-only
    print("\n✅ Task updated!")
