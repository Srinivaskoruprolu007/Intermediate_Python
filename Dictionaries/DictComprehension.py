"""
Dictionary comprehension is a concise and efficient way to create dictionaries in Python.
It consists of a single expression that defines the key-value pairs of the dictionary.
The basic syntax is: {key_expression: value_expression for item in iterable if condition}
- key_expression: Expression to determine the dictionary key.
- value_expression: Expression to determine the dictionary value.
- iterable: An iterable object (like a list, tuple, or range) to loop through.
- condition (optional): A conditional statement to filter items based on a condition.
"""
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares) # Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

words = ['apple', 'banana', 'cherry']
lengths = {word : len(word) for word in words}
print(lengths) # Result: {'apple': 5, 'banana': 6, 'cherry': 6}

grades = {"John":85, 'Jane':92, "Dave":30, 'Sara':89}
passed_students = {name:grade for name, grade in grades.items() if grade >= 35}
print(passed_students) # Result: {'John': 85, 'Jane': 92, 'Sara': 89}

matrix = {
    'row1':[1, 2, 3],
    'row2':[4, 5, 6],
    'row3':[7, 8, 9]
}
squared_even_matrix = {
    key : {num : num ** 2 for num in value if num % 2 == 0}
    for key, value in matrix.items()
}
print(squared_even_matrix) # Result: {'row1': {2: 4}, 'row2': {4: 16, 6: 36}, 'row3': {8: 64}}

data = {
    'A':[1, 2, 3],
    'B':[4, 5],
    'C':[6, 7, 8, 9]
}
flattened = {f'{k}{i+1}':v for k, v in data.items() for i, v in enumerate(v)}
print(flattened)
