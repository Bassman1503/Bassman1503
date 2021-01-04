""" THIS CODE SHOWS EXAMPLES OF HOW IT IS POSSIBLE TO IMPLEMENT EFFICENT CODE 
FOR LOOPING ON MULTIPLE SEQUENCES OF THE SAME LENGTH.
"""

# Create two different lists 
#
people= ['Conrad', 'John', 'Emily', 'Alice']
ages= [23, 78, 45, 15]

# Try to loop on two lists in an inefficient way (using access via positional index)
#
print('\n')
for position in range(len(people)):
    person= people[position]
    age= ages[position]
    print(person, age)
print('\n')

# Try to loop on the two lists in an efficient way (using zip function and implicit assignment)
#
for person, age in zip(people, ages):
    print(person, age)
print('\n')

# Try to loop on the two lists using zip function and explicit assignemnts in "for" body
#
for data in zip(people, ages):
    person, age= data
    print(person, age)
print('\n')