import schedule
import time

def monday_task():
    print("Start your weekly goals")

def wednesday_task():
    print("Review your weekly progress")

def friday_task():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(monday_task)
schedule.every().wednesday.at("17:00").do(wednesday_task)
schedule.every().friday.at("18:00").do(friday_task)

print("Scheduler is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
