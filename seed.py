import subprocess
import platform
import os

# Ensure necessary directories exist
for directory in ["bin/servers", "bin/clients"]:
    os.makedirs(directory, exist_ok=True)

config_file = "config.csv"

# Read configuration and launch servers
with open(config_file, "r") as file:
    next(file)  # Skip header line
    for entry in file:
        details = entry.strip().split(",")
        if len(details) != 3:
            continue  # Ignore malformed lines

        ip_address, port_number, node_identifier = details
        script_cmd = [os.sys.executable, "seedHelper.py", port_number, node_identifier]

        print(f"Launching server at port {port_number} with node ID {node_identifier}")

        system_type = platform.system()
        if system_type == "Windows":
            subprocess.Popen(["cmd", "/c", "start", "cmd", "/k"] + script_cmd, shell=True)
        elif system_type == "Linux":
            subprocess.Popen(["gnome-terminal", "--"] + script_cmd)
        elif system_type == "Darwin":  # macOS
            subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "python3 echo-server.py {port_number} {node_identifier}"'])
