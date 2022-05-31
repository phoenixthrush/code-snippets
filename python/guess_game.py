import os

class idk():
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
            os.system("cls")
            print("\033[96mreenter idk\033[00m")
        if idk.guessing == idk.hiddennumber:
            print("\033[31myou won uh ye\033[00m")
            exit()
        else:
            print("\033[96mwrong number\033[00m")
            idk.guessingcount = idk.guessingcount + 1
            main()
            exit()

    print("\033[31myeah out of guesses wtf\033[00m")

main()
