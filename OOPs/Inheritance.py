
#Inherits, extends, overrides
"""
Inheritance is one of the OOPs properties that are used to inherit, extends, and overrides the properties,
function from the superclass (Parent-class) to its subclasses (child-classes)
"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working...")


"""
In python you can simply inherit a class by using the class name of the parent class as shown below `class SoftwareEngineer(Employee)`
i.e SoftwareEmployee class is inherited by Employee class
"""
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, grade):
        # super is a keyword used to use the parent's constructor from the child constructor
        super().__init__(name, age)
        self.salary = salary
        self.grade = grade

    def work(self):
        print(f"{self.name} is coding...")
class Designer(Employee):
    def __init__(self, name, age, salary, grade):
        super().__init__(name, age)
        self.salary = salary
        self.grade = grade

    def work(self):
        print(f"{self.name} is designing...")

se = SoftwareEngineer('Srinivas', 23, 2000, 'A')
se.work()
de = Designer("Tharun", 22, 5000, 'A')
de.work()