import subprocess
import sys
import time
import platform

script_name = "peerHelper.py"

for index in range(5):
    cmd = [sys.executable, script_name, str(index)]
    
    if platform.system() == "Windows":
        subprocess.Popen(["cmd", "/c", "start", "cmd", "/k"] + cmd, shell=True)
    elif platform.system() == "Linux":
        subprocess.Popen(["gnome-terminal", "--"] + cmd)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "python3 {script_name} {index}"'])
    
    time.sleep(6)
