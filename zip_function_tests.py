"""THIS CODE SHOWS EXAMPLES OF ZIP FUNCTION USAGES.
"""

# Initialize two lists
#
people= ['Conrad', 'Alice', 'Emily']
ages= [23, 45, 67]

# Print all <person, age> tuples (in an efficient way and feeding lists to zip function)
#
print('\n')
for person, age in zip(people, ages):
    print(person, age)
print('\n')

# Initialize a third list of cities, with the same length as the preceding lists
#
cities= ['New York', 'Tripoli', 'Mosca']

# Print all <person, age, city> tuples (in an efficient way and fedding lists to zip function)
#
for person, age, city in zip(people, ages, cities):
    print(person, age, city)
print('\n')

