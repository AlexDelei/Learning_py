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

6. Membership Operators
Are used to test if a sequence are represented in an object
Operator    Description                                           Example_in_use
  in        Returns True if a sequence with the specified value   x in y
            is present in the object
  not in    Returns True if a sequence with the specified value   x not in y
            is not present in an object

7.Python Bitwise operators
Are used to compare 'binary numbers'
Operator    Name      Description                       Example
  &         AND       Sets each bit to 1 if both bits    x & y
                      are 1
  |         OR        sets each bit to 1 if one of both  x | y
                      bits  are 1
  ^         XOR       sets each bit to 1 if only one of  x ^ y
                      two bits is 1
  ~         NOT       inverts all bits                    ~x
  <<       Zero fill   shift left by pushing zeros in      x << 2
           left shift  from the right and let the leftmost
                       bits fall off
  >>      signed right  shifts right by pushing copies of   x >> 2
          shift               the leftmost bit in from the left,
                        and let the rightmost bits falloff
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

a = 1
a <<= 1
print(a)

#membership operators
x = ["banana", "pineapple"]
print("pineapple" in x)
"""
#operator precedence
this describes the order in which the operations are performed i.e from highly prioritized

This is the order , from highly to lowly prioritiezed:
Operator

()
**
+x, -x, ~x
* / // %
+ , -
>> , <<
&
^
|
==  !=  >  >=  <  <=  is  is not  in  not in 
not(logical not)
and(logical and)
or(logical or)
"""