# Made by an Asian - Phoenixthrush
# Temperature

def celsius_to_kelvin():
    c = float(input("Enter your temperature in Celsius!: "))
    k = c + 273.15
    print()
    print("It would be " + str(k) + " in Kelvin")

def celsius_to_fahrenheit():
    c = float(input("Enter your temperature in Celsius!: "))
    f = 32.0 + 1.8 * c
    print()
    print("It would be " + str(f) + " in Fahrenheit")

def kelvin_to_celsius():
    k = float(input("Enter your temperature in Kelvin!: "))
    c = k - 273.15
    print()
    print("It would be " + str(c) + " in Celsius")

def kelvin_to_fahrenheit():
    k = float(input("Enter your temperature in Kelvin!: "))
    f = k*1.8 - 459.67
    print()
    print("It would be " + str(f) + " in Fahrenheit")

def fahrenheit_to_celsius():
    f = float(input("Enter your temperature in Fahrenheit!: "))
    c = 5.0*(f - 32.0)/9.0
    print()
    print("It would be " + str(c) + " in Celsius")

def fahrenheit_to_kelvin():
    f = float(input("Enter your temperature in Faherenheit!: "))
    k = (f + 459.67)/1.8
    print()
    print("It would be " + str(k) + " in Kelvin")

def temperature():

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

# DDos
# Fake

def ddos_fake():
    import time

    print()
    print("You must insert in every field or the script breaks")
    IP = input("Please specify the destination (google.com): ")
    x = int(input("How many times do you want to ddos (50): "))
    port = int(input("Which port do you want to send the packets to (80): "))

    print()
    x = x + 1
    time.sleep(2)
    for i in range(1,x):
        time.sleep(0.1)
        print("Sended " + str(i) + " Packets to " + str(IP) + " on Port " + str(port))
    time.sleep(2)
    print()
    print("DDOS to " + str(IP) + " finished")
    print("Could not timeout Servers")

# Dick Meter
# Im Gay

def dick_meter():
    import random
    from tkinter import messagebox

    x = random.randint(0,20)

    if x == 0:
        messagebox.showinfo("Dick Meter", "You got no dick haha lmao!")
    elif x == 20:
        messagebox.showinfo("Dick Meter", "Damn dude you got a huge cock!")
    else:
        messagebox.showinfo("Dick Meter", "Damn dude you got a " + str(x) + " centimeter cock!")

# Age Meter

def age_meter():
    from tkinter import messagebox

    print()
    x = input("How old are you? ")
    messagebox.showinfo("Age Meter", "You are " + str(x) + " Years old!")

# High Meter

def high_meter():
    from tkinter import messagebox

    print()
    x = input("How tall are you (in cm)? ")
    messagebox.showinfo("High Meter", "You are " + str(x) + " cm high!")