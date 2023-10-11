#Global Variables - declared outside the/a function
x = "Fantastic"

def myfunc():
    x = "amazing"
    print("Excellent and " + x)

myfunc()
print("Python is " + x)

#changing the value of a global variable
x = "awesome"
def my2():
    global x
    x = "fantastic"

print("first " + x)
my2()
print("second " + x)