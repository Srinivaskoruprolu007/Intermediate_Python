# dunder_methods_example.py
"""
Dunder or magic methods in Python are special methods that start and end with double underscores (__).
They are used to define and customize the behavior of objects, enabling operations like initialization,
representation, comparison, arithmetic, and more.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __gt__(self, other):
        return self.age > other.age

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

# Creating instances and testing methods
p1 = Person("Alice", 30)
p2 = Person("Alice", 13)
p3 = Person("Bob", 25)

print("Testing __str__ and __repr__:")
print(str(p1))  # Calls __str__
print(repr(p1))  # Calls __repr__

print("\nTesting __eq__:")
print(p1 == p2)  # True, calls __eq__
print(p1 == p3)  # False, calls __eq__

print(p1 > p2)

print("\nTesting __add__ with Vector:")
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__
print(v3)  # Vector(6, 8)

print("\nTesting __len__ and __getitem__ with CustomList:")
my_list = CustomList([1, 2, 3, 4])
print(len(my_list))  # Calls __len__
print(my_list[2])  # Calls __getitem__

print("\nTesting __call__ with Greeter:")
greet = Greeter("Alice")
print(greet())  # Calls __call__

