import os
import shutil
import time

source = input("Enter source directory: ")
destination = input("Enter destination directory: ")

log_file = "CopyLog.txt"

while True:
    try:
        if not os.path.isdir(source):
            print("Invalid source directory.")
            break

        if not os.path.isdir(destination):
            print("Invalid destination directory.")
            break

        for file in os.listdir(source):
            if file.endswith(".txt"):
                src = os.path.join(source, file)
                dest = os.path.join(destination, file)

                try:
                    shutil.copy2(src, dest)

                    with open(log_file, "a") as log:
                        log.write(f"Copied: {file}\n")

                    print(file, "copied.")

                except Exception as e:
                    print(f"Could not copy {file}: {e}")

    except Exception as e:
        print("Error:", e)

    time.sleep(600)      # 10 minutes
