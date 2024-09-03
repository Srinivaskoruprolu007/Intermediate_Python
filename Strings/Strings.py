# Strings: Ordered, immutable, text representation
my_string = "Hello people"
print(my_string)
"""
Strings in Python can be defined using either single quotes (' ') or double quotes (" "). 
Additionally, triple quotes (''' ''' or """ """) are used for creating multiline strings or for writing docstrings in your code. 
Triple quotes allow you to span a string across multiple lines and are particularly useful for long text or documentation.
"""
multiLineString = '''Hello \
world
'''
print(multiLineString)

myString = "wonderful"
"""
You can access a specific character in a string by using indexing. Python strings are indexed starting from 0 
up to the length of the string minus 1. Additionally, Python supports negative indexing, which allows you to 
access characters from the end of the string, with -1 being the last character.
"""
print(myString[0]) # first character
print(myString[-1]) # last character

"""
Strings in Python are immutable, which means you cannot modify a string by assigning a value to a specific index. 
Any attempt to change a character at a particular position will result in a TypeError. 
Instead, if you need to modify a string, you'll need to create a new string with the desired changes.
"""

# myString[1] = 'y' # raises TypeError

sliced_string = my_string[:1:]
print(sliced_string)
sliced_string = my_string[::-1]
print(sliced_string)
sliced_string = my_string[1:5:2]
print(sliced_string)
"""
Slicing in strings works the same way as in lists. You can extract a portion of a string by specifying a range 
of indices in the format `string[start:stop]`. The `start` index is inclusive, while the `stop` index is 
exclusive. You can also specify a `step` to include every nth character within the specified range. 
If no start or stop index is provided, slicing defaults to the beginning or end of the string, respectively.
"""

greeting = "Hello"
name = "Tharun"
sentence = greeting + " "+name
print(sentence)

"""
You can concatenate two strings using the `+` operator, which joins them together into a single string. 
This operation creates a new string that combines the contents of the original strings.
"""

for i in greeting:
    print(i)

for i in range(len(greeting)):
    print(greeting[i])

"""
You can iterate over a string using a `for` loop in two ways: 
1. By directly looping through each character in the string using `for char in string`.
2. By using a `for` loop with `range`, iterating from 0 to the length of the string minus 1. 
   This allows you to access each character by its index.
"""

if 'e' in greeting:
    print("yes")
else:
    print('no')

"""
You can check if a given character is present in a string using the membership operator `in`. 
This operator returns `True` if the character is found in the string and `False` if it is not.
"""


