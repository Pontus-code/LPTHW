# Learning Pyhon 3 the Hard Way - Exercise 8. Printing, Printing.

# Creates a string containing four pairs of curly braces.
formatter = "{} {} {} {}"

# Prints the variable above.
print(formatter)

# Replaces the four curly braces in formatter with integers.
print(formatter.format(1, 2, 3, 4))
# Replaces the four curly braces in formatter with strings.
print(formatter.format("one", "two", "three", "four"))
# Replaces the four curly braces in formatter with booleans.
print(formatter.format(True, False, False, True))
# Replaces the four curly braces in formatter with four instances of the formatter string.
print(formatter.format(formatter, formatter, formatter, formatter))
# Replaces the four curly braces in formatter with four strings.
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))

print("#" * 30)

# This will only print the first four strings.
print(formatter.format("What", "if", "I", "use", "more", "than", "four", "strings?"))

# Providing only three strings will cause an error.
# print(formatter.format("Only", "three", "strings"))

# How about different data types?
print(formatter.format(1, "=", 1, True)) 

# Let's try something else.
formatter2 = "I would like {} and {} for {}."
print(formatter2.format("eggs", "bacon", "breakfast"))
print(formatter2.format("spaghetti", "meatballs", "lunch"))
print(formatter2.format("fish", "potatoes", "dinner"))

 


