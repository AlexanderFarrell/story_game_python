import time

seconds_per_message = 1

def narrate(message):
    print(message)
    time.sleep(seconds_per_message)

def speak(speaker, message):
    narrate(f"{speaker}: {message}")

def yes():
    while True:
        choice = input("Yes or no?: ")
        choice = choice.lower()

        if choice == "yes" or choice == "y":
            return True
        elif choice == "no" or choice == 'n':
            return False
        else:
            print("Please enter yes or no")

def choose(options):
    while True:
        print("What would you like to do?")
        for i, o in enumerate(options):
            print(f" {i+1}. {o}")
        choice = input("Type a number: ")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(options):
                return options[choice-1]
        print("Please enter a valid number")

