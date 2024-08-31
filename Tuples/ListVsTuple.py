import sys
"""
The code compares the memory sizes of a list and a tuple containing the same elements.
The `sys.getsizeof()` function is used to determine the number of bytes used by each data structure.
Typically, tuples are more memory-efficient than lists because tuples are immutable and have a fixed size,
whereas lists have additional overhead to support dynamic resizing and mutability.
"""
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), " Bytes")
print(sys.getsizeof(my_tuple), " Bytes")

# let's check the iteration speed
"""
The code uses the `timeit` module to measure the execution time for creating a list and a tuple, each performed 1,000,000 times.
The `timeit.timeit()` function runs the provided statement (creating a list or tuple) repeatedly and returns the total time taken.
Typically, tuple creation is faster than list creation due to tuples being immutable and having a simpler structure compared to lists,
which have additional overhead for dynamic resizing and mutability.
"""
import timeit
# Measure the time it takes to create a list with 1,000,000 iterations
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
# Measure the time it takes to create a tuple with 1,000,000 iterations
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
