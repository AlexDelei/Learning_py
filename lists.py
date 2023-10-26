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
#output = ['student in', 'University is ']

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

"""
sorting lists - lists have a sort() functions that sorts the list alphabetically, ascending order or  by default

sort()
"""

my_list = list(("mangoes", "pawpaws", "apple", "strawberries", "passionfruits", "watermelons", "tomatoes"))
my_list.sort()
print(my_list)
#output = ['apple', 'mangoes', 'passionfruits', 'pawpaws', 'strawberries', 'tomatoes', 'watermelons']
"""
sorting numerically
"""
list2 = list((340, 567, 234, 109, 790, 675, 289, 987, 111, 42))
list2.sort()
print(list2)
#output = [42, 109, 111, 234, 289, 340, 567, 675, 790, 987]
"""
sorting in a descending order
"""
list3 = list(("mangoes", "pawpaw", "apple", "strawberries", "passionfruits", "watermelons", "tomatoes"))
list3.sort(reverse= True)
print(list3)
#output = ['watermelons', 'tomatoes', 'strawberries', 'pawpaw', 'passionfruits', 'mangoes', 'apple']
list4 = list((340, 567, 234, 109, 790, 675, 289, 987, 111, 42))
list4.sort(reverse=True)
print(list4)
#output = [987, 790, 675, 567, 340, 289, 234, 111, 109, 42]

"""
reverse() function reverses the current sorting of elements in the list
"""
list3.reverse()
print(list3) # = ['apple', 'mangoes', 'passionfruits', 'pawpaw', 'strawberries', 'tomatoes', 'watermelons']
list3.reverse()
print(list3)# = ['watermelons', 'tomatoes', 'strawberries', 'pawpaw', 'passionfruits', 'mangoes', 'apple']

"""
custom sort function
The function will return a number that will be used to sort the list (the lowest number first)
"""
def myfunc(n):
    return abs(n - 50)

list5 = list((200, 345, 423, 90, 235))
list5.sort(key= myfunc)
print(list5)
"""
sort() function is case sensitive resulting in all capital letters being sorted before lowercase letters
"""
list6 = list(("banana", "dragon fruits", "Oranges", "Kiwi", "cherry"))
list6.sort()
print(list6)
#output = ['Kiwi', 'Oranges', 'banana', 'cherry', 'dragon fruits']
"""
performing case-insensititve sorting
str.lower is used as a key functoion

"""
list6
list6.sort(key=str.lower)
print(list6)
#output = ['banana', 'cherry', 'dragon fruits', 'Kiwi', 'Oranges']
"""
copying a list with a copy() function
"""
list7 = ["apple", "juice", "melon"]
#list8 = list7.copy()
#print(list8)
#output = AttributeError: 'list' object has no attribute 'copy'
"""
an alternative way which is working is using list() function
"""
list7 = ["apple", "juice", "melon"]
list8 = list(list7)
print(list8)
#output = ['apple', 'juice', 'melon']

"""
Joining , concatinating two lists
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# output = ['a', 'b', 'c', 1, 2, 3]

"""
another way is appending the elements one by one
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
#output = ['a', 'b', 'c', 1, 2, 3]

"""
Not forgetting the extend() function which appends the elements of one list to the other
"""
list1 = ["a", "b", "c"]
list2 = [9, 8, 7]

list1.extend(list2)
print(list1)
#output =  ['a', 'b', 'c', 9, 8, 7]

"""
The lists in-built functions/methods

insert()        -   adds item/items at specified position in a list
append()        -   adds item at the end of a list
list()          -   inbuilt for creating a new list
clear()         -   clears the contents of a list
count()         -   counts the number of elements specified in a value
remove()        -   removes the specified list item
pop()           -   removes the item at the index provided
sort()          -    sorts the list in a certain order
reverse()       -   this reverses the way the current list is sorted
"""