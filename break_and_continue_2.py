
"""THIS CODE SHOWS EXAMPLES OF BREAK AND CONTINUE STATEMENTS USAGEE
"""

someIntegers= [1, 3, 45, 78, 9, 56, 78]
someTuples= [('NO', 'YOU CAN\'T'), ('YES', 'YOU CAN'), ('NO', 'YOU CAN'), ('YES', 'YOU CAN \'T')]
someDicts= [{'key_1': 'value_1', 'key_2': 'value_2'}, {'key_3': 'value_3'}, {'key_4': 'value_4', 'key_5':'value_5', 'key_6': 'value_3'}]
someLists= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Stop when 45 is detected in someIntegers
#
found= False
for integer in someIntegers:
    if(integer is 45):
        found= True
        break
if found is True:
    print('\n')
    print("45 found in someIntegers")
else:
    print('\n')
    print("45 hasn't been found into someIntegers")

# Find all positive answers
#
print('Positive answers found: ')
for answer in someTuples:
    confirmation, permission= answer
    if confirmation is 'NO':
        continue
    print(confirmation, permission)

# Find the key(s) with value 'value_3'
#
found= False
ownerDict= None
for dictItem in someDicts:
    if 'value_3' not in dictItem.values():
        continue
    found= True
    print("Found key(s) with value \'value_3\' in the dictionary: ", dictItem)

if found is False:
    print("value \'value_3\' not found in any of the examined dictionary")

print('\n')