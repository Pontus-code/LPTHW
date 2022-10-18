# Learning Python 3 the Hard Way - Exercise 7. More Printing.

# Prints a string.
print("Mary had a little lamb.")
# Prints a formatted string.
print("Its fleece was white as {}.".format('snow'))
# Prints a string.
print("And everywhere that Mary went.")
# Prints a string multiple times.
print("." * 10) # what'd that do?

# Assigns a string to a variable.
end1 = "C"
# Assigns a string to a variable.
end2 = "h"
# Assigns a string to a variable.
end3 = "e"
# Assigns a string to a variable.
end4 = "e"
# Assigns a string to a variable.
end5 = "s"
# Assigns a string to a variable.
end6 = "e"
# Assigns a string to a variable.
end7 = "B"
# Assigns a string to a variable.
end8 = "u"
# Assigns a string to a variable.
end9 = "r"
# Assigns a string to a variable.
end10 = "g"
# Assigns a string to a variable.
end11 = "e"
# Assigns a string to a variable.
end12 = "r"

# All work and no play makes Jack a dull boy.

# Watch that comma at the end. Try removing it to see what happens.
# It results in a syntax error.

# Prints several string variables and defines a delimeter at the end of the string.
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
# Prints many string variables.
print(end7 + end8 + end9 + end10 + end11 + end12)

# Prints 50 octothorpes.
print("#" * 50)
# Defines a function that will print the variables using a for loop.
def cheesefunction():
    for i in range(12):
        print(eval("end" + str(i+1)), end='')
# Prints a string with many punctuations and no new line at the end.
print("I like" + "." * 30, end='')
# Calls the print function at the end of the printed line above.
cheesefunction()
# Let's assign the output of the for loop to a variable instead.
# Defines a global string variable.
cheesevariable = ""
# Loops through the variables and adds them to the new variable.
for i in range(12):
    cheesevariable += eval("end" + str(i+1))
# Creates a new line.
print("")
# Prints the same line as above using the string variable.
print("I like" + "." * 30 + cheesevariable)

	


