# Sets : unordered, mutable, no duplicates
"""
You can create a set by using curly braces with values inside.
However, be aware that if you use empty curly braces, it will create a dictionary, not a set.
To create an empty set, use the `set()` constructor instead.
"""
myset = {1, 2, 3, 4, 5, 6}
my_set = set("Hello")
print(myset)
print(my_set)
"""
The `set()` constructor can take iterables like lists, tuples, and strings as parameters to create a set.
"""

myset.add(8)
myset.add(9)
myset.add(10)
myset.add(7)
"""
You can add new elements to a set using the add() method. 
This method allows you to insert a single item into the set. 
Since sets only contain unique elements, if the item you're adding already exists in the set, it won't be added again. 
The add() method is particularly useful for gradually building up a set by adding elements one at a time.
"""

print(myset.remove(4))
try:
    print(myset.remove(11))
except:
    print("element is not exists")
"""
The remove() method in Python is used to delete a specific element from a set. 
However, if the element you attempt to remove is not present in the set, the remove() method will raise a KeyError. 
This can be problematic if you're unsure whether the element exists in the set.
"""
print(myset.discard(15))
print(myset.discard(9))
print(myset)
"""
As an alternative, you can use the discard() method. 
Like remove(), the discard() method removes a specific element from the set.
However, if the element is not found, discard() does not raise an error; instead, it simply does nothing and returns None. 
This makes discard() a safer option when you're not certain whether the element is in the set.
"""
print(myset.pop()) # remove arbitrary value
"""
The pop() method in Python removes and returns an arbitrary element from a set. 
Since sets are unordered, you won't know which element will be removed. 
If the set is empty, calling pop() will raise a KeyError.
"""

"""
You can check if an element is present in a set by using the `in` operator. 
This operator returns `True` if the element exists in the set and `False` if it does not.
"""
if 1 in myset:
    print("yes")
else:
    print("no")

"""
You can iterate over a set using a for loop. 
This allows you to access each element in the set one by one. 
Since sets are unordered, the elements will be iterated in an arbitrary order.
"""
for i in myset:
    print(i)
