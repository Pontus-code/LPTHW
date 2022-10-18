# Learning Pythong 3 the Hard Way - Exercise 10. What was that?

# Assigns a string to a variable with an escape sequence tab.
tabby_cat = "\tI'm tabbed in."
# Assigns a string to a variable with an escape sequence new line.
persian_cat = "I'm split\non a line."
# Assigns a strings to a variable with escaped backslashes.
backslash_cat = "I'm \\ a \\ cat."

# Assigns a multi-line string to a variable including escape sequences for tab.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Prints a variable.
print(tabby_cat)
# Prints a variable.
print(persian_cat)
# Prints a variable.
print(backslash_cat)
# Prints a variable.
print(fat_cat)

# Prints 50 octothorpes.      		
print('#' * 50 + '\n' * 5)

# Prints a multi-line string with escaped double-quotes within.
print(
'''
 WARNING!
	DON'T
		FALL
			DOWN
				THE
					"STAIRS"
						!!!
''')

# Prints 10 rows of 10 octothorpes preceded by incremental tabs forming some stairs.
for i in range(10):
    print('\t' * i + "#" * 10, end='\n')

# Prints a format string with escape sequences.
print("Mind the gap!{}OUCH!".format('\n' * 5 +'\t' * 2))

# String with escaped backslashes.
print("I\\will\\always\\escape\\the\\backslashes!")

# String with non-escaped backslashes.
print("I\will\never\return\after\I\escape\this\time")

 
    
