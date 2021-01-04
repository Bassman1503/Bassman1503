"""THIS CODE SHOWS EXAMPLE ABOUT BYTEARRAY OBJECTS CREATION AD USAGE
"""

# Create an empty bytearray object.
#
print(bytearray())

# Create a bytearray object from an immutable range of values.
#
print(bytearray(range(5)))

# Create a bytearray object from a string.
#
print(bytearray("string", "utf-8"))

# Create a byearray object from an integer, which represents its size.
#
print(bytearray(5))

# Create a bytearray object from a bytes object
#
print(bytearray(b'string'))