import os
import re #to enable the program to search or extract from files
from config import log_dir
from utils.titleUI import print_title as pt

def edit_log():
    pt("EDIT LOG ENTRY")

    # Step 1: Ask user which file to edit
    filename = input("Which log file do you want to edit (without .txt)? ").strip().lower()
    filepath = os.path.join(log_dir, f"{filename}.txt")

    if not os.path.exists(filepath):
        print("File not found.")
        return

    # Step 2: Read and extract entries
    with open(filepath, "r") as file: #'r' mode means the file is on 'read' mode only
        content = file.read()

    entries = re.split(r"-{5,}", content) #that r" are for escape sequence, means treating '/' or '\' as just regular char
    tasks = []
    for i, entry in enumerate(entries):
        match = re.search(r"Task ?: ?(.*)", entry)
        uid = re.search(r"ID ?: ?(.*)", entry)
        if match and uid:
            tasks.append((i, match.group(1), uid.group(1)))

    if not tasks:
        print("No editable tasks found.")
        return

    # Step 3: Show options to the user
    for i, (index, task, uid) in enumerate(tasks, start=1):
        print(f"{i}. {task} (ID: {uid})")

    # Step 4: Ask user which to edit
    choice = input("Which task number do you want to edit? ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("Invalid selection.")
        return

    entry_index = tasks[int(choice) - 1][0]
    entry_list = entries[entry_index].strip().splitlines()

    # Step 5: Ask which field to edit
    print("\nEditable fields: Task / Status / Progress / Detail")
    field = input("Which field do you want to edit? ").strip().lower()
    new_value = input("New value: ").strip()

    updated_lines = []
    for line in entry_list:
        if f"[{field.capitalize()}]" in line:
            updated_lines.append(f"[{field.capitalize()}] :{new_value}")
        else:
            updated_lines.append(line)

    # Step 6: Rebuild entries and save
    entries[entry_index] = "\n" + "\n".join(updated_lines)
    with open(filepath, "w") as file:
        file.write("\n------------------------------\n".join(entries))

    print("Log entry updated.")
