"""
Slicing is a python feature is same as the slicing in list
"""
nums_tuple = 1, 2, 3, 4, 5, 6
print(nums_tuple[1:4])
print(nums_tuple[::2])
print(nums_tuple[::-1]) # reversing

"""
Unpacking is a technique in Python that 
allows you to assign each element in a tuple to a separate variable.
"""
info = "Tharun", 19, "Vizag"
name, age, city = info
print(info)
print(name)
print(age)
print(city)

"""
It raises a ValueError if the number of elements in the tuple does not match the number of variables you want to unpack
"""

nums = (1, 2, 3, 4, 5, 6, 7)
"""
Unpacking the tuple 'nums' into three variables:
- i1 will be assigned the first element of the tuple (1).
- i2 will be assigned a list containing all the elements between the first and last elements ([2, 3, 4, 5, 6]).
- i3 will be assigned the last element of the tuple (7).
"""
i1, *i2, i3 = nums
print(i1)
print(i2)
print(i3)
print(type(i2))

