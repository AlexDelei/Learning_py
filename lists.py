#Python Lists
"""
Lists are used to store multiple items in a single variable
Lists is one of the 4 in-built python data types used to to hold data, the other three are:
 -> tuple
 -> set
 -> dictionary

Lists are created using SQUARE brackets ' [] '
The lists items are orderd, changeable and allow duplicate.
#ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

#changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#allow duplicate
You can the same items in the list

Lists are indexed i.e [0] - first item

"""
#To determine the number of items in the list;
fruits = ["apples", "watermelons", "passionfruits", "oranges"]
print(len(fruits))

"""
Lists can be of any data types
"""
list1 = ["mercedese", "rolls royce", "range rover"]
list2 = [5000, 3450, 5000]
list3 = [True, False, True]
"""
Lists can have mixed data types too
"""
list4 = ["rolls royce", 4500, True]
"""
What is the data type of a list?

<class 'list'>
"""

"""
List constructor 'list()'
You can create a new list using the list() function

"""
thislist = list(("apples", 400, True)) #uses double rounded brackets
print(thislist)

#ACCESSING ITEMS IN A LIST
print(list1[2])
#RANGE OF INDEXES
list5 = list(("Being a", "student in", "University is ", "a good feeling"))
print(list5[1:3])
#output = 'student in', 'University is ']

#Range of Negative indexes
"""
Means starting from the back,
"""
print(list5[-4:])
#output = ['Being a', 'student in', 'University is ', 'a good feeling']
print(list5[-2:-1])
#output = ['University is ']
if "range rover" in list1:
    print("Yeah it is there!!")

"""
Changing item value

"""
list5[2] = "a private university"
print(list5)
#output = ['Being a', 'student in', 'a private university', 'a good feeling']

"""
changing a range of item values
"""
list5[1:3] = "lecturer in", "a University is"
print(list5)
#output = ['Being a', 'lecturer in', 'a University is', 'a good feeling']

"""
Inserting items

To insert a new list item, without replacing any of the existing values, we can use the insert() function.
The insert() function, inserts an item at the specified index

"""
list1 = ["mercedese", "rolls royce", "range rover"]
list1.insert(0, "toyota")
print(list1)
#output = ['toyota', 'mercedese', 'rolls royce', 'range rover']

"""
Append items

To add item(s) at the end of a list, we use the append() function

"""
fruits = ["apples", "watermelons", "passionfruits", "oranges"]
fruits2 = list(("pineapples", "tomatoes", "strawberries", "blueberries"))
fruits.append("mangoes")
print(fruits)
fruits2.append("pawpaw")
print(fruits2)
#output = ['apples', 'watermelons', 'passionfruits', 'oranges', 'mangoes']
#output = ['pineapples', 'tomatoes', 'strawberries', 'blueberries', 'pawpaw']

"""
Extend list
To append elements from another list to the current list, use the extend() function.

Appending element of 'fruits' list to 'fruits2' list.
"""
fruits = ["apples", "watermelons", "passionfruits", "oranges"]
fruits2 = list(("pineapples", "tomatoes", "strawberries", "blueberries"))
fruits2.extend(fruits)
print(fruits2)
#output = ['pineapples', 'tomatoes', 'strawberries', 'blueberries', 'apples', 'watermelons', 'passionfruits', 'oranges']
"""
The extend() function does not have to append lists only ,  but also any iterable object
 -> sets
 -> tuples
 -> dictionaries

"""
fruits2 = list(("pineapples", "tomatoes", "strawberries", "blueberries"))
thistuple = ("kiwi", "bananas")
fruits2.extend(thistuple)
print(fruits2)
#output = ['pineapples', 'tomatoes', 'strawberries', 'blueberries', 'kiwi', 'bananas']

"""
Removing list items

remove() fiunction removes the specified list item
"""
print(fruits2) # this is after appending the two lists
fruits2.remove("bananas")
print(fruits2)
#output = ['pineapples', 'tomatoes', 'strawberries', 'blueberries', 'kiwi']

"""
if there are duplicate items , the remove function removes the first one that is occuring in  the list
"""
"""
Removing at the specified index

pop() function removes an item at a specified index, if no index specified, it removes the last item

"""
print(list5)#['Being a', 'lecturer in', 'a University is', 'a good feeling']
list5.pop(2)
print(list5)#['Being a', 'lecturer in', 'a good feeling']
list5.insert(2, "a University is")
print(list5)#['Being a', 'lecturer in', 'a University is', 'a good feeling']
"""
del keyword also removes at the specified index
"""
del list5[2]
print(list5)#['Being a', 'lecturer in', 'a good feeling']
"""
clear() function empties a list 
"""
#test = ["alex", "delei", 18]
#test.clear()
#print(test)#AttributeError: 'list' object has no attribute 'clear'

"""
LOOPING THROUGH A LIST

"""
list5.insert(2, "a University is")
for x in list5:
    print(x)
    """
    Being a
    lecturer in
    a University is
    a good feeling
    """
"""
Looping through the index numbers

for this to happen , we use the range() function and len() function

"""
list5
for i in range(len(list5)):#in range works the same as ; i < no.of list items; i++
    print(list5[i])
    """
    Being a
    lecturer in
    a University is
    a good feeling
    """
list5
i = 0
while i < len(list5):
    print(list5[i])
    i = i + 1
    """
    Being a
    lecturer in
    a University is
    a good feeling
    """
"""
Looping through using list comprehension
"""
list5
#[print(x) for x in list5]
"""
[print(x) for x in list5]
     ^
SyntaxError: invalid syntax
"""

list5
newlist = []
for x in list5:
    if "lecturer" in list5:
        newlist.append(x)
        break
        

print(newlist)