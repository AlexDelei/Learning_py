#Python operators
"""
The operator groups in python are:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

1. Arithmetic operators
Operator    Name
  +         addition
  -         subtraction
  *         multiplication
  /         division
  %         modulus
  **        exponentiation
  //        floor division

2. Assignment operators
Assign values to variables
Operator    Example    Same as
  =         x = 5       x = 5
  +=        x += 3      x = x + 3
  -=        x -=3       x = x - 3
  *=        x *= 3      x = x * 3
  /=        x /= 3      x = x / 3
  %=        x %= 3      x = x % 3
  //=       x //= 3     x = x // 3
  **=       x **= 3     x = x ** 3
  &=        x &= 3      x = x & 3
  |=        x |= 3      x = x | 3
  ^=        x ^= 3      x = x ^ 3
  >>=       x >>= 3     x = x >> 3
  <<=       x <<= 3     x = x << 3

3. Comparison operators
Compare two values
Operator    Name
  ==        equal to
  !=        not equal to
  >         greater than
  <         less than
  >=        greater than or equal to
  <=        less than or equal to

4. Logical operators
Are used to combine conditional statements
Operator    Description                                     Example in use
  and       Returns true if both conditions are true        x < 5 and x < 10
  or        Returns true if one of the conditions is true   x > 5 or x > 3
  not       reverses the condition                          not(x < 5 and x < 10)

5. Identity operators
Are used to compare the objects , not if they are equal,but if they are actually the same objects with the same memory allocation
Operator        Description                                             Example
 is             Returns true if both variables are the same object      x is y
 is not         Returns true if both variables are not the same objects  x is not y

"""
x = ["bananas", "apple"]
y = ["bananas", "apple"]
z = x

print(x is z)
#prints True because thay are the same objects
print(x is y)
#prints False since thay are not the same objects even if they have the same content
print(x == y)
#prints True since this compares the two values . This brings the difference be2wn
#'is' and '=='