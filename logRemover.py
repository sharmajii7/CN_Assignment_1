import os
import shutil

bin_folder = "logs"

if os.path.exists(bin_folder):
    shutil.rmtree(bin_folder)
else:
    print(f"{bin_folder} directory not found.")
