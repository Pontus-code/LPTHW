# Learning Python3 the Hard Way. Excercise 38. Doing Things to Lists.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print("#".join(stuff[3:5])) # suoer stellar!

print("\nLet's make a do to list")
to_do_list = []
print("I need to go grocery shopping!")
to_do_list.append("Groceries")
print("And I have to do laundry!")
to_do_list.append("Laundry")
print("Yeah, and brush my teeth!")
to_do_list.append("Brush teeth")
print("And shower!")
to_do_list.append("Shower")
print("Got to fix the bike!")
to_do_list.append("Fix bike")
print("I should paint the fence.")
to_do_list.append("Paint fence")
print("And tidy the garden.")
to_do_list.append("Tidy garden")
print("I should call my parents too.")
to_do_list.append("Call parents")
print("I should also take a nap.")
to_do_list.append("Take nap")
print("It's time to finish this to do list!")
to_do_list.append("Finish list")

print("\nHmm, let's see how many items are on my list.")
print(f"I count... {len(to_do_list)} things on the list.")
print("This is my to do list:")
for task in to_do_list:
    print("\t* " + task)
print(f"But wait! I can already cross off '{to_do_list.pop()}'!")
print(f"Only {len(to_do_list)} items left on the list. Good job!")
print("I deserve a nap now.")
print(f"Hmm where on the list is that? Its... right there. # {(to_do_list.index('Take nap') + 1)}.")
print(f"Let's cross that out too.")
to_do_list.pop(8)
print("Let's have another look at the list.")
for task in to_do_list:
    print("\t* " + task)
print(f"Only {len(to_do_list)} items left on the list.")
print("I'm being VERY productive. Now let's nap.")
print("ZZZzzzzz....")
