# Learning Python3 the Hard Way - Excercise 15. Reading Files.

# Imports argv from sys module
from sys import argv

# Assigns arguments to string variables.
script, filename = argv

# Opens a file with the filename provided as an argument, and assigns it to a file object.
txt = open(filename)

# Prints a format string.
print(f"Here's your file {filename}:")
# Prints the contents of the file.
print(txt.read())
# Closes the file.
txt.close()

# Prints a string.
print("Type the filename again:")
# Prompts the user for an input string and assigns it to a string variable.
file_again = input("> ")

# Opens a file.
txt_again = open(file_again)

# Prints the contents of that file.
print(txt_again.read())
# Closes the file.
txt_again.close()
