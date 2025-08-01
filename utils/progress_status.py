from config import ri

def status():
    status = ri("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").strip().lower()
    if status == "o":
        status_text = "On Progress"
    elif status == "f":
        status_text = "Finish"
    elif status == "p":
        status_text = "Plan"
    elif status == "c":
        status_text = "Canceled"
    else:
        status_text = "Unknown"
        print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")

    return status

def progress(status):
    if status == "o":
        progress = ri("Progress: ")
        if not progress.endswith("%"):
            progress += "%"
    elif status == "f":
        progress = "100%"
    elif status == "p":
        progress = "0%"
    elif status == "c":
        progress = "Canceled"
    else:
        progress = "-"

    if progress.endswith("%"):
        try:
        #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
            percent_value = int(progress.strip('%'))
            filled_blocks = percent_value // 10
            empty_block = 10 - filled_blocks
            bar = "█" * filled_blocks + "." * empty_block
            progress_bar = f"[{bar}] {percent_value}%"
        except ValueError:
            progress_bar = "invalid"
    else:
        progress_bar = f"[{progress}]"
    
