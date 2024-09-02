a = frozenset([1, 2, 3, 4])

"""
`frozenset` is a built-in Python data type that represents an immutable version of a set. Unlike regular sets,
frozensets cannot be modified after their creation. This immutability makes frozensets hashable and therefore 
usable as keys in dictionaries or elements in other sets.

Key characteristics of frozensets:
- Immutable: Once created, the elements of a frozenset cannot be added, removed, or modified.
- Hashable: Because they are immutable, frozensets can be used as keys in dictionaries or elements in other sets.
- Set Operations: Frozensets support common set operations like union, intersection, difference, and symmetric difference, but do not support methods that modify the set, such as `add()` or `remove()`."""

# Example:
# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])

# Performing set operations
union_set = frozen_set.union({4, 5, 6, 7})  # Union of frozenset and another set
intersection_set = frozen_set.intersection({3, 4, 5})  # Intersection with another set
difference_set = frozen_set.difference({1, 2, 6})  # Difference with another set

# Attempting to modify a frozenset will result in an AttributeError
frozen_set.add(6)  # This will raise an AttributeError since frozensets do not support `add()` method
"""
Use frozensets when you need a set-like structure that should not be altered and need to ensure its elements
remain constant throughout the program.

"""