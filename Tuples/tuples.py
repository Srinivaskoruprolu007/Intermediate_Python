"""
Tuple: Ordered, immutable, allows duplicate elements
"""

"""
Tuple can be created by using round braces which are actually optional
but if you put only one element in round braces that is not considered as tuple.
To define a single-element tuple, include a trailing comma, like (element,)
"""
myTuple = (1, "Messi", True)
print(myTuple)
myTuple = 1, "messi", True
print(myTuple)
single = ("Dhoni")
print(type(single), single)

sing_tuple = ("King",)
print(sing_tuple)

"""
You can access elements in a tuple using indexing, which works the same way as in lists.
Indexing starts from 0 and goes up to the length of the tuple minus 1. 
Negative indexing is also supported, allowing you to access elements from the end of the tuple.
"""
num = myTuple[0]
print(num)
football = myTuple[-2]
print(football)

"""
Since tuples are immutable, you cannot use the assignment operator to change their values.
"""
"""
Iterating over a tuple
"""
for i in myTuple:
    print(i)
for i in range(len(myTuple)):
    print(myTuple[i])

my_tuple = ('a', 'b', 'c', 'd', 'e', 'e')
"""
To check whether a given element is in a tuple, 
use the membership operator in. 
You can also count the occurrences of an element using the count() method and 
find the first index of an element using the index() method.
"""
if 'a' in my_tuple:
    print("yes")
else:
    print('no')

print(my_tuple.count('e')) # 2
print(my_tuple.index('a')) # 0

# tuple to list and vice-versa
list_tuple = list(my_tuple)
print(list_tuple)
tuple_list = tuple([1, 2, 4, 5, 6])
print(tuple_list)
