from config import LOG_DIR, JSON_DIR
import json

def converter_title(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        title = data[0].get("Title", "Unknown")
        time = data[0].get("Time of Creation", "Unknown")
        author = data[0].get("Author", "Unknown") 

        raw_text = (
            f"<Title> : {title}\n"
            f"<Time of Creation> : {time}\n"
            f"<Author> : {author}\n\n"
            ">>> Begin Log <<<\n\n"
            
        )
        # raw_text = f"Title: {title}\nTime of Creation: {time}\nAuthor: {author}\n\n"
        return raw_text 
        with open(json_path, "w", encoding="utf-8") as out:
            out.write(raw_text)
             
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."
def converter_entry(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for entry in data[0]["Content"]:

            uuid = entry.get("UUID", "Unknown")
            clock = entry.get("Date and Time", "Unknown")
            task = entry.get("Task", "Unknown")
            status = entry.get("Status", "Unknown")
            progress = entry.get("Progress", "-")
            detail = entry.get("Detail", "")

        raw_text = (
            f"[UUID] : {uuid}\n"
            f"[Date and Time] : {clock}\n"
            f"[Task] : {task}\n"
            f"[Status] : {status}\n"
            f"[Progress] : {progress}\n"
            f"[Detail] : {detail}\n"
            "-------------------------\n"
        )
        # raw_text = f"UUID: {uuid}\nClock: {clock}\nTags: {tags}\nJournal: {journal}"
        return raw_text

        with open(json_path, "w", encoding="utf-8") as out:
            out.write(raw_text)
            
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."
