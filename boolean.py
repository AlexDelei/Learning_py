#bool()
"""
The bool() function allows you to evaluate any value, and give you True or False in return
"""
print(bool("Helllo"))
print(bool(15))
"""
Most values are True
Any string is True except empty ones
Any number is True except 0
Any list, tuple, set and dictionary are True except empty ones

"""
"""
If you have an object that is made from a class with a __len__ function that returns 0 or False, then bool functino will evaluate to False

"""
class myclass():
    def __len__(self):
        return 0
    
myjob = myclass
print(bool(myjob))

"""
when you compare two values , the expression is evaluated in python and returns the Boolean answer of it
"""
print(10 > 9)
print(10 == 9)
print(4 > 3)

"""
You can create functions that return boolean values
"""
def myFunc():
    return True
if myFunc():
    print("YES")
else:
    print("NO!")

"""
Python has many inbuilt functions that return boolean values, like the isinstance() function which is used to
determine of a an object is of  certain data type

"""
x = "flower"
print(isinstance(x, int))