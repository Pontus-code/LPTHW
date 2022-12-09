# Learning python3 the Hard Way. Excercise 33. While loops.

def loop(number):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)
    
    numbers = []
    i = 0
    for i in range(number):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)
loop(10)