class Animal:
    def __init__(self, name, legs, wings):
        self.name = name
        self.legs = legs
        self.wings = wings

    # Instance method to simulate walking
    def walk(self):
        print(self.name, "is walking with", self.legs, "legs.")

    # Instance method to simulate hunting
    def hunt(self, found):
        if found:
            print(self.name, "hunting was successful.")
        else:
            print(self.name, "hunting failed.")

    # Instance method to simulate flying, with a return statement
    def fly(self):
        if self.wings:
            return f"{self.name} is flying."
        else:
            return f"{self.name} cannot fly because it has no wings."

    # Instance method to simulate eating with a parameter and a return value
    def eat(self, food):
        return f"{self.name} is eating {food}."

# Create an instance of Animal
lion = Animal("Simba", 4, False)
lion.walk()  # Call walk method
lion.hunt(True)  # Call hunt method
print(lion.fly())  # Call fly method and print return value
print(lion.eat("meat"))  # Call eat method and print return value

# Conclusion
"""
This code defines an `Animal` class that encapsulates the attributes and behaviors of an animal.
The class includes:
1. An initializer method (`__init__`) to set the name, number of legs, and wings.
2. Instance methods `walk`, `hunt`, `fly`, and `eat`, each demonstrating different actions animals can perform.
3. The `fly` method returns a message based on whether the animal can fly, while the `eat` method takes a food parameter and returns a message indicating what the animal is eating.

Overall, this example illustrates how to create a class with multiple methods to model the behavior of animals, showcasing the principles of encapsulation and method definitions in object-oriented programming.
"""
