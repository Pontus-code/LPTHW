# Learning Python3 the Hard Way. Excercise 36. Designing and Debugging.

from sys import exit

def start():
    print("Welcome to the escape room.")
    print("You're locked inside this room and must find the key to get out.")
    print("To your left is a radio.")
    print("To your right is a chest.")
    print("What to you want to do?")
    print("If you get stuck and need help, just ask for help.")

    while True:

        choice = input("> ")

        if "chest" in choice:
            chest()
        elif "radio" in choice:
            radio()
        elif "help" in choice:
            print("Check out the radio or the chest.")
        else:
            print("I'm sorry I don't understand, try something else.")

def radio():
    morse_code = ('DI DAH DAH DAH DAH', 'DI DI DI DAH DAH', 'DI DI DI DAH DAH', 'DAH DAH DI DI DI')
    print("You approach the radio.")
    print("It repeats a series of high pitched sounds.")
    for i in morse_code:
        print(i)
    print("Thats odd. I wonder if that is some kind of code?")
    print("What do you want to do?")

    while True:

        choice = input("> ")

        if "chest" in choice:
            chest()
        elif "help" in choice:
            print("Have you heard of Morse code?")
        else:
            print("Im sorry I dont understand, please try something else.")

def chest():
    obfuscated_code = ''.join(chr(number) for number in [49, 51, 51, 55])

    print("You approach a small chest.")
    print("It's locked.")
    print("You need a 4-digit code to open the padlock.")
    print("What do you want to do?")

    while True:

        choice = input("> ")

        if "radio" in choice:
            radio()
        elif "help" in choice:
            print("Have you listened to the radio?")
        elif "open" in choice:
            code = (input("Enter a 4 digit code to open the chest: "))
            digits = ''
            for c in code:
                if c.isdigit():
                    digits += c
                if digits == obfuscated_code:
                    finished()       
            else:
                print(f"Im sorry. {code} is not the correct code.")
        else:
            print("I'm sorry I don't understand. Try something else.")

def finished():
    print("You open the chest and inside is the key!")
    print("You can now leave the escape room.")
    print("CONGRATULATIONS!!!") 
    exit(0)

start()