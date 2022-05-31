import os
import random

def die_or_survive():
    os.system("cls")
    x = random.randint(0,1)
    if x == 1:
        print("You survived!")
        print("damn you got luck bitch!")
        exit()
    else:
        if os.path.exists("%temp%\\rick.mp4"):
            os.system("%temp%\\rick.mp4")
        if os.path.exists("%temp%\\rick.zip"):
            os.system("%temp%\\rick.zip")

        os.system("bitsadmin /transfer mydownloadjob /download /priority foreground \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/rick.zip\" \"%temp%\\rick.zip\"")
        os.system("powershell -c \"Expand-Archive %temp%\\rick.zip %temp% -Force\"")
        os.system("del %temp%\\rick.zip")
        os.system("start %temp%\\rick.mp4")
        exit()

def menue():
    os.system("cls")
    print("You have a 50 percent chance to surive!")
    print("If you fail all your data will be lost!")
    print()
    choice = input("Do you really want to continue? [y|n] ")

    if choice == "y":
        print("continues!")
    elif choice == "n":
        print("exiting!")
        exit()
    else:
        menue()
        exit()

menue()
die_or_survive()

