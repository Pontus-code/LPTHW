# Learning Python3 the Hard Way - Excercise 22. What Do You Know So Far?

# Words and symbols used so far, and some more...

# : A colon precedes an indented block of code, also to slice strings, access parts of a list or assign key:value pairs i a dictionary.
# Comments:
    # Octothorpe will make the interpreter ignore the text to the right on the same line.
    # """ or ''' The interpreter will ignore everything between double or triple-quotes. Also used fro multi-line strings.
# Strings:
    # " or ' Double or single quotes surrounds a string. Single quotes can be used within double quotes and vice versa.
    # str() Turns specified variable into the data class string.
    # print("a string") Prints a string.
    # print("a string" end = '') Prints a string without an ending newline.
    # print(f"First name: {variable1} and Last name: {variable2}") Prints a format string, allowing variables inside curly braces within the quotes.
    # print("First name: {} and Last name: {}".format(variable1, variable2) Another way of writing a format string by giving the variables at the end. 
    # print("I like the following colors: {} {} {} {}".format(*colors)) Uses elements from a list called colors.
# String methods:
    # encode() Returns encoded version of the string, raw data.
    # decode() Returns decoded version of byte-data, default is unicode ("UTF-8").
    # find() or index() Searches string for a specified value and returns the position.
    # isalpha() True if all characters are in the alphabet.
    # join() Converts elements of a list into a string.
    # split() Splits a string at specified seperator and returns a list.
    # lsplit() and rsplit() trims left and right side of string respectively.
    # strip() Returns a string with specified characters trimmed from the beginning and end of string. 
    # lower() Converts a string into lower case.
# White space characters:
    # \n Newline.
    # \t Tab.
    # \\n Escapes \ and prints '\n'.
#  Integers:
    # Whole numbers.
    # int(5) turns a string "5" into an integer.
    # int("A", 16) or int("1010", 2) Convert base 16 or base 2 into decimal. 
    # random.randrange(1, 10) Picks a random number between 1 and 9.
# Floats:
    # float("4.00") Converts a string into a floating point number.
    # round() Rounds a floating point number to the closest whole number.
# Lists:
    # Array of elemnts.
    # append() Adds an element to the end of the string.
    # clear() Removes all elements from the list.
    # index() Returns the index of the first element with the specified value.
    # insert() Inserts an element at specified position.
    # pop() Removes element at specified position.
    # remove() removes first element with specified value.
    # reverse() reverses a list.
    # random.choice() Picks a random element in a list.
# Arithmetic operators:
    # * Will multiply operands or repeat a string.
    # ** Exponent, to the power of...
    # + Will add operands or concatenate two strings.
    # - Substract an operand from another.
    # / Divides an operand with another.
    # // Floored division, results are rounded.
    # % Modulus divides two operands and returns the remainder.
# Comparison operators:
    # > Greater than.
    # >=  Equal or greater than.
    # ==  Equals to.
    # != or <>  Not equal to.
    # < Less than.
    # <= Equal or less than.
# Logical Operators: 
    # and True if both operands are True.
    # or  True if either operand is True.
    # not True if no operand is True
# Assignment operators:
    # = Assigns the operand on the right to the one on the left.
    # += Adds the the right operator to the left operator and assigns it to the left operand.
    # -= Removes the right operand from the left and assigns it to the left operand.
    # *= Multiplies the right with the left and assigns it to left.
    # %= modulus of right and left and assigns left.
    # /= Divides right with left and assings left.
    # **= Takes left to the power of right and assigns left.
    # //= Performs floor division and assigns left.
# Bitwise operators:
    # & or AND Copies a bit to the result if it exists in both operands.
    # | or OR Copies a bit if it exists in either operand.
    # ^ or XOR Copies a bit if it only exists in either operand.
    # ~ or Ones Complement Flips the bits of one operand.
    # << or Left Shift Left operands value is moved left by the number of bits specified by the right operand.
    # >> or Right Shift Left operands value is moved right by the number specified by the right operand.
# File manipulation:
    # open(filename, 'rt') Opens a file as readable('r') text('t') (default)
        # 'w' Opens the file for writing, truncating the file first.
        # 'w+' Opens the file for reading and writing, existing file is truncated.
        # 'x' Opens for eXclusive creation, returns an error if the file already exists.
        # 'a' Opens the file for writing, appending at the end of the file.
        # 'a+' Opens for reading and appending.
        # 'rb' Opens file in binary.
        # 'wb' Writes binary to file.
    # File methods:
        # read() Returns file contents.
        # write() Writes to file.
        # readlines() Returns a list of lines from file.
        # readline() Returns one line.
        # len(readlines()) Returns number of lines.
        # writeline() Writes a list of strings to a file.
        # seek() Changes file position, 0 = beginning
        # tell() Returns the current file position.
        # close() Closes the file.
        # truncate() Rezies the file to the specified size.
# Functions:
    # def function(arg1, arg2): Defines a function that takes two arguments.
    # from sys import argv Imports argv module from sys package.
    # script, first, second = argv Unpacks arguments.
    # return "result" Returns result of function.
# Input:
    # a = input("What's your input?") Asks user fror input and assigns it to a variable.
    # str(input("Give me a string: ")) Only takes a string.
    # int(input("Give me a number: ")) Only takes an integer.
    # input("Press RETURN or continue or CTRL-C to exit") Input can be used to pause script until user input. Input is not assigned to a variable.
# Misc. modules:
    # from os.path import exists Imports the module exists from the package os.path
    # from datetime import datetime Imports the function datetime from the module datetime.




