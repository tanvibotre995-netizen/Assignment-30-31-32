import schedule
import time
import os
from datetime import datetime

def CreateLogFile():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    # File name (24-hour format)
    filename = "Logs/MarvellousLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as fobj:
        # Creation time (12-hour format with AM/PM)
        creation_time = datetime.now().strftime("%d_%m_%Y %I:%M:%S %p")
        fobj.write("Creation Time : " + creation_time + "\n")
        fobj.write("Log file created successfully")

    print("Created:", filename)

schedule.every(10).minutes.do(CreateLogFile)

while True:
    schedule.run_pending()
    time.sleep(1)
