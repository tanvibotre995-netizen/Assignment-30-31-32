import schedule
import time

def DisplayMessage(message):
    print(message)

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval > 0:
    schedule.every(interval).seconds.do(DisplayMessage, message)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("Interval should be greater than zero")
