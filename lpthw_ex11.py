# Learning Python3 the Hard Way - Exercise 11. Asking questions.

# Prints a string.
print("Form #1:")
# Prints a line ending with a blank space, not a newline.
print("How old are you?", end=' ')
# Takes a string input from the user and assigns it to a variable.
age = input()
# Prints a string ending without a newline.
print("How tall are you?", end=' ')
# Takes a string input and assigns it to a variable.
height = input()
# Prints a string ending without a newline.
print("How much do you weigh?", end=' ')
# Takes a string input and assigns it to a variable.
weight = input()

# Prints a format string using the variables assigned above, beginning with a newline.
print(f"\nSo, you're {age} old, {height} tall and {weight} heavy.")

# Prints a string beginning with two newlines.
print("\n\nForm #2:")
# Takes a string input from the user and assigns it to a variable.
color = input("What is your favourite color? --> ")
# Prints a different kind of format string using the variable above.
print("Your favourite color is {}, mine is green.".format(color))

# Prints a string beginning with two newlines.
print("\n\nForm #3:")
# Takes a string input from the user and prints a string with the input in one line.
print("Your lucky number is " + input("What is your lucky number? --> ") + ", mine is 5.")

# Prints a string beginning with two newlines.
print("\n\nForm #4:")
# Prints a string.
print("I'm an adding machine. Please provide two numbers and I will add them for you!")
# Takes an integer input from the user and assigns it to a variable.
num1 = int(input("What is the first number you want to add? --> "))
# Takes an integer input from the user and assigns it to another variable.
num2 = int(input(str(num1) + " is a great number! What number would you like to add to it? --> "))
# Adds the two numbers and prints the calculation in a format string.
print("\nThis is a tough one, let me think...  {} and {} makes {}!".format(num1, num2, num1 + num2))
