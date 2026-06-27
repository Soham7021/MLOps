# Types of Inheritance in Python

# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Single Inheritance
class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Multiple Inheritance
class Cat(Animal):
    def speak(self):
        return "Cat meows"

class Lion(Dog, Cat):
    def speak(self):
        return "Lion roars"

# Multilevel Inheritance
class Puppy(Dog):
    def speak(self):
        return "Puppy yips"

# Hierarchical Inheritance
class Bird(Animal):
    def speak(self):
        return "Bird chirps"

class Parrot(Bird):
    def speak(self):
        return "Parrot talks"

# Demonstrating the inheritance types
def demonstrate_inheritance():
    animal = Animal()
    dog = Dog()
    cat = Cat()
    lion = Lion()
    puppy = Puppy()
    bird = Bird()
    parrot = Parrot()

    print(animal.speak())  # Animal speaks
    print(dog.speak())     # Dog barks
    print(cat.speak())     # Cat meows
    print(lion.speak())    # Lion roars
    print(puppy.speak())   # Puppy yips
    print(bird.speak())    # Bird chirps
    print(parrot.speak())  # Parrot talks

if __name__ == "__main__":
    demonstrate_inheritance()