from utils.completer import enable_autocomplete as ea
from config import LOG_DIR, JSON_DIR,ri
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
        # with open(json_path, "w", encoding="utf-8") as out:
        #     out.write(raw_text)
             
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."
def converter_entry(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        raw_text = ""
        for entry in data[0]["Content"]:
            # print("running")
            uuid = entry.get("UUID", "Unknown")
            clock = entry.get("Date and Time", "Unknown")
            task = entry.get("Task", "Unknown")
            status = entry.get("Status", "Unknown")
            progress = entry.get("Progress", "-")
            detail = entry.get("Detail", "")
            raw_text += (
                f"[UUID] : {uuid}\n"
                f"[Date and Time] : {clock}\n"
                f"[Task] : {task}\n"
                f"[Status] : {status}\n"
                f"[Progress] : {progress}\n"
                f"[Detail] : {detail}\n"
                "-------------------------\n"
            )
        # raw_text = f"UUID: {uuid}\nClock: {clock}\nTags: {tags}\nJournal: {journal}"
        # print(raw_text)
        return raw_text

        # with open(json_path, "w", encoding="utf-8") as out:
        #     out.write(raw_text)
            
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."

def convert_whole():
    ea()
    filename = ri("Input the file to convert to .log from .json: ").strip().lower()
    json_path = JSON_DIR / f"{filename}.json"
    raw_path = LOG_DIR / f"{filename}.log"
    #convert the header first        
    header = converter_title(json_path)
    with open(raw_path, 'w', encoding='utf-8') as file:
        file.write(header)
    raw_path.chmod(0o444)

    #convert the entries after
    entries = converter_entry(json_path)
    raw_path.chmod(0o666)
    with open(raw_path, 'a') as f:
        f.write(entries) 
    raw_path.chmod(0o444)
    #NB: this method is messy,i know, but it's much
    # better than rewrite all the logic for the convert here
