from debug import debugEntry as debug
from utils.uxHelper import clear_screen as clss, pause
from pathlib import Path
import re
from config import log_dir,ri

def list_entries():
    print("Insert '!' to return to main menu")            
    filename = ri("Insert the filename:")
    log_path = log_dir / f"{filename}.txt"

    if not log_path.exists():
        print(f"❌ File '{filename}.txt' not found.")
        return []

    content = log_path.read_text(encoding='utf-8')

    #Split the entries
    # entries = content
    # entries = content.split("---")
    entries = [e for e in content.split("---") if e.strip()]
    if not "\[ID\]" in entries[0] and not "[Task]" in entries[0]:
        entries = entries[1:]
    clss()   
    print("\n🐛 DEBUG: Found", len(entries), f"entry chunks from {filename}.txt\n")

    tasks = []
    for i, entry in enumerate(entries):
        entry = entry.strip()
        if not entry:
            continue  # Skip empty entries

        print(f"\n📦 Entry #{i + 1} content:\n{entry}\n")

        
        task_match = re.search(r"\[Task\]\s*:\s*(.+)", entry)
        id_match = re.search(r"\[ID\]\s*:\s*([a-f0-9\-]+)", entry) #that \[ and \] might looks like empty box in other IDE or platform
        
        if task_match and id_match:
            task = task_match.group(1).strip()
            uid = id_match.group(1).strip()
            tasks.append((i, task, uid))
            print(f"✅ Found Task: '{task}' with ID: {uid}")
        else:
            print("⚠️ Task or ID not found in this entry.")

    if tasks:
        print(f"\n📝 Available Log Entries from {filename}.txt:\n")
        for i, task, uid in tasks:
            print(f"{i+1}. Task: {task} | ID: {uid}")
        
    else:
        print("⚠️ No valid entries found.")

    debug(entry, task, uid, i, entries)
    pause()
    return tasks
    








