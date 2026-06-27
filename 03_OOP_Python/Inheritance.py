
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball")

# Example usage
if __name__ == "__main__":
    # Create a dog instance
    my_dog = Dog("Buddy", "Golden Retriever")
    
    # Access attributes
    print(f"Name: {my_dog.name}")
    print(f"Species: {my_dog.species}")
    print(f"Breed: {my_dog.breed}")
    
    # Call methods
    my_dog.make_sound()
    my_dog.fetch()

    # Create another dog instance using the super keyword
    another_dog = Dog("Max", "Bulldog")
    another_dog.make_sound()
    another_dog.fetch()
    