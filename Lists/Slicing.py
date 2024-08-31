"""
Slicing is a feature in Python that allows you to access elements in a list from one index (start) to another index (stop, exclusive) with an optional step to skip elements
"""

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1: 5] # [2, 3, 4, 5]
print(a)
skip_one = mylist[::2]
print(skip_one)
reverse_list = mylist[::-1]
print(reverse_list)

"""
If you want to copy a list to another list, you can use the copy() method. Avoid directly assigning the list to another variable, as this will create a reference to the original list in memory. Changes to the new list will affect the original list.
"""
list_ori = [1, 2, 3, 4]
list_cpy = list_ori
list_cpy.append(5)
print(list_ori)
print(list_cpy)

# better approach
list_copy = list_ori.copy()
list_copy.append(6)
print(list_ori)
print(list_copy)

"""
Alternative ways to copy a list include:
1.Using the list() constructor.
2.Using slicing ([:]).
These methods are similar to the copy() method in terms of functionality.
"""
copy_list = list(list_ori)
copy_list_sli = list_ori[:]

