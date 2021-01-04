
"""THIS CODE SHOWS EXAMPLES ABOUT TUPLE CREATION AND USAGE.

Tuples are immutable sequences of heteregenous or omogeneous elements.
Tuples can be accessed via unpacking or indexing mechanisms. 
"""

# Example of tuple initialization using embracing round parenthesis.
#
print('Tuple initalization using embracing round parenthesis: aTuple = (1, 2, 3)\nThe result is:')
aTuple = (1, 2, 3)
print(aTuple)
print('\n\n')

# Example of tuple initialization without using embracing round parenthesis.
#
print('Tuple initialization without using embracing parenthesis: aTuple = 4, 5, 6\nThe result is:')
aTuple = 4, 5, 6
print(aTuple)
print('\n\n')

# Example of intialization of a tuple with a single element. Comma is needed
# after the first element; if comma is not used, interpreter will read the 
# initializing value as a simple value ebraced by parenthesis.
#
print('Example of intialization of a single element tuple; comma is neeeded after the unique element: aTuple = (42, )\nThe result is:')
aTuple= (42, )
print(aTuple)
print('\n\n')

# Access an element through indexing .
#
print('Accessing the first element of the tuple (1, 2, 3) by its index (0)...\nThe result is: ')
aTuple= 1, 2, 3
print(aTuple[0])
print('\n\n')

# Multiple assignment using a tuple of values as right value of the same assignment.
#
print('Multiple assignment using a tuple of values as right value of the same assignment: a, b, c, = 4, 5, 6\nPrinting assigned values...')
a, b, c = 4, 5, 6
print('a =', a)
print('b =', b)
print('c =', c)
print('\n\n')

# Testing membership of an element with respect to a tuple
#
print('Testing membership of an element with respect to a tuple')
print('Given tuple: (1, 2, 3)')
aTuple= (1, 2, 3)
print('Queries:\n\t - 1 is in (1, 2, 3)? (answer should be \"True\")\n', 1 in aTuple)
print(' - 4 is in (1, 2, 3)? (answer should be \"False\")', 4 in aTuple)
print('\n\n')

# A tuple can contain heterogeneous elements.
# Example of heterogeneous tuple
#
class Someclass:
    def __init__(self, objType):
        self.objType= 'a Someclass object'

obj= Someclass('Someclass')
aTuple= (1, 'anbc', obj)
print('An example of heterogeneous tuple:', aTuple)
print('Types of each objects contained in the tuple, respectively: ', type(aTuple[0]), type(aTuple[1]), type(aTuple[2]))
print('\n\n')

