# collections: Counter, namedtuple, OrderedDict, defaultDict, deque
from collections import deque, namedtuple, defaultdict, Counter, OrderedDict

"""
Counter():
Counter is used to tally the occurrences of elements in a string or list.
It returns a Counter object, which is a dictionary-like structure where keys represent the elements and values denote their respective counts
"""
a = 'aaaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)

"""
You can retrieve the top n most frequent elements using the most_common method of a Counter object. 
This method takes an integer argument n and returns a list of the n most common elements along with their counts.
"""
print(my_counter.most_common(2))

"""
ou can access the most frequent element by selecting the element at index 0 from the list returned by the most_common method
"""
print(my_counter.most_common(1)[0][0])


# namedtuple
"""
`namedtuple` is a factory function from the `collections` module that creates 
simple, immutable classes for storing data. It is similar to structs in other 
programming languages and provides a way to define lightweight objects with 
named fields.
"""
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)
"""
The namedtuple takes two argument i.e name of the object and s
"""