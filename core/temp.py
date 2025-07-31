import json

# Load JSON
with open('tasks.json', 'r') as f:
    data = json.load(f)

# Show entries
for i, entry in enumerate(data):
    print(f"[{i}] Task: {entry['task']} | Status: {entry['status']} | Progress: {entry['progress']}")

# Choose entry
choice = int(input("\nWhich task number do you want to edit? "))
task = data[choice]

# Edit fields
task['task'] = input(f"New task name (current: {task['task']}): ") or task['task']
task['status'] = input(f"New status (current: {task['status']}): ") or task['status']
task['progress'] = input(f"New progress (current: {task['progress']}): ") or task['progress']

# Save back
with open('tasks.json', 'w') as f:
    json.dump(data, f, indent=4)

print("\n✅ Task updated!")
