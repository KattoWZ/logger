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
        
    print("\n🐛 DEBUG: Found", len(entries), "entry chunks\n")

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
        print("\n📝 Available Log Entries:\n")
        for i, task, uid in tasks:
            print(f"{i+1}. Task: {task} | ID: {uid}")
        
    else:
        print("⚠️ No valid entries found.")

    # print(f"[DEBUG] Raw entry:\n{entry}")
    # print(f"[DEBUG] Extracted → Task: {task}, ID: {uid}")

    # print(f"\nIndex i = {i}, Entry #{i + 1}\n")

    # for i, entry in enumerate(entries):
    #     print(f"Index i = {i}, Entry #{i + 1}")
    #     print(f"{entry}")
    # print(f"\n📊 Total valid entries: {len(entries)}\n")

    # print(f"\n📦 Entry #{i + 1} (index i = {i})\n{entry}\n")
    pause()
    return tasks
    








