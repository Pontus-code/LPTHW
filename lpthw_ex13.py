# Learning Python3 the Hard Way - Excercise 13. Parameters, Unpacking, Variables.

# Imports argv from the sys module.
from sys import argv
# read the WYSS section for how to run this
# Assigns the values of the argv list to separate variables, where the first is the name of the file.
script, first, second, third, fourth = argv


# Prints the arguments.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

# Takes an input from the user.
question = input("What was your third argument? --> ")

# Compares the user input to the argument.
if question == third:
    print(f"Correct! Your third argument was {question}.")
else:
    print(f"False! Your third argument was {third}, not {question}.")



