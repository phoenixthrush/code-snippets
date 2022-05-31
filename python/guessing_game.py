import os

class idk:
    guessingcount = 0
    hiddennumber = 5
    guessing = ""
    guessingLimit = 3

def main():
    os.system("cls")
    while idk.guessingcount < idk.guessingLimit:
        try:
            idk.guessing = int(input("\033[31mEnter ur number: \033[00m"))
        except ValueError:
            main()
            exit()
        if idk.guessing == idk.hiddennumber:
            print("\033[31myou won uh ye\033[00m\n")
            print("\033[96mPress enter to exit!\033[00m")
            os.system("pause >nul")
            exit()
        else:
            print("\033[96mwrong number\033[00m\n")
            idk.guessingcount = idk.guessingcount + 1
            print("\033[96mPress enter to retry!\033[00m")
            os.system("pause >nul")
            main()
            exit()

    print("\033[31myeah out of guesses wtf\033[00m")
    print("\033[96mPress enter to exit!\033[00m")
    os.system("pause >nul")
    exit()

main()