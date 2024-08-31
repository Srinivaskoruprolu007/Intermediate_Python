# Dictionary: Key-value pairs, Unordered, Mutable
"""
You can create a dictionary using curly braces {} or the dict() constructor.
"""
myDict = {"name":"Srinivas", "age":23, "city":"Vizag"}
print(myDict)

myDict2 = dict(name="Srinivas", age=23, city="Vizag")
print(myDict2)

"""
You can access values in a dictionary using their associated keys
"""
value = myDict["name"]
print(value)
age = myDict['age']
print(age)
"""
Note: If you try to access a key that does not exist in the dictionary, it will raise a KeyError
"""

"""
You can add key-values pair by simple syntax
"""
myDict["married"] = True
print(myDict)
"""
If the key is exited then it will overwritten with new value
"""
myDict["married"] = False
print(myDict)

"""
You can delete a key-value pair by del keyword and also delete last pair by pop() method
and also you can delete item using popitem()
"""
del myDict["married"]
print(myDict)

myDict.pop("city")
print(myDict)

myDict.popitem()
print(myDict)

"""
To check whether the given Key is present or not in a dict you can use membership operator `is`
"""
if "age" in myDict:
    print(myDict['age'])
else:
    print("key is not found")

try:
    print(myDict['age'])
except:
    print("Error")


"""
There are several ways to iterate through a dictionary:

1. Use a `for` loop directly to access the keys in the dictionary.
2. Use `for key in dict.keys()` to iterate over the keys explicitly.
3. Use `for value in dict.values()` to iterate over the values explicitly.
4. use `for key, value in dict.items()` to iterate over the keys and values explicitly.
"""
myDict = {"name":"Srinivas", "age":23, "city":"Vizag"}
print(myDict)
for key in myDict:
    print(key)
for key in myDict:
    print(myDict[key])

for key in myDict.keys():
    print(myDict[key])

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, '--> ',value)


