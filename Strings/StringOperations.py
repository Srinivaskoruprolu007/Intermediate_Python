from Tools.scripts.objgraph import store
from timeit import default_timer as timer
myString = '   Hello   '
myString = myString.strip()
print(myString)
"""
If your string contains any leading or trailing white spaces, you can remove them using the `strip()` method. 
This method returns a new string with all white spaces removed from both the beginning and the end of the original string. 
It does not affect any white spaces that are within the string.
"""


print(myString.upper())
print(myString.lower())
"""
You can also convert a string to uppercase using the `upper()` method or to lowercase using the `lower()` method. 
Additionally, you can check if the string starts with a certain character or substring using the `startswith()` method.
"""
print(myString.startswith('h'))
print(myString.endswith('llo'))

"""
You can also find the first index where a character or substring appears in a string using the `find()` method. 
This method returns the index of the first occurrence of the specified character or substring, or `-1` if it is not found in the string.
"""
print(myString.find('He'))

"""
You can replace a substring with another substring in a string using the `replace()` method. 
This method typically takes two arguments: the substring you want to replace and the substring you want to replace it with. 
Optionally, you can provide a third argument to specify the maximum number of replacements to perform.
"""

my_string = 'hello world'
my_string = my_string.replace("world", 'universe')
print(my_string)


"""
The `split()` method is used to convert a string into a list of substrings, based on a specified delimiter. 
By default, the delimiter is a space (" "), meaning that the string will be split wherever a space occurs. 
You can also specify a different delimiter to split the string at other characters.
"""
my_string = 'how are you doing'
my_list = my_string.split(" ")
print(my_list)

"""
The `join()` method is used to convert a list of strings into a single string, with a specified delimiter placed 
between each element of the list. The delimiter is defined by the string on which `join()` is called.
"""

new_string = ', '.join(my_list)
print(new_string)


my_list = ['a'] * 100000

# if you want to join them together
# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

# good

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

"""
When comparing the two approaches for joining a list of strings into a single string, 
you'll notice a significant difference in performance. The brute-force approach using 
a `for` loop typically takes more time than the `join()` method. The `join()` method is 
more efficient and optimized for this task, making it the preferred choice for concatenating strings from a list.
"""


