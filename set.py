""" THIS CODE SHOS EXAMPLES OF SET OBJECTS CREATION AND USAGE
REMEMBER THAT OBJECT OF A SET ARE HASHABLE.
"""

#-------- MUTABLE SET OBJECTS --------------
#

# Creation of an empty set object.
#
aFirstSet= set()

# Add elements to the previous set.
#
aFirstSet.add(1)
aFirstSet.add(2)
print("First set: ", aFirstSet)
# Creation of a set passing a list of elements as input to the constructor.
#
aSecondSet= set([2, 3, 4, 5])
print("Second set: ", aSecondSet)

# Creation of a set using curly braces.
#
aThirdSet= {56, 7, 991}
print("Third set: ", aThirdSet)

# Remove an element from the first set.
#
aFirstSet.remove(2)
print("Removing 2 form the first set: ", aFirstSet)

# Try to add a duplicate to the second set. 
# Duplicates are not allowed in a set.
#
aSecondSet.add(4)
print("Adding a duplicate to the second set...\nDuplicates are not allowed: ", aSecondSet)

aFirstSet.add(34)
aFirstSet.add(7)
aFirstSet.add(81)
print("Adding elements 34, 7, 81 to the first set...", aFirstSet)

# Union of two sets.
#
print("Union of the first and second set: ", aFirstSet | aSecondSet)

# Intersection of the first two sets.
#
print("Intersection of the first and second set: ", aFirstSet & aSecondSet)

# Difference between the first and the second set.
#
print("Difference between frist and second set (order: first set - second set): ", aFirstSet - aSecondSet)

# Test membership of some elements to the first set.
#
print("7 is in the first set? ", 7 in aFirstSet)
print("566 is in the firsts set? ", 566 in aFirstSet)


#----------- IMMUTABLE SET OBJECTS ----------
#

# Create an empty immutable set object - or frozenset.
#
aFirstFrozenSet= frozenset()
print("first frozen set: ", aFirstFrozenSet)

# Try to add an element to the first frozen set.
#
#print("Trying to add an element to the first frozen set....")
#aFirstFrozenSet.add(1)

# Try to remove an element from a second frozen set.
aSecondFrozenSet= frozenset([1, 2, 3])
print("Second frozen set: ", aSecondFrozenSet)
#print("Trying to remove an element from the second frozen set....")
#aSecondFrozenSet.remove(2)


# Union of two frozen sets still work on them.
#
print("Union of the first and second frozen sets: ", aFirstFrozenSet | aSecondFrozenSet)

# Intersection of the first and second frozen still works on them.
#
print("Intersection of the first and second frozen set: ", aFirstFrozenSet & aSecondFrozenSet)

# Difference between the first and second froze3n set still works on them.
#
print("Difference between firt and second frozen set: ", aFirstFrozenSet - aSecondFrozenSet)

# Test membership of some elements to the second frozen set.
#
print("7 is in the second frozen set? ", 7 in aSecondFrozenSet)
print("2 is in the second frozen set? ", 2 in aSecondFrozenSet)