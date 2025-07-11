from pathlib import Path
import re
from config import log_dir,ri

def list_entries():
    filename = ri("Input:")
    log_path = log_dir / f"{filename}.txt")

    if not log_path.exists():
        print(f"❌ File '{filename}.txt' not found.")
        return []

    with open(log_path, "r") as file:
        content = file.read()

    entries = re.split(r"-{5,}", content)  # Split by lines like -----
    tasks = []

    print("\n🐛 DEBUG: Found", len(entries), "entry chunks\n")

    for i, entry in enumerate(entries):
        entry = entry.strip()
        if not entry:
            continue  # Skip empty entries
    
        print(f"\n📦 Entry #{i + 1} content:\n{entry}\n")
    
        task_match = re.search(r"\s*Task\s*\s*:\s*(.+)", entry)
        id_match = re.search(r"\s*ID\s*\s*:\s*([a-f0-9\-]+)", entry)
    
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

    return tasks
