import os
import time
import schedule
from datetime import datetime


if not os.path.exists("Logs"):
    os.mkdir("Logs")

def CreateTextFile():
    now = datetime.now()

   
    filename = "Logs/Log_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

   
    with open(filename, "w") as fobj:
        fobj.write(f"File Name     : {os.path.basename(filename)}\n")
        fobj.write(f"Creation Date : {now.strftime('%d_%m_%Y')}\n")
        fobj.write(f"Creation Time : {now.strftime('%I:%M:%S %p')}\n")

    print(f"{filename} created successfully.")


schedule.every(1).minutes.do(CreateTextFile)

print("File creation scheduler started...")


CreateTextFile()

while True:
    schedule.run_pending()
    time.sleep(1)
