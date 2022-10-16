# Learning Python 3 the Hard Way - Exercise 4. Variables and Names.

# The number of cars.
cars = 100
# The number of passengers that each car can take.
space_in_a_car = 4
# The number of available drivers.
drivers = 30
# The number of passengers travelling.
passengers = 90
# The number of cars that is not driven.
cars_not_driven = cars - drivers
# The number of cars driven.
cars_driven = drivers
# How many passengers can the driven cars take.
carpool_capacity = cars_driven * space_in_a_car
# How many passengers in each driven car on average.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")



