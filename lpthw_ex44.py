# Learning Python3 the Hard Way. Excercise 44. Inheritance versus Composition.

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
    
    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered")

print("\n" + "#" * 10 + "INHERITANCE" + "#" * 10 + "\n")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()



class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")
       
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

print("\n" + "#" * 10 + "COMPOSITION" + "#" * 10 + "\n")

son = Child()

son.implicit()
son.override()
son.altered()