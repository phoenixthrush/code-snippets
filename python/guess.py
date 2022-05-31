from random import randint

success = False
zahlenraum = input("Wie groß soll der Zahlenraum sein? (0-20): ").split("-")
hidden = randint(int(zahlenraum[0]), int(zahlenraum[1]))
lives = int((int(zahlenraum[1]) - int(zahlenraum[0])) / 5)

while lives > 0 and success is False:
    response = int(input(f"Gib eine Zahl zwischen {zahlenraum[0]} und {zahlenraum[1]} an: "))
    if response < hidden:
        lives -= 1
        if lives == 0:
            print("Du hast keine Leben mehr!")
            break
        print("Die gesuchte Zahl ist größer!")
    elif response > hidden:
        lives -= 1
        if lives == 0:
            print("Du hast keine Leben mehr!")
            break
        print("Die gesuchte Zahl ist kleiner!")
    elif response == hidden:
        print("Glückwunsch du hast die Zahl erraten!")
        success = True
    else:
        print("Fehler!")
