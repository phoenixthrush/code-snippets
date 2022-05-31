# Made by an Asian - Phoenixthrush
# Temperature

def celsius_to_kelvin():
    c = float(input("Enter your temperature in Celsius!: "))
    k = c + 273.15
    print()
    print("It would be " + str(k) + " in Kelvin")
    print("Press Enter to exit!")
    tmp = input()

def celsius_to_fahrenheit():
    c = float(input("Enter your temperature in Celsius!: "))
    f = 32.0 + 1.8 * c
    print()
    print("It would be " + str(f) + " in Fahrenheit")
    print("Press Enter to exit!")
    tmp = input()

def kelvin_to_celsius():
    k = float(input("Enter your temperature in Kelvin!: "))
    c = k - 273.15
    print()
    print("It would be " + str(c) + " in Celsius")
    print("Press Enter to exit!")
    tmp = input()

def kelvin_to_fahrenheit():
    k = float(input("Enter your temperature in Kelvin!: "))
    f = k*1.8 - 459.67
    print()
    print("It would be " + str(f) + " in Fahrenheit")
    print("Press Enter to exit!")
    tmp = input()

def fahrenheit_to_celsius():
    f = float(input("Enter your temperature in Fahrenheit!: "))
    c = 5.0*(f - 32.0)/9.0
    print()
    print("It would be " + str(c) + " in Celsius")
    print("Press Enter to exit!")
    tmp = input()

def fahrenheit_to_kelvin():
    f = float(input("Enter your temperature in Faherenheit!: "))
    k = (f + 459.67)/1.8
    print()
    print("It would be " + str(k) + " in Kelvin")
    print("Press Enter to exit!")
    tmp = input()

def temperature():

    print()
    print("Temperature Converter - Phoenixthrush")
    print()
    print("1 -- Celsius to Kelvin!")
    print("2 -- Celsius to Fahrenheit")
    print("3 -- Kelvin to Celsius")
    print("4 -- Kelvin to Fahrenheit")
    print("5 -- Fahrenheit to Celsius")
    print("6 -- Fahrenheit to Kelvin")
    print()

    x = input("Please enter an option!: ")

    if x == "1":
        celsius_to_kelvin()
    elif x == "2":
        celsius_to_fahrenheit()
    elif x == "3":
        kelvin_to_celsius()
    elif x == "4":
        kelvin_to_fahrenheit()
    elif x == "5":
        fahrenheit_to_celsius()
    elif x == "6":
        fahrenheit_to_kelvin()
    else:
        print("Dude that is not a option!")
        temperature()

if __name__ == "__main__":
    temperature()
