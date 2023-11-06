"""
Set

Are defined using {}

Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

Set items are unordered, unchangeable, and do not allow duplicates
1. Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and CANNOT be referred to by index or key.

2. Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

3. Duplicates Not Allowed
Sets cannot have two items with the same value.

"""
"""
sets can be of any data types
"""
thisset = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}
"""
set() constructor
"""

"""
Accessing Items in a set

**You CANNOT ACCESS ITEMS IN A LIST BY USING AN INDEX
"""
#print(thisset[0])
#output = TypeError: 'set' object does not support indexing
"""
But you can loop through and print the values
"""
for i in thisset:
    print(i)
    