# Learning Python3 the Hard Way. Excercise 30. Else and If.

people = 50
cars = 40
trucks = 45

# If if-line is True then run indented block of code.
if cars > people:
    print("We should take the cars.")
# If the if-line is False evaluate the elif-line.
elif cars < (people + cars - 100):
    print("We should not take the cars.")
# If all if and elif lines above are False then run the indented block of code.
else:
    print("We can't decide.")


if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")