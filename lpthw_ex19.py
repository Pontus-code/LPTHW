# Learning Python3 the Hard Way - Exercise 19. Functions and Variables.

# Defines a functions that takes two arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints a format string including one of the arguments.
    print(f"You have {cheese_count} cheeses!")
    # Prints another format string including the other argument.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enought for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Runs the function with two integers as input.
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Runs the functions with two variables as input.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")

# Runs the function with two expressions.
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Runs the function with two expressions including both integers and variables.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Another function.
def story(char1, char2):
    print(f"Once upon a time there was a hunter called {char1}.")
    print(f"Meanwhile there was a rabbit in the forest called {char2}.")
    print(f"One day the hunter {char1} saw the rabbit and killed {char2}")
    print("The end...\n")

# Run the function with variables.
hunter = "Robin hood"
rabbit = "Brother Tuck"
story(hunter, rabbit)

# Ask the user to provide the input.
story(input("What's the name of the hunter? "), input("Whats the name of the rabbit? "))

# Run the function with inputs from a list.
list_of_names = ['Drizzt', 'Brie']
hunter, rabbit = list_of_names
story(hunter, rabbit)

# Run the function with random items from a list.
namelist = ['Bilbo', 'Gandalf', 'Aragon', 'Sam', 'Saruman', 'Sauron', 'Boromir', 'Gollum']
import random
name1 = random.choice(namelist)
name2 = random.choice(namelist)
story(name1, name2)

# Ask the user to input names and run the function with random names from that list.
print("Please provide four names.\n")
list = []
for i in range(4):
    name = input(f"Please provide name #{i+1}: ")
    list += [name] 

print("\nI will use two random names from your list in my story...\n")
name1 = random.choice(list)
name2 = random.choice(list)
story(name1, name2)


    
