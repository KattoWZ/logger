import platform
import subprocess

#simple funtion to clear the screen
def clear_screen():
    # os.system('cls' if os.name == 'nt' else 'clear')
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#pause before moving the screen
def pause(msg="Press 'Enter' to continue..."):
    input(msg)
    
#pause before moving the screen and clear the screen after prompt inserted
def pause_and_clear(msg="Press 'Enter' to contine..."):
    input(msg)
    clear_screen()
