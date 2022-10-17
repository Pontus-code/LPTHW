# Learning Python 3 the Hard Way - Exercise 6. Strings and Text.

# Creates a variable and assigns it a value.
types_of_people = 10
# Creates a format string that uses a variable.
x = f"There are {types_of_people} types of people."
# Creates av variable.
binary = "binary"
# Also a variable.
do_not = "don't"
# Creates another format string. This one has to variables.
y = f"Those who know {binary} and those who {do_not}."

# Prints the variable x.
print(x)
# Prints the variable y.
print(y)

# Prints a format string containing a variable.
print(f"I said: {x}")
# Same as above.
print(f"I also said: '{y}'")

# Creates a variable and assigns it a boolean value.
hilarious = False
# Creates a string that accepts a variable.
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints a string that accepts a variable.
print(joke_evaluation.format(hilarious))

# Assigns a string to a variable.
w = "This is the left side of..."
# Same as above.
e = "a string with a right side."

# Prints to variables, in this case it's two strings.
print(w + e)

