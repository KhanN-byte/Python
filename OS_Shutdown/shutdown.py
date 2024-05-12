import os


shutdown = input("Do you want to shut down the PC? (yes / no): ").lower()  # Convert input to lowercase for case insensitivity

if shutdown == "no":
    exit()
elif shutdown == "yes":
    os.system('/mnt/c/Windows/system32/shutdown.exe /s')
else:
    print("Computer Restarting... \n")
    os.system('/mnt/c/Windows/system32/shutdown.exe /r')



