import schedule
import time

def Display():
    print("Jay Ganesh")

schedule.every(2).seconds.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)
