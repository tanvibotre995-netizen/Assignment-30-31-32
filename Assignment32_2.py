import os
import time
from datetime import datetime

file_path = input("Enter file path: ")
log_file = "FileSizeLog.txt"

while True:
    try:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)

            with open(log_file, "a") as f:
                f.write(f"Path: {file_path}\n")
                f.write(f"Size: {size} bytes\n")
                f.write(f"Date & Time: {datetime.now()}\n")
                f.write("-" * 40 + "\n")

            print("File information logged.")

        else:
            print("File does not exist.")

    except Exception as e:
        print("Error:", e)

    time.sleep(30)
