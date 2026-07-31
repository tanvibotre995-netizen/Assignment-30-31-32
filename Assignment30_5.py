import schedule
import time
from datetime import datetime

def Task():
    fobj = open("Marvellous.txt", "a")
    fobj.write("Task executed at : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.close()

schedule.every(5).minutes.do(Task)

while True:
    schedule.run_pending()
    time.sleep(1)
