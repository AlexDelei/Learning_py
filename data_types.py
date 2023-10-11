"""
various data types in python
text type: str
numeric types: int, float, complex
sequence types: list, tuple, range
mapping types: dict
set types: set , frozenset
boolean type: bool
binary types: bytes, bytearray, memoryview
none type: NoneType
"""
"""
x = int(24)
x = float(23.5)
x = complex(1j)
x = str("ALEX")
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = dict(name="John", age=36)
x = range(45)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytearray(5)
x = memoryview(bytes(5))
x = bytes(5)
"""
#Type conversion
x = 1
y = 39.8
z = 1j

#converting from int to float
a = float(x)

#conerting from float to int
b = int(y)

#converting from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print("\n")

print(type(a))
print(type(b))
print(type(c))