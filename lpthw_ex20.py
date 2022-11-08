# Learning Python3 the Hard Way - Exercise 20. Functions and Files.

# Imports argv from sys module.
from sys import argv

# Unpacks the argv list to the variables script and input_file.
script, input_file = argv

# Defines a function that reads a file.
def print_all(f):
    print(f.read())

# Defines a function that sets the pointer to the beginning of the line.
def rewind(f):
    f.seek(0)

# Defins a function that prints a specific line from the file.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Opens a file and assigns it to a file object.
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Sets a counter to 1.
current_line = 1
print_a_line(current_line, current_file)

# Sets the counter to 2.
current_line += 1
print_a_line(current_line, current_file)

# Sets the counter to 3.
current_line += 1
print_a_line(current_line, current_file)


# Reading lines and rewinding in the middle of it.
current_file.seek(0)
print(current_file.readline(), end = "")
print(current_file.readline())
current_file.seek(0)
print(current_file.readline())
print(current_file.readline())
print(current_file.readline())

