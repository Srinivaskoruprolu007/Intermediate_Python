# Lists : Ordered, mutable, allows duplicate elements

"""
A list can be created either using square brackets [] or the list() constructor.
"""
mylist = ["banana", "cherry", "apple", "mango"]
print(mylist)

mylist2 = list()

"""
Lists allow multiple data types, meaning they can store strings, integers, booleans, and more.
"""
mylist2 = ["Orange", 2, 2.50, True]

"""
Lists can also contain duplicate values
"""
mylist3 = [1, 1, 2, 4, 5, 9]

"""
We can access elements in a list using indexing, which ranges from 0 to the length of the list minus 1. Lists also support negative indexing, allowing you to access elements from the end of the list.
"""
# first element
print(mylist3[0]) # 1
# last element
print(mylist3[-1]) # 9

"""
You can iterate over a list using a for-in loop or a for loop with range from 0 to the length of the list minus 1
"""
for fruit in mylist:
    print(fruit)

for i in range(len(mylist3)):
    print(mylist3[i])


"""
You can also check if a given element is present in the list using the membership operator in.
"""
if "banana" in mylist:
    print("yes")
else:
    print("no")

# length of the list by using len() method
print(len(mylist3))


"""
You can also add elements to the end of the list using the append() method.
"""
mylist3.append(34)
print(mylist3)

"""
You can also insert elements at a specific index using the insert() method by passing the index and the value to be inserted
"""
mylist3.insert(__index=4, __object=5)
print(mylist3)

"""
You can also remove the last element from the list using pop() method
"""
deleted = mylist3.pop()
print(deleted)

"""
You can also remove a specific item from the list using the remove() method. Be careful: if the element you want to delete is not in the list, you will get a ValueError.
"""
removed_item = mylist.remove("Cherry")
print(removed_item)

"""
You can delete all items from the list using clear()
"""
mylist3.clear()
print(mylist3)

"""
You can reverse the elements in a list and sort them in ascending or descending order. To reverse the list, use the reverse() method. To sort in ascending or descending order, use the sort() method with the reverse=True parameter for descending order. The sort() method sorts the list in place. If you prefer not to modify the original list, use the sorted() function to create a new list with the sorted elements
"""
number_list = [4, 5, 6,2, 1, 6, 8]
print(number_list)
reversed_numbers = number_list.reverse()
print(reversed_numbers)
# in-place sorting
number_list.sort()
print(number_list)
# descending order
number_list.sort(reverse=True)
print(number_list)

# new-instance sorting
sorted_nums = sorted(number_list)
print(sorted_nums)

sorted_desc = sorted(number_list, reverse=True)

"""
Tip: You can also create a list with the same value repeated a specific number of times by using the multiplication operator. For example, [value] * n creates a list with value repeated n times.
"""
new_list = [0] * 5

"""
You can concatenate two list into one list by using + operator
"""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
concat_list = list1 + list2
print(concat_list)

"""
The extend() method adds all the elements of another list (or any iterable) to the end of the current list.
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

"""
The index() method returns the index of the first occurrence of a specified value. If the value is not found, it raises a ValueError.
"""
fruits = ["apple", "banana", "cherry", "banana"]
index_banana = fruits.index("banana")
print(index_banana)  # 1

"""
The count() method returns the number of occurrences of a specified value in the list.
"""
num_list = [1, 2, 2, 3, 4, 2]
count_twos = num_list.count(2)
print(count_twos)  # 3

"""
The copy() method returns a shallow copy of the list.
"""
original_list = [1, 2, 3]
copy_list = original_list.copy()
print(copy_list)  # [1, 2, 3]

"""
The del statement allows you to delete items from a specific index or a slice of the list. It can also be used to delete the entire list.
"""
# Deleting an element by index
del original_list[1]
print(original_list)  # [1, 3]

# Deleting the entire list
del list1
# print(list1)  # This would raise a NameError because list1 no longer exists.

my_list=[1,2,3,45]
