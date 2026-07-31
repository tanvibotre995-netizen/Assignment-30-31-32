import schedule
import time
import datetime

def DisplayDateTime():
    current = datetime.datetime.now()
    print("Current Date and Time:", current)

schedule.every(1).minutes.do(DisplayDateTime)

while True:
    schedule.run_pending()
    time.sleep(1)
