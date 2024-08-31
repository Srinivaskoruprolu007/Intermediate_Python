
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 23, "Senior", 7000]
"""
A class is a blueprint used to define more complex data types.
It allows for creating objects that bundle data and functionality together.
"""
# Class
class SoftwareEngineer:
    # class attribute
    alias = "Data Driver"
    def __init__(self, name, age, level, salary):
        #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

"""
1. Class attributes (`alias`), which are shared among all instances of the class.
2. Instance attributes (`name`, `age`, `level`, `salary`), which are unique to each instance.
3. The creation of class instances (`se1` and `se2`) and how to access both class and instance attributes.
"""

#instance
se1 = SoftwareEngineer("Srinivas",23, "Junior", 6000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Tharun",  23, "Senior", 7000)


