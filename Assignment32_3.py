import os
import time

file_path = input("Enter text file path: ")

while True:
    try:
        if not os.path.exists(file_path):
            print("Error: File does not exist.")

        elif os.path.getsize(file_path) == 0:
            print("Error: File is empty.")

        else:
            with open(file_path, "r") as f:
                print("\n----- File Content -----")
                print(f.read())
                print("------------------------")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError:
        print("Error: File cannot be opened.")

    except Exception as e:
        print("Error:", e)

    time.sleep(60)
