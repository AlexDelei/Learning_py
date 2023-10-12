"""

Like many other languages , strings in python are arrays of bytes
However, Python does not have a character data type, a single character is simply a string with a length of 1.


"""

b = "sweet, bananas"
print(b[0])

print("\n")
for x in "bananas":
    x = x
    print(type(x))
    print(x)

print("\n")
 
text = "The best things in this life are free!"
if "free" in text:
    print("Absolutely! 'free' is present in " + text)

print("\n")

text2 = "The bests things in this life are free!"
if "car" not in text2:
    print("No, 'car' is not in " + text2)

print("\n")

#Slicing 
b = "Alex Delei"
print(b[2:7])

print("\n")

c = "Alex Delei Saitoti"
print(c[2:])

print("\n")

d = "Alex Delei Saitoti"
print(d[-5:-2])

print("\n")

#Modifying strings
"""
printing in uppper case

"""
a = "alex delei saitoti."
print(a.upper())

print("\n")

"""
printing in lower case

"""
e = "ALEX DELEI SAITOTI."
print(e.lower())

print("\n")

"""
strip() - removes white spaces at the beginning and/or after the actual text

"""
a = "# Alex Delei  #"
print(a.strip())
a = a.upper()
print(a.strip())

print("\n")

"""
replace() - replaces a string with another one

"""
a = "alex delei saitoti"
a = a.upper()
print(a.replace("ALEX", "WETH"))

print("\n")
"""
split() - this function splits string into substrings if it finds instances of a separator.

"""
s = """ Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. """
s = s.upper()
b = len(s)
print(s.split(","))
print(b, "words")

print("\n")

"""
concatinating strings or words

"""
a = "i"
b = " am a student"
c = " at Kirinyaga university"

a = a.upper()
z = c
c = c[3:].upper()
print(a + b + z[:3] + c)


print("\n")

"""
We can combine strings and numbers i.e 
a = 18
text = "My name is Alex and am " + a
print(text)

On the other way, we can combine strings and numbers using format() function.
The format function takes passed arguments , formats them and places them in the string where the placeholders {} are.

"""
age = 10
jina = "john"
name = "My name is {} and i am {} years old"
#if "john" in name:
 #   x = "john"
  #  x.upper()
print(name.format(jina, age))

#using indexes
a = "yoghurt"
b = "cakes"
c = "soda"
f = 100
g = 180
h = 45
items = "The prices of : {2} is {4} shillings, {1} for {5} shillings and {0} for {3} shillings only"
print(items.format(a, b, c, f, g, h)) #Can place in any order so as long there are indices

print("\n")

"""
escape characters in python. 
An escape character is a backslash \ followed by the character you want to insert.

Other escape characters in python
\'  for sinlge quote
\\ for backslash
\n for new line
\r for carriage return
\t for tab
\b for backspace
\f for form feed
\ooo for octal value
\xhh for Hexadecimal value

"""