from config import log_dir, ri, pt, datetime
from utils.uxHelper import pause_and_clear as psc
import uuid
import os

#updating existing log file
def update_log():
    pt("Log Updater")
    entry_id = str(uuid.uuid4())
    doc = ri("Input log file name: ").strip().lower()
    filepath = log_dir /  f"{doc}.txt"

    #check if file exists
    if not os.path.exists(filepath):
        print(f"Log file '{doc}.txt' not found in '{log_dir}/' directory")
        print("Please create the log file first before updating.")
        psc()
        return #Don't continue, just exit the function
    print(f"Log file found! Now updating '{doc}.txt'...")

    while True:
        print("\n----- Adding new entry ------")

        task = ri("Input task: ")
        status = ri("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").lower()
        #intrepet the progress based on status options
        progress = "-" #default progress value
        if status == "o":
            status_text = "On Progress"
            progress = ri("Progress: ")
            if not progress.endswith("%"): #Check if the % is present or typed by the user or not
                progress += "%"
        elif status == "f":
                status_text = "Finish"
                progress = "100%"
        elif status == "p":
                status_text = "Plan"
                progress = "0%"
        elif status == "c":
                status_text = "Canceled"
                progress = "Canceled"
        else:
                status_text = "Unknown"
                progress = "-"
                print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")

        if progress.endswith("%"):
            # try:
            #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
            percent_value = int(progress.strip('%'))
            filled_blocks = percent_value // 10
            empty_block = 10 - filled_blocks
            bar = "█" * filled_blocks + "." * empty_block
            progress_bar = f"[{bar}] {percent_value}%"
            # except:
            #     progress_bar = f"[{progress}]"
        else:
            progress_bar = f"[{progress}]"
        detail = input("Input the detail(optional): ")
        timestamp = datetime.now().replace(microsecond=0)
            #writing the input into the log entry
        log_entry = (
            "\n------------------------------\n"
            f"[{timestamp}]\n"
            f"[ID] :{entry_id}\n"
            f"[Task] :{task} \n"
            f"[Status] :{status_text} \n"
            f"[Progress] :{progress_bar} \n"
            f"[Detail] :{detail} \n"
            )
        with open(filepath,"a") as file:
            file.write(log_entry)
        
        print(f"\n Log sucessfully saved to '{filepath}'")
        again = input("\n Do you want to add another log? (Y/N): ").strip().lower()
        if again != "y":
            print("\n Logging session ended.")
            break
#EOL Updating log funtion        

