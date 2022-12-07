# Learning Python3 the Hard Way. Excercise 32. Loops and Lists.

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list.
for number in the_count:
    print(f"This is count {number}")

# Same as above.
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Also we can go through mixed lists too.
# Notice we have to use {} since we don't know what's in it.
for i in change:
    print(f"I got {i}")

# We can also build lists. first start with an empty one.
elements = []

# Then use the range function to do 0 to 5 counts.
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # Append is a function that lists undersand.
    elements.append(i)

# Now we can print them out too.
for i in elements:
    print(f"Element was: {i}")

# Adding a range of numbers to a list wihtout using a foor loop.
elements = list(range(0, 6))
print(elements)

# Removing 2 from the list.
elements.pop(2)
print(elements)

# Reverses the order of the elements in the list
elements.reverse()
print(elements)
# Changes the last element to 9.
elements[-1] = 9
print(elements)
