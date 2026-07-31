import schedule
import time
import shutil
import os
from datetime import datetime

def Backup():
    source = input("Enter source file path: ")
    destination = input("Enter destination directory path: ")

    current = datetime.now()

    filename = os.path.basename(source)
    
    backup_name = filename.split(".")[0] + "_" + current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    destination_file = os.path.join(destination, backup_name)

    shutil.copy(source, destination_file)

    with open("backup_log.txt", "a") as fobj:
        fobj.write("Backup completed successfully at : " + 
                   current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print("Backup completed successfully")


# Execute backup every hour
schedule.every(1).hour.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)
