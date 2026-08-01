import os
import schedule
import time
from datetime import datetime

def ScanDirectory():
    path = input_path

    file_count = 0
    folder_count = 0

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            file_count += 1

        elif os.path.isdir(full_path):
            folder_count += 1

    print("Directory Scanned:", path)
    print("Total Files:", file_count)
    print("Total Subdirectories:", folder_count)
    print("Scan Time:", datetime.now())
    print("---------------------------")


input_path = input("Enter directory path: ")

schedule.every(1).minutes.do(ScanDirectory)

while True:
    schedule.run_pending()
    time.sleep(1)
