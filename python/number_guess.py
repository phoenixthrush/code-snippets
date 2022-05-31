import random
number = random.randint(0, 100)
number_of_guesses = 1

while number_of_guesses < 6:
    print("This is your " + str(number_of_guesses) + " try!")
    guess = int(input("Please enter your guess (between 0 and 100): "))
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
        print()
    if guess > number:
        print("Your guess is too high")
        print()
    if guess == number:
        break
if guess == number:
    print("You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("You did not guess the number, The number was " + str(number))
