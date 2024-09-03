# %, format(), f-strings
"""
In Python, you can format strings using three different methods:
1. The `%` operator (often referred to as the old-style string formatting).
2. The `format()` method, which provides more flexibility and readability.
3. F-strings (formatted string literals), which offer a concise and modern way to embed expressions inside string literals.
"""

var = 'Tom'
my_string = 'the variable is %s' %var
print(my_string)

var = 3.123543
greet = 'bye'
my_string = 'the variable is %.2f and %s' %(var, greet)
print(my_string)


var = 3.123543
greet = 'bye'
my_string = 'the variable is %d and %s' %(var, greet)
print(my_string)


var = 3.123543
greet = 'bye'
my_string = 'the variable is {:.2f} and {}'.format(var, greet)
print(my_string)

var = 3.123543
greet = 'bye'
my_string = f'the variable is {var} and {greet}'
print(my_string)
