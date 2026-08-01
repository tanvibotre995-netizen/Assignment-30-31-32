import os
import schedule
import time
from datetime import datetime

def count_files():
    directory = input("Enter directory path: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    file_count = sum(
        1 for item in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, item))
    )

    with open("DirectoryCountLog.txt", "a") as file:
        file.write(f"Directory Path : {directory}\n")
        file.write(f"Number of Files: {file_count}\n")
        file.write(f"Date & Time    : {datetime.now()}\n")
        file.write("-" * 40 + "\n")

    print("Log updated successfully.")

directory = input("Enter directory path: ")

def log_directory():
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    file_count = sum(
        1 for item in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, item))
    )

    with open("DirectoryCountLog.txt", "a") as file:
        file.write(f"Directory Path : {directory}\n")
        file.write(f"Number of Files: {file_count}\n")
        file.write(f"Date & Time    : {datetime.now()}\n")
        file.write("-" * 40 + "\n")

    print("Log Updated")

schedule.every(5).minutes.do(log_directory)

print("Monitoring started...")

while True:
    schedule.run_pending()
    time.sleep(1)
