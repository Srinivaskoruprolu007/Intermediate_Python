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

"""
When you want to copy a dictionary, avoid assigning it directly to another variable, 
as any changes made to the copied dictionary will also affect the original dictionary.
"""
# Avoid this
mydict_cpy = myDict
mydict_cpy["key"] = "value"
print(myDict)
print(mydict_cpy)

# Better approaches
mydict_cpy = myDict.copy()
mydict_cpy['new-key'] = 'new-value'
print(myDict)
print(mydict_cpy)

mydict_cpy = dict(myDict)
mydict_cpy['new-key'] = 'values'
print(myDict)
print(mydict_cpy)


"""
Rules for working with dictionaries in Python:

1. Keys must be unique and immutable: You can use types like strings, numbers, or tuples as dictionary keys, 
but you cannot use lists or other dictionaries.

2. Dictionaries are mutable: You can change the values, 
add new key-value pairs, or remove existing ones after the dictionary has been created.

3. Dictionaries do not maintain order: In Python versions prior to 3.7, dictionaries do not maintain order. 
Starting with Python 3.7, dictionaries preserve the insertion order.

4. Avoid direct assignment for copying: When copying a dictionary, use methods like `copy()` or `deepcopy()` to avoid unintentional changes to the original dictionary.

5. Keys must be hashable: This means that the keys must have a hash value that remains the same during their lifetime. 
Common hashable types include integers, strings, and tuples.

6. Dictionary keys can be of different types: While it's possible to have keys of different types within the same dictionary, 
it's generally good practice to use consistent key types.

7. Use `in` to check for the existence of a key: Instead of manually searching for a key, use the `in` keyword to determine if a key exists in the dictionary.
"""
