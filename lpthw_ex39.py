# Learning Python3 the Hard Way. Excercise 39. Dictionaries, Oh Lovely Dictionaries.

# Create a mapping of state to abbreviation.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities.
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities.
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has : ", cities['OR'])

# Print some states.
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using the state then cities dict.
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# Print every state abbreviation.
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")

# Print every city in a state.
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

# Now do both at the same time.
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}.")

print('-' * 10)
# Safely get an abbreviation by state that might not be there.
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get a city with a default value.
city = cities.get("TX", 'Does Not Exist')
print(f"The city for the state of 'TX' is: {city}.")

print('#' * 20)

countries = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'England': 'London',
    'Poland': 'Warsaw'
}
print("Some european countries and their capitals.\n")

for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")


print("\nNow let's try this dictionary out...")
print(f"The capital of England is... {countries['England']}")

print(f"Let's see... What country is Madrid the capital of?")
for country, capital in countries.items():
    if capital == 'Madrid':
        print(f"Aah, it's {country}.")

print("Let's remove Spain from the dictionary...")
del countries['Spain']

print("Oh you want a copy?")
copy = countries.copy()
print("Here, you're welcome, try it out!")
print("")
for country, capital in copy.items():
    print(f"Capital of {country} is {capital}.")

print("\nNice! I know, Spain is missing =(")
print("Careful with that glass of red wine!")
copy.clear()

for country, capital in copy.items():
    print(f"Capital of {country} is {capital}.")

print("It's destroyed. I can't read anything!")