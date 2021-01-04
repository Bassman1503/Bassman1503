
"""THIS CODE SHOWS EXAMPLES OF LOOPING FUNCTIONS
"""

# Create a list of surnames
#
surnames= ['Rashla', 'Sumaki', 'Alderman']

# Print each surname 
#
print('\n')

for surname in surnames:
    print(surname)
print('\n')

# Print each surname and its position in the list
#
for position, surname in enumerate(surnames):
    print(position, surname)
print('\n')