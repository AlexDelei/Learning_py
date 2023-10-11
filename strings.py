"""

Like many other languages , strings in python are arrays of bytes
However, Python does not have a character data type, a single character is simply a string with a length of 1.


"""

b = "sweet, bananas"
print(b[0])

print("\n")
for x in "bananas":
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