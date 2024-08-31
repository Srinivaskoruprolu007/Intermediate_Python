"""
List comprehension is a Python feature that allows you to create a list more efficiently, elegantly, and in a single line.
"""
a = [1, 2, 3, 4, 5, 6]
squares_a = [i*i for i in a]
print(a)
print(squares_a)

"""
You can also include conditions inside list comprehensions to perform common checks, such as filtering even or odd numbers, or values less than or greater than a certain threshold.
"""
even_squares = [i*i for i in a if i%2 == 0]
print(even_squares)
