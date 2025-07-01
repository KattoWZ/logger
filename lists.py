from config import  log_dir, ri, pt
import os

#listing existing log file
def list_log():
    pt("Log List")
    if not os.path.exists(log_dir): #check if the log/ dir is exist, and create the dir if missing or not exist
        os.makedirs(log_dir)
        print("`{log_dir}/` is missing, created the directory\n")

    files = [f for f in os.listdir(log_dir) if f.endswith(".txt")] 

    if files:
        print("Available log files: ")
        for f in files:
            print(f" - {f}")
            # print("\n")
    else:
        print("No log files found yet. \n")
    print("===============================")
#EOL List function
