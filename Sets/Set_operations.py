# Sets: Unordered, mutable, no duplicates
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 6, 4, 8}
primes = {2, 3, 5, 7, 11}

"""
You can perform a union operation using the union() method or | operator, which returns a new set containing all elements from both sets.
This operation combines the elements, ensuring that there are no duplicates, as sets inherently maintain unique elements.
"""
u = odds.union(evens)
u1 = odds | evens
print(u)
print(u1)

"""
You can perform an intersection operation using the `intersection()` method or & operator, which returns a new set containing only the elements that are common to both sets. 
This method effectively finds the overlap between the two sets, ensuring that only shared elements are included in the result.
"""
i = evens.intersection(primes)
i1 = evens & odds
print(i)
print(i1)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
diff1 = setA - setB
print(diff1)
"""
setA.difference(setB)` will compute the difference between `setA` and `setB`. 
The result will be a new set containing elements that are in `setA` but not in `setB`. 
Specifically, it will return:- Elements {4, 5, 6, 7, 8, 9} which are in `setA` but not in `setB`.
"""
print(diff)

sym_diff = setB.symmetric_difference(setA)
"""
The `symmetric_difference` method returns a new set containing elements that are in either of the two sets but not in both. 
This operation identifies the unique elements in each set when compared to the other.
"""
print(sym_diff) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

setA.update(setB) # or setA |= setB

"""
The `update()` method will update the setA with the union of setA and setB  
"""
print(setA) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB) # or setA =& setB
"""
The `intersection_update()` method will update the setA with intersection of setA and setB
"""
print(setA) # {1, 2, 3}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB) # setA -= setB
"""
The `difference_update()` method will update the setA with difference of setA and setB
"""
print(setA) # {4, 5, 6, 7, 8, 9}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
"""
The `symmetric_difference_update()` method will update the setA with element which are not the difference of setA and setB
"""
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

if setB.issubset(setA):
    print('all elements of setB are present in setA')
else:
    print('Not all elements of setB are present in setA')

"""
The `issubset()` is used to check whether the one set is the subset of another set
"""

if setB.issuperset(setA):
    print('all elements of setA are in setB')
else:
    print("setB is not a superset of setA")

"""
The `issuperset()` is used to check whether the one set is superset of another set
"""

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
if setA.isdisjoint(setC):
    print("No one element of setC is not present in setA i.e setA is disjoint of setC ")
else:
    print("Some of the elements in setA are present in setC so, which are not disjoint sets.")
"""
The `isdisjoint()` is used to check the given sets are disjoint to each other or not 
"""

"""
If you want to copy a set to another set which can be done by using copy() method
and never copy a set by assigning to another variable which will effect the original set
if you done any changes to copied set
"""
setCopy = setA
setCopy.add(11)
print(setCopy)
print(setA)

# better and recommended way
setCopy = setA.copy()
setCopy.add(12)
print(setCopy)
print(setA)


