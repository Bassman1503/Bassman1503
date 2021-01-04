
# itertools module is useful for efficient iterating
# 

# count is an infinite iterator
#
from itertools import count

# --------------------------------| INFINITE ITERATOR |----------------------------------#

# EXAMPLE 1
#
print('\n')
for n in count(2, 2):
    if n > 30:
        break
    print(n, end='  ')
print('\n')

# EXAMPLE 2
#
# Use count to generate enumeration of each element of a list
#
aList= ['one', 'two', 'three']
print(list(zip(aList, count(0))))
print('\n')

# EXAMPLE 3
#
# infinite loop
#
#for n in count(0):
#    print(n)

#-------------------------------| TERMINATE ON THE SHORTEST SEQUENCE |------------------#

# EXAMPLE 1
#
# Filter input data according to some selector
#
from itertools import compress

# Input of data to be filtered
#
someIntegers= range(10)

# Even numbers selector
#
evenSelector= [1, 0] * 5
oddSelector= [0, 1] * 5

# Filter data according to the proper selector
#
evenNumbers= list(compress(someIntegers, evenSelector))
oddNumbers= list(compress(someIntegers, oddSelector))

# Print results
#
print('\n')
print("Initial data source: ", list(someIntegers))
print("All even numbers contained in the intial data source: ", evenNumbers)
print("All odd numbers contained in the intial data source: ", oddNumbers)
print('\n')