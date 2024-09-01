"""
Encapsulation is a property in OOPs that is used to hide functionality and properties from the user
Which can be achieved by _(protected) and __(private) in python

_(single underscore is used to declare a property to be protected. you can access from outside you shouldn't use)
__(double underscore is used to declare a property to be private. You can't access from outside, but you can access by using setters and getters
"""
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 5000
        self._codeFixes = 9

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, newSalary):
        if self.__salary < 1000 or self.__increment():
            self.__salary = newSalary * 2
    def __increment(self, ):
        return self._codeFixes >= 10
    # @salary.deleter
    # def salary(self):
    #     del self.__salary


"""
Polymorphism is a core concept of OOPs in python which allows different functionalities to the same function with same name
depends on the instance of a class
1. static polymorphism (compile time)
2. dynamic polymorphism (run time)  
"""

se = SoftwareEngineer("Tharun", 22)
se.salary = 6000
print(se.salary)
# del se.salary
print(se.salary)



