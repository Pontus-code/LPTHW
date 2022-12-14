# Learning Python3 the Hard Way. Excercise 42. Is-A, Has-A, Objects and Classes.

## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    
    def __init__(self, name):
        ## Animal has-a name
        self.name = name

    def what(self):
        print(f"I am an animal. My name is {self.name}")


## Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name


## Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name.
        self.name = name

    def jump(self):
        print("The cat jumped.")

    def what(self):
        print(f"I am a cat. My name is {self.name}")

## Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind,
        self.pet = None

    def hello(self):
        print(f"Hello my name is {self.name}")

## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary.
        self.salary = salary



## Fish is-a object.
class Fish(object):

    def __init__(self, name):
        self.name = name

## Salmon is-a Fish.
class Salmon(Fish):
    
    def __init__(self):
        self.species = "Salmon"

## Halibut is-a Fish.
class Halibut(Fish):
    
    def __init__(self, name):
        self.species = "Halibut"
        self.name = name

## rover is-a Dog that has-a name Rover.
rover = Dog("Rover")

## satan is-a Cat that has-a name Satan.
satan = Cat("Satan")

## mary is-a Person that has-a name Mary.
mary = Person("Mary")

## mary has-a pet that is-a Cat that has-a name Satan.
mary.pet = satan

## frank is-a Employee that has-a name Frank and has-a salary 120000.
frank = Employee("Frank", 120000)

## frank has-a pet that is-a Dog that has-a name Rover.
frank.pet = rover

## Flipper is a Fish.
flipper = Fish("Flipper")

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut("Harry")

mammoth = Animal("Wooly")

things = ['pen', 'watch', 'mirror', 'chair', 'plant', 'glasses']

frank.things = things

print(f"{frank.name} has the following things {' '.join(frank.things)}.")
print(f"{frank.name} gives his {frank.things[4]} to {mary.name}")
mary.things = frank.things[4]
frank.things.pop(4)
print(f"Now {mary.name} has {mary.things} and {frank.name} has {' '.join(frank.things)}.")
print(f"{frank.name} salary is $ {frank.salary} and his pets name is {frank.pet.name}.")
print(f"{mary.name} has a pet named {mary.pet.name}.")
print(f"{mary.pet.name} can introduce himself: ", end = '')
mary.pet.what()
print(f"Come on {mary.pet.name}, jump!")
mary.pet.jump()
print(f"{frank.name} and {mary.name} exchange pets.")
mary.pet = rover
frank.pet = satan
print(f"Now {frank.name} has a pet named {frank.pet.name}")
print(f"And {mary.name} has a pet named {mary.pet.name}")
print('-' * 20)
mammoth.what()
print(f"{harry.name} is a {harry.species}.")
rover.what()
satan.what()
mammoth.what()
mary.hello()
frank.hello()