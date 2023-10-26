"""
Just like lists , tuples are used to store multiple items in a single variable
tuple is one of the four built-in data types in python used to store collection of data , the other three are 
-> lists
-> sets
-> dictionary

A tuple is a collection which is ordered and unchangeable
Tuples are written with ROUND BRACKETS
Tuple items are ordered , unchangeable and allow duplicates

1. Ordered
When we say they are ordered , it means that the items have a defined oreder and it wont change

2. Unchangeable
Means , we cannot change, add or remove items after the tuple has been created

3. Allow Duplicates
Since tuples are indexed , they can have items with the same value

"""

"""
Creating a tuple with one item.
To create a tuple with one item , you have to add a comma after the item , otherwise python will not recognize it as a tupple

"""
my_tuple = ("apple",)
print(type(my_tuple))
#output = <type 'tuple'>
"""
Data types

A tuple can be of any data type
"""
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

"""
A tuple can contain different data types
"""
tuple1 = ("abc", 34, True, 40, "male")

"""
its possible to create a tuple using  the tuple() function

"""
tuple4 = tuple(("apple", "banana", "cherry")) #note the rounded brackets
print(tuple4)
#output = ('apple', 'banana', 'cherry')

"""
To access the tuple items, you referr to their indexes inside square brackets
"""
print(tuple4[2])

"""
Range of indexes are the same as those for the lists
i.e
tuple[2:5]
tuple[2:]
tuple[:4]
tuple[-4:-1]
tuple[-1]
"""
fruits = tuple(("apple", "mangoes", "melons", "oranges"))
if "melons" in fruits:
    print("Yep ! Melons exist in fruits tuple")

#output = Yep ! Melons exist in fruits tuple


"""
Unpacking tuples

When we create tuples, we assign values to it, this is called 'packing'
But in python, we are also allowed to extract values into variables, a process called 'unpacking'

"""
fruits = tuple(("apple", "bananas", "mangoes"))
(green, yellow, red) = fruits

print(red)
print(yellow)
print(green)
#output = 
"""
mangoes
bananas
apple
"""
fruits = tuple(("apple", "banana", "cherry", "strawberry", "raspberry"))
#(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#output = 
"""
    (green, yellow, *red) = fruits
                    ^
SyntaxError: invalid syntax
"""

"""
Looping through a tuple
"""
fruits = tuple(("apple", "banana", "cherry", "strawberry", "raspberry"))
for c in fruits:
    print(c)

print("\n")

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print("\n")
"""
Looping through the index numbers which stand for the tuple items
"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])