import subprocess
import sys
import time
import platform
import os

script_name = "peerHelper.py"
NUMBER_OF_PEERS = 5

for index in range(NUMBER_OF_PEERS):
    cmd = [sys.executable, script_name, str(index), str(NUMBER_OF_PEERS)]
    
    if platform.system() == "Windows":
        subprocess.Popen(["cmd", "/c", "start", "cmd", "/k"] + cmd, shell=True)
    elif platform.system() == "Linux":
        subprocess.Popen(["gnome-terminal", "--"] + cmd)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "python3 {script_name} {index}"'])
    
    time.sleep(6)

os.remove("degreeCount.txt")