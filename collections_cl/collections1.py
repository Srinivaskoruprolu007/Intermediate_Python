from collections import deque, namedtuple, defaultdict, Counter, OrderedDict

# Counter
"""
Counter is used to tally the occurrences of elements in a string or list.
It returns a Counter object, which is a dictionary-like structure where keys 
represent the elements and values denote their respective counts.
"""
a = 'aaaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)

"""
You can retrieve the top n most frequent elements using the most_common method 
of a Counter object. This method takes an integer argument n and returns a list 
of the n most common elements along with their counts.
"""
print(my_counter.most_common(2))

"""
You can access the most frequent element by selecting the element at index 0 
from the list returned by the most_common method.
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


# defaultdict
"""
`defaultdict` is a subclass of dict that provides a default value for the key that does not exist, 
so it won't raise a KeyError.
"""
d = {}
d['a'] = 1
d['b'] = 2
try:
    print(d['c'])  # keyError
except:
    print("key error due to normal dictionary")

d = defaultdict(int)
"""
Here, we create a defaultdict that automatically initializes missing keys with the integer 0.
"""
print(d['c'])  # No error, prints default value (0)


# deque (double-ended queue)
"""
`deque` (pronounced as 'deck') is a generalization of stacks and queues, which allows you 
to add or remove elements from both ends efficiently (O(1) time complexity for append and pop operations).
"""
dq = deque()

# Add elements to the right
dq.append(1)
dq.append(2)
dq.append(3)
print("After appending elements to the right:", dq)

# Add elements to the left
dq.appendleft(0)
print("After appending an element to the left:", dq)

# Remove elements from the right
dq.pop()
print("After popping an element from the right:", dq)

# Remove elements from the left
dq.popleft()
print("After popping an element from the left:", dq)

# Rotate the deque
dq.rotate(1)  # Rotate right by 1
print("After rotating by 1 position to the right:", dq)

dq.rotate(-1)  # Rotate left by 1
print("After rotating by 1 position to the left:", dq)


# OrderedDict
"""
`OrderedDict` is like a regular dictionary, but it remembers the order in which 
items were inserted. In Python 3.7+, the regular dictionary also maintains insertion order,
so `OrderedDict` is mostly useful for earlier Python versions or for explicit usage.
"""
ordered_dict = OrderedDict()
ordered_dict['banana'] = 3
ordered_dict['apple'] = 4
ordered_dict['orange'] = 2

print("\nOrderedDict maintains the order of insertion:")
for key, value in ordered_dict.items():
    print(key, value)

# Updating an existing key won't affect its position
ordered_dict['apple'] = 10
print("\nAfter updating 'apple', the order remains unchanged:")
for key, value in ordered_dict.items():
    print(key, value)
