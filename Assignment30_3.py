import schedule
import time

def Display():
    print("Marvellous Infosystems")

schedule.every(30).minutes.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)
