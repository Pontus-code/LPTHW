# Learning Python3 the Hard Way - Exercise 21. Functions Can Return Something.

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes", what, "Can you do it by hand?")

# Doing the same calculation without the functions.
by_hand = (30 + 5) + ((78 - 4) - ((90 * 2)  * ((100/2) / 2)))
print(f"Yes I can do it by hand...  tadaaa..  {by_hand}")

def repeat(string, number):
    print(f"Repeating {string} {number} times.")
    return string * number
    

# Takes a string input and repeats it by an integer input.
print('\n' + repeat((input("What string do you want to repeat? ")), (int(input("How many times do you want to repeat that string? ")))))

print("\nLets calculate how many seconds there are in a day.")
print("There are 60 seconds in a minute, 60 minutes in an hour and 24 hours in a day.")
print(f"There are {multiply(multiply(60, 60), 24)} seconds in a day.")
 
