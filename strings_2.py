"""
String Methods

capitalize() - Converts the first character to upper case

casefold() - Converts string into lower case

count() - Returns the number of times a specified value occurs in a string

center() - Returns a centered string

encode() - Returns an encoded version of the string

endswith() - Returns true if the string ends with the specified value

expandtabs() - Sets the tab size of the string

find() - Searches the string for a specified value and returns the position of where it was found

format() - Formats specified values in a string

format_map() - Formats specified values in a string

index() - Searches the string for a specified value and returns the position of where it was found

isalnum() - Returns True if all characters in the string are alphanumeric

isalpha() - Returns True if all characters in the string are in the alphabet

isascii() - Returns True if all characters in the string are ascii characters

isdecimal() - Returns True if all characters in the string are decimals

isdigit() - Returns True if all characters in the string are digits

isidentifier() - Returns True if the string is an identifier

islower() - Returns True if all characters in the string are lower case

isnumeric() - Returns True if all characters in the string are numeric

isprintable() - Returns True if all characters in the string are printable

isspace() - Returns True if all characters in the string are whitespaces

istitle() - Returns True if the string follows the rules of a title

isupper() - Returns True if all characters in the string are upper case

join() - Joins the elements of an iterable to the end of the string

ljust() - Returns a left justified version of the string

lower() - Converts a string into lower case

lstrip() - Returns a left trim version of the string

maketrans() - Returns a translation table to be used in translations

partition() - Returns a tuple where the string is parted into three parts

replace() - Returns a string where a specified value is replaced with a specified value

rfind() - Searches the string for a specified value and returns the last position of where it was found

rindex() - Searches the string for a specified value and returns the last position of where it was found

rjust() - Returns a right justified version of the string

rpartition() - Returns a tuple where the string is parted into three parts

rsplit() - Splits the string at the specified separator, and returns a list

rstrip() - Returns a right trim version of the string

split() - Splits the string at the specified separator, and returns a list

splitlines() - Splits the string at line breaks and returns a list

startswith() - Returns true if the string starts with the specified value

strip() - Returns a trimmed version of the string

swapcase() - Swaps cases, lower case becomes upper case and vice versa

title() - Converts the first character of each word to upper case

translate() - Returns a translated string

upper() - Converts a string into upper case

zfill() - Fills the string with a specified number of 0 values at the beginning

"""

#capitalize()
"""
Defn:
The capitalize() function returns a string where the fist character is uppercase and the rest is lower

Syntax:
string_variable.capitalize()

NO PARAMETER VALUES

"""
name = "alex loves python!"
x = name.capitalize()
print(x)

print("\n")


#casefold()
"""
Defn:
The casefold() function returns a string with lowercase characters
It is similar to lower() function  but casefold() is stronger and more aggressive meaning it will convert many characters into lowercase

Syntax:
string_variable.casefold()

NO PARAMETERS

"""

#center()
"""

Defn:
The center() function will center align the string, using a specified character (space is default) as the fill character.

Syntax:
string_variable.center(length, character)

where -> length (is a must) is the length of the returned string
      -> character (optional) is the character to fill the missing space on each side. Default is " " (space) 


"""

text = "pineappple"
x = text.center(50)
print(x)

print("\n")

#count()
"""

Defn:
The count() function returns the number of times a specified value appears in the string

Syntax:
string_value.count(value, start, end)

where the parameters -> value (a must) is the string to search for
                     -> start (optional) is an integer , the position to start the search
                     -> end   (optional) is an integer , the postion to end the search, default is the end of the string   


"""

text = "I love apples , apples are my favorite"
x = text.count("apples", 0, )
print(x)

print("\n")

#encode()
"""

Defn:
The encode() funtion encodes a string using a specified encoding. Default encoding uses UTF-8 

Syntax:
string_variable.encode(encoding = encoding, errors = errors)

where parameter values -> encoding  (optional) is a string specifying the encoding to use
                       -> errors  (optional) is a string specifying the error method

                       legal error methods are
                      1. 'backslashreplace' - uses a backslash instead of the character that could not be encoded
                      2. 'ignore' - ignores the character that can not be encoded
                      3. 'namereplace' - replaces the character with a text explaining the character
                      4. 'strict' - Default, raises an error on failure
                      5. 'replace' - replaces the character with a questionmark
                      6. 'xmlcharrefreplace' - replaces the caharacter with an xml character

"""

name = "My name is Ståle"
print(name.encode(encoding="ascii", errors="backslashreplace"))
#print(name.encode(encoding="ascii", errors="ignore"))