
# Example of String objects manipulations. All operations on strings are read.only, 'cause
# a string object is ALWAYS immutable. As well, remember that string coding in Python is
# UTF-8 based.
#

string = 'The fuck'

# Indexing examples
#
print(string[0]) # Access to the first character of the string
print(string[len(string)-1]) # Remember that string indexing starts from 0, not from 1

# Slicing examples
#
print(string[1:])
print(string[:5])
print(string[:])


