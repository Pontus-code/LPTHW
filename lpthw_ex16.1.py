# Learning Python3 the Hard Way - Excercise 16. Reading and Writing Files.

# Script that reads a file. 

from sys import argv

script, filename = argv

print(f"Opening '{filename}'.")
f = open(filename, 'r')

print(f"Printing the contents of '{filename}':\n")
print(f.read())

print(f"And finally, we close '{filename}'.")
f.close()
