# Learning Python 3 the Hard Way - Exercise 9. Printing, Printing, Printing.

# Here's some new strange stuff, remember type it exactly.

# Assigns a string to a variable.
days = "Mon Tue Wed Thu Fri Sat Sun"
# Assings a string with new line white spaces to a variable.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints a string and a variable.
print("Here are the days:", days)
# Prints a string and a variable.
print("Here are the months:", months)

# Prints a multi-line string.
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# Prints 50 octothorpes.
print("#" * 50)

# Triple quotes can also be used to make multi-line comments.
""" No one will
	ever take this
		multi-line string
			seriously anyway... """
# Let's make a list of the week days from the string variable. 
days_list = days.split(" ")
# Now let's print them row after row like the months above.
for i in days_list:
    print(i, end="\n")
# How about printing the months in one row like the days were in the beginning.
for i in months.split("\n"):
    print(i, end=' ')

	
