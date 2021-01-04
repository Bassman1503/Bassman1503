"""THIS CODE SHOES EXAMPLES OF LIST CREATION AND USAGE
"""


#--------------------- INITIALIZATION ---------------------


# Create an empty list
#
aFirstList= [] # use "[]"
print("First list: ", aFirstList)
aSecondList= list() # use list constructor 
print("Second list: ", aSecondList)

# Create a list containing some elements using "[]"
#
aThirdList= [1, 2, 3]
print("Third list: ", aThirdList)

# Create a list from a  tuple of elements, passing this to the list constructor
#
aFourthList= list(('wtf', 1, 23, '34'))
print("Fourth list: ", aFourthList)

# Create a list from a string
#
aFifthList= list('HELLO')
print("Fifth list: ", aFifthList)


#--------------- LIST USAGES ---------------------

# Append an element to the end of a list
#
aFirstList.append(78)
print("First list modified: ", aFirstList)

# Extend the second list appending a list of two elements to its end. 
#
aSecondList.extend([34, 56])
print("Second list modified: ", aSecondList)

# Getting the position of an element of the third list.
#
position= aThirdList.index(3)
print("Getting the position of ", 3,  " in the third list: ", position)

# Insert a specified element in the specified position of the fourth list.
#
aFourthList.insert(1, 'CHE_CAZ...')
print("Insert \'CHE CAZ...\' in the second position of the fourth list: ", aFourthList)

# Remove the last element of the fifth list.
#
aFifthList.pop()
print("Remove the last element of the fifth list: ", aFifthList)

# Remove the element placed in the specified position of fourth list.
#
aFourthList.pop(2)
print("Remove the element placed in the third position of fourth list: ", aFourthList)

# Remove a specified element from the third list.
#
aThirdList.remove(2)
print("Remove 2 from the third list: ", aThirdList)

# Reversing the order of the second list's elements.
#
aSecondList.reverse()
print("Reversing the order of the second list's elements: ", aSecondList)

# Sorting the elements of the first list.
#
print("Sorting the elements of the first list...")
aFirstList.extend([45, 789])
print("Starting list: ", aFirstList)
aFirstList.sort()
print("Ordered list: ", aFirstList)

# Clear the elements of the second list.
#
aSecondList.clear()
print("Clearing the elements of the second list: ", aSecondList)

# Get the highest value for the first list.
#
print("Highest value of the first list: ", max(aFirstList))

# Get the lowest value of the first list
#
print("Lowest value of the first list: ", min(aFirstList))

# Get length of the first list
#
print("Length of the first list: ", len(aFirstList))

# Concatenate the first and second list
#
aSecondList.append(100)
print("Concatenating first and second list: ", aFirstList + aSecondList)

# Concatenate a list to itself two times
#
print("Concatenating a list to itself two times: ", aFirstList*2)

# Example of "sorted()" method usage.
#
from operator import itemgetter

aTuplesList= [(2, -1), (1, 3), (1, 1), (4, 5)]

print(sorted(aTuplesList))
print(sorted(aTuplesList, key=itemgetter(0)))
print(sorted(aTuplesList, key=itemgetter(0, 1)))
