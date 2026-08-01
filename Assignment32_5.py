import os
import time

directory = input("Enter directory path: ")
log_file = "DeletedFilesLog.txt"

while True:
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)

                try:
                    if os.path.getsize(path) == 0:
                        os.remove(path)

                        with open(log_file, "a") as log:
                            log.write(path + "\n")

                        print("Deleted:", path)

                except PermissionError:
                    print("Permission denied:", path)

                except Exception as e:
                    print("Error:", e)

    except Exception as e:
        print("Directory Error:", e)

    time.sleep(3600)      # 1 hour
